import random
from random import shuffle
import sys
import shlex, subprocess
import time
from time import sleep
import operator
from time import time


#Algotimo genetikoa, irudiak aurreprozesatze egoki bat aurkitzeko, ondoren OCR egiteko
#Indibiduo bakoitza irudi eraldaketen lista bat izango da eta eraldaketa bat nahi adina aldiz agertzea onartuko da.
#N eraldaketa desberdin erabiliko dira:
# 	null (ezer ez aplikatzea)
#	MORAN 1
#	MORAN 2 (Yosuren indizeak diren eraldaketei, "_" bat jarriko diegu aurretik, komandoa desberdina baita)
#	MORAN 3
#	EDU 1
#	EDU 2 (Yosuren indizeak diren eraldaketei, "_" bat jarriko diegu aurretik, komandoa desberdina baita)
#	EDU 3
#	Negate
#	Edge 2
#	Edge 4
#	Edge 6
#	Edge 8
#	Contrast
#   Normalize
#	Lat 3x3
#	Gaussian-Blur 3x3


class indibiduo:
	#eraikitzailea
	def __init__(self, eral, ebal):
		self.eraldaketak = eral
		self.ebaluazioa = ebal
 
 
 
def hasierakoPopulazioa(eraldaketak):

	indibiduoak = []
	#eraldaketa denak denekin 14^2 indibiduo sortuko ditugu alde batetik
	for e1 in eraldaketak:
		for e2 in eraldaketak:
			eral = [e1,e2,"null","null","null","null","null","null"]
			inb = indibiduo(eral,-1)#horaindik ebaluatu gabe baitago
			indibiduoak.append(inb)

	# beste n_indibiduo guztiz ausaz
	for i in range(n_ausaz):
		eral = []
		for i in range(8):
			r = random.randrange(0, len(eraldaketak))
			eral.append(eraldaketak[r])
		inb = indibiduo(eral,-1)#horaindik ebaluatu gabe baitago
		indibiduoak.append(inb)

	return indibiduoak	
		

#Erdiak batetik eta beste erdiak bestetik
def elekzioaLehena(indibiduoak):

	kop = len(eraldaketak)*len(eraldaketak)
	lag1 = []
	lag2 = []

	print(len(indibiduoak))

	#sortutako moduaren arabera sailkatu
	lag1 = indibiduoak[0:kop]
	lag2 = indibiduoak[kop:len(indibiduoak)]

	#ordenatu
	lag1.sort(key=operator.attrgetter('ebaluazioa'),reverse = True)
	lag2.sort(key=operator.attrgetter('ebaluazioa'),reverse = True)

	#sailkapen bakoitzetik indibiduen erdiak hartu
	lag1 = lag1[0:int(n_indibiduaoak/2)]
	lag2 = lag2[0:int(n_indibiduaoak/2)]

	return lag1 + lag2
 


def elekzioa(indibiduoak):

	denera = 0
	gehikuntzak = []
	gurasoak = []
	aurrekoa = 0
	for ind in indibiduoak:
		denera += ind.ebaluazioa
		gehikuntzak.append(denera)

	#gurasoak hautatu(roulete wheel selection)
	for i in range(int(9/10*n_indibiduaoak)): #3/4 guraso
		#ausazko zenbakia lortu
		r = random.randrange(0, int(denera))
		#ausazko zenbakia zein indizeri dagokion aurkitu
		for j in range(len(indibiduoak)):
			if r < gehikuntzak[j]:
				gurasoak.append(indibiduoak[j])
				break
	return gurasoak	


def irudiakEraldatu(indibiduoak):
 
	komandoa = ""
	#indibiduo bakoitzeako
	for i in range(len(indibiduoak)):
		print (str(i)+". indibiduoa")
		ind = indibiduoak[i];

		#null diren eraldaketak kendu
		eralNullKendu = []
		for j in range(len(ind.eraldaketak)):
			eral = ind.eraldaketak[j]
			if eral != "null":
				eralNullKendu.append(eral)

		print(str(i)+". Indibiduoa")

		#eraldaketarik ez badu
		if 0 == len(eralNullKendu):

			komandoa = "cp "+argazkia+" temp/indibi"+str(i)
			args = shlex.split(komandoa)
			subprocess.call(args)

		for j in range(len(eralNullKendu)):
			eral = eralNullKendu[j]
			#yosuren indizeen kasuan izena aldatzeko
			komandoa2 = ""
			print(eral)

			#eraldaketa bakarra badu
			if 1==len(eralNullKendu):
				#yosuren indizeak bada
				if eral[0] == '_':
					zer = eral[2]
					num = eral[1]
					if len(eral)==3:
						komandoa = "./demo "+argazkia+" "+num+" "+zer
					elif len(eral)==4:
						komandoa = "./demo "+argazkia+" "+num+" "+zer+eral[3]
					komandoa2 = "mv thres.png temp/indibi"+str(i)
				#edge bada
				elif eral[2] == 'd':
					num = eral[0]
					komandoa = "convert -edge "+num+" "+argazkia+" temp/indibi"+str(i)
				#null bada
				elif eral[1]=='u':
					komandoa = "cp "+argazkia+" temp/indibi"+str(i)
				#normalize bada
				elif eral[2]=='r':
					komandoa = "convert -normalize "+argazkia+" temp/indibi"+str(i)
				#negate bada
				elif eral[0]=='n':
					komandoa = "convert -negate "+argazkia+" temp/indibi"+str(i)
				#kontarst bada
				elif eral[0]=='c':
					komandoa = "convert -contrast "+argazkia+" temp/indibi"+str(i)
				#gaussian-blur	
				elif eral[0]=='g':
					komandoa = "convert -gaussian-blur 3x3 "+argazkia+" temp/indibi"+str(i)
			
			#lehena bada
			elif j==0:
				#yosuren indizeak bada
				if eral[0] == '_':
					zer = eral[2]
					num = eral[1]
					if len(eral)==3:
						komandoa = "./demo "+argazkia+" "+num+" "+zer
					elif len(eral)==4:
						komandoa = "./demo "+argazkia+" "+num+" "+zer+eral[3]
					komandoa2 = "mv thres.png temp/ir"+str(j)
				#edge bada
				elif eral[2] == 'd':
					num = eral[0]
					komandoa = "convert -edge "+num+" "+argazkia+" temp/ir"+str(j)
				#null bada
				elif eral[1]=='u':
					komandoa = "cp "+argazkia+" temp/ir"+str(j)
				#normalize bada
				elif eral[2]=='r':
					komandoa = "convert -normalize "+argazkia+" temp/ir"+str(j)
				#negate bada
				elif eral[0]=='n':
					komandoa = "convert -negate "+argazkia+" temp/ir"+str(j)
				#kontarst bada
				elif eral[0]=='c':
					komandoa = "convert -contrast "+argazkia+" temp/ir"+str(j)
				#gaussian-blur	
				elif eral[0]=='g':
					komandoa = "convert -gaussian-blur 3x3 "+argazkia+" temp/ir"+str(j)

			#azkena bada
			elif j==len(eralNullKendu)-1:
				#yosuren indizeak bada
				if eral[0] == '_':
					zer = eral[2]
					num = eral[1]
					if len(eral)==3:
						komandoa = "./demo temp/ir"+str(j-1)+" "+num+" "+zer
					elif len(eral)==4:
						komandoa = "./demo temp/ir"+str(j-1)+" "+num+" "+zer+eral[3]
					komandoa2 = "mv thres.png temp/indibi"+str(i)
				#edge bada
				elif eral[2] == 'd':
					num = eral[0]
					komandoa = "convert -edge "+num+" temp/ir"+str(j-1)+" temp/indibi"+str(i)
				#null bada
				elif eral[1]=='u':
					komandoa = "cp temp/ir"+str(j-1)+" temp/indibi"+str(i)
				#normalize bada
				elif eral[2]=='r':
					komandoa = "convert -normalize temp/ir"+str(j-1)+" temp/indibi"+str(i)
				#negate bada
				elif eral[0]=='n':
					komandoa = "convert -negate temp/ir"+str(j-1)+" temp/indibi"+str(i)
				#kontarst bada
				elif eral[0]=='c':
					komandoa = "convert -contrast temp/ir"+str(j-1)+" temp/indibi"+str(i)
				#gaussian-blur bada
				elif eral[0]=='g':
					komandoa = "convert -gaussian-blur 3x3 temp/ir"+str(j-1)+" temp/indibi"+str(i)
			

			else:
			#yosuren indizeak bada
				if eral[0] == '_':
					zer = eral[2]
					num = eral[1]
					if len(eral)==3:
						komandoa = "./demo temp/ir"+str(j-1)+" "+num+" "+zer
					elif len(eral)==4:
						komandoa = "./demo temp/ir"+str(j-1)+" "+num+" "+zer+eral[3]
					komandoa2 =  "mv thres.png temp/ir"+str(j)
				#edge bada
				elif eral[2] == 'd':
					num = eral[0]
					komandoa = "convert -edge "+num+" temp/ir"+str(j-1)+" temp/ir"+str(j)
				#null bada
				elif eral[1]=='u':
					komandoa = "cp temp/ir"+str(j-1)+" temp/ir"+str(j)
				#normalize bada
				elif eral[2]=='r':
					komandoa = "convert -normalize temp/ir"+str(j-1)+" temp/ir"+str(j)
				#negate bada
				elif eral[0]=='n':
					komandoa = "convert -negate temp/ir"+str(j-1)+" temp/ir"+str(j)
				#kontarst bada
				elif eral[0]=='c':
					komandoa = "convert -contrast temp/ir"+str(j-1)+" temp/ir"+str(j)
				#gaussian-blur bada
				elif eral[0]=='g':
					komandoa = "convert -gaussian-blur 3x3 temp/ir"+str(j-1)+" temp/ir"+str(j)
			
			#komandoa exekutatu
			print(komandoa)
			args = shlex.split(komandoa)
			subprocess.call(args)
			#yosuren indizea bada
			if(komandoa2!=""):
				args = shlex.split(komandoa2)
				subprocess.call(args)		



			
def irudiakEbaluatu(indibiduoak, hiz):
	
	#indibiduo guztiak ebaluatu
	for i in range(len(indibiduoak)):
		komandoa = "tesseract -l "+hiz+" temp/indibi"+str(i)+" temp/indibi"+str(i)
		print(komandoa)
		args = shlex.split(komandoa)
		subprocess.call(args)

		#konparatu
		ehunekoa = testuakKonparatu("temp/indibi"+str(i)+".txt", textOCR)
		indibiduoak[i].ebaluazioa = ehunekoa

	return indibiduoak	


def testuakKonparatu(izena1, izena2):

	#lehenengo fitxategia irakurri
	fitx1 = open(izena1,'r')
	list1 = []
	for line in fitx1:
		l =  line.split(" ")
		for i in range(0,len(l)):
			string = l[i]
			string = string.replace(",","")
			string = string.replace(".","")
			string = string.replace("\n","")
			if string != "\n":
				list1.append(string)
	fitx1.close()

	#bigarren fitxategia irakurri
	fitx2 = open(izena2,'r')
	list2 = []
	for line in fitx2:
		l =  line.split(" ")
		for i in range(0,len(l)):
			string = l[i]
			string = string.replace(",","")
			string = string.replace(".","")
			string = string.replace("\n","")
			if string != "\n":
				list2.append(string)

	fitx2.close()

	kont = 0
	#Bi listen arteko antzekotasunak begiratu
	for i in range(0,len(list1)):
		 for j in range(0,len(list2)):
		 	if list1[i]!="" and list2[j]!="":
		 		if list1[i].lower() == list2[j].lower():
		 			kont = kont + 1
		 			list1[i]=""
		 			list2[j]=""
		 			break

	if len(list2)!=0:
		ehunekoa = kont * 100 / len(list2)
	else:
		ehunekoa = 0

	print("**************************************************************")
	print("1 fixategiak bigarrenarekin duen antza => %"+str(ehunekoa))
	print("**************************************************************\n")

	return ehunekoa


#guraso kopuruak bikoitia izan behar du
def gurutzaketak(gurasoak):

	berriak = []
	for i in range(int(len(gurasoak)/2)):

		gur1 = gurasoak[i]
		gur2 = gurasoak[i+1]
		#gurutzatu egingo ditugu(one point crossover)
		r = random.randrange(1, 101)
		#%90-eko probabilitatearekin egingo dugu gurutzaketa
		if(r > 10):
			#gurutzaketa zein puntutan egingo den erabaki
			r_ind = random.randrange(8)
			berria1 = gur1.eraldaketak[0:(r_ind)] + gur2.eraldaketak[r_ind:8]
			berria2 = gur2.eraldaketak[0:(r_ind)] + gur1.eraldaketak[r_ind:8]
			indBer1 = indibiduo(berria1,-1)
			indBer2 = indibiduo(berria2,-1)
			berriak.append(indBer1)
			berriak.append(indBer2)
		else:
			berriak.append(gur1)
			berriak.append(gur2)

	return berriak				




def mutazioa(berriak): 
	
	mutatuakEdoEz = []
	for berri in berriak:
		r = random.randrange(1, 101)
		#%10-eko probabilitatearekin egingo dugu mutazioa
		if(r > 90):
			non_ind = random.randrange(8)
			zer_ind = random.randrange(len(eraldaketak))
			berri.eraldaketak[non_ind] = eraldaketak[zer_ind]
			mutatuakEdoEz.append(berri)
		else:
			mutatuakEdoEz.append(berri)

	return mutatuakEdoEz
	

def populazioBerria(indibiduoak, berriak):
	
	indibiduoak.sort(key=operator.attrgetter('ebaluazioa'),reverse = True)
	lag = indibiduoak[0:int(n_indibiduaoak/10)]
	lag = mutazioa(lag)
	populazioBerria = berriak + lag
	return populazioBerria

 
 

print("*** ALGORITMO GENETIKOA ***")
print("")
start_time = time()

#eraldaketa mota guztiak 
#eraldaketak=["null","_1M","_2M","_3M","_1E1","_2E1","_3E1","negate","2edge","4edge","6edge","8edge","contrast","normalize"]
#eraldaketak=["null","negate","contrast","normalize"]
eraldaketak=["null","negate","contrast","normalize","gaussian-blur","_3M"]
#eraldaketak=["null","_1M","_2M","_3M","_1G","_2G","_3G","_1L","_2L","_3L","negate","2edge","4edge","6edge","8edge","contrast","normalize"]
#eraldaketak=["null","negate","2edge","contrast"]

#indibiduo bakoitzak 8 eraldaketa izango ditu
indibiduoak=[]
#populazio berriak sortzeko gurasoak
gurasoak=[]
#eraldatuko dugun argazki originalaren path-a
argazkia = sys.argv[1]
#OCR-egitean fallo kopurua begiratzeko eskuz idatzitako testua
textOCR = sys.argv[2]
#tesseract-i hizkuntza pasatzeko
hizkuntza = sys.argv[3]

#direktorioa sortu, argazkien eraldaketan bertan gordetzeko
komandoa = "mkdir temp"
args = shlex.split(komandoa)
subprocess.call(args)

while True:
	try:
		n_indibiduaoak = int(input("Zenbat indibiduo ?? ->"))
		n_ausaz = int(input("Zenbat ausaz ?? ->"))
		n_generazioak = int(input("Zenbat generazio ?? ->"))
		break
	except ValueError:
		print("Denek ZENBAKI OSOKOAK izan behar dute!\n")


#soluziorik onena gordeko duen indibiduoa
onenaIndibi = indibiduo([],-1)

indibiduoak = hasierakoPopulazioa(eraldaketak)
irudiakEraldatu(indibiduoak)
indibiduoak = irudiakEbaluatu(indibiduoak, hizkuntza)
indibiduoak = elekzioaLehena(indibiduoak)


for generazio in range(n_generazioak):
    print(str(generazio) + ". Generazioa")

    irudiakEraldatu(indibiduoak)
    indibiduoak = irudiakEbaluatu(indibiduoak, hizkuntza)   

    #orain arteko onena hobetu badu
    for i in range(len(indibiduoak)):
    	if(indibiduoak[i].ebaluazioa>onenaIndibi.ebaluazioa):
    		onenaIndibi = indibiduo(indibiduoak[i].eraldaketak, indibiduoak[i].ebaluazioa)


    print("****************************************")
    print("****************************************")
    print(onenaIndibi.eraldaketak)
    print(onenaIndibi.ebaluazioa)
    print("****************************************")
    for ind in indibiduoak:
    	print(str(ind.ebaluazioa)+"  "+str(ind.eraldaketak))
    print("****************************************")
    print("****************************************")
    sleep(2)

    gurasoak = elekzioa(indibiduoak) 
    berriak = gurutzaketak(gurasoak)
    #berriak = mutazioa(berriak)
    #indibiduoetatik 9/10 berriak sortu dira
    #1/10 berriz, lehengo populazioko onenak izango dira
    indibiduoak = populazioBerria(indibiduoak, berriak)


#emaitza gorde
outfile = open(argazkia+"emaitzak", 'a')
outfile.write(str(ind.ebaluazioa))
outfile.write(str(ind.eraldaketak))

#direktorioa ezabatu
komandoa = "rm -rf temp"
args = shlex.split(komandoa)
subprocess.call(args)

elapsed_time = time() - start_time
print("Bilaketa Egiten Pasatako Denbora: %0.10f segundu." % elapsed_time)

exit(0)










 
