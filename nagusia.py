#!/usr/bin/python3

import sys
import shlex, subprocess
import codecs
import io
from PIL import Image
import psutil
import hunspell


def irudiaEraldatu(eraldaketak, argazkia, izena):
 
	komandoa = "mkdir temp"
	args = shlex.split(komandoa)
	subprocess.call(args)

	komandoa = ""

	#null diren eraldaketak kendu
	eralNullKendu = []
	for j in range(len(eraldaketak)):
		eral = eraldaketak[j]
		if eral != "null":
			eralNullKendu.append(eral)

	#print(ind)
	print(eralNullKendu)

	#eraldaketarik ez badu
	if 0 == len(eralNullKendu):
		#komandoa = "kopiatu.sh "+argazkia+" "+str(i)
		komandoa = "cp "+argazkia+" eral"+str(izena)
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
				komandoa2 = "mv thres.png eral"+str(izena)
			#edge bada
			elif eral[2] == 'd':
				num = eral[0]
				komandoa = "convert -edge "+num+" "+argazkia+" eral"+str(izena)
			#null bada
			elif eral[1]=='u':
				komandoa = "cp "+argazkia+" eral"+str(izena)
			#normalize bada
			elif eral[2]=='r':
				komandoa = "convert -normalize "+argazkia+" eral"+str(izena)
			#negate bada
			elif eral[0]=='n':
				komandoa = "convert -negate "+argazkia+" eral"+str(izena)
			#kontarst bada
			elif eral[0]=='c':
				komandoa = "convert -contrast "+argazkia+" eral"+str(izena)
			#gaussian-blur	
			elif eral[0]=='g':
				komandoa = "convert -gaussian-blur 3x3 "+argazkia+" eral"+str(izena)

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
				komandoa2 = "mv thres.png eral"+str(izena)
			#edge bada
			elif eral[2] == 'd':
				num = eral[0]
				komandoa = "convert -edge "+num+" temp/ir"+str(j-1)+" eral"+str(izena)
			#null bada
			elif eral[1]=='u':
				komandoa = "cp temp/ir"+str(j-1)+" eral"+str(izena)
			#normalize bada
			elif eral[2]=='r':
				komandoa = "convert -normalize temp/ir"+str(j-1)+" eral"+str(izena)
			#negate bada
			elif eral[0]=='n':
				komandoa = "convert -negate temp/ir"+str(j-1)+" eral"+str(izena)
			#kontarst bada
			elif eral[0]=='c':
				komandoa = "convert -contrast temp/ir"+str(j-1)+" eral"+str(izena)
			#gaussian-blur bada
			elif eral[0]=='g':
				komandoa = "convert -gaussian-blur 3x3 temp/ir"+str(j-1)+" eral"+str(izena)
		

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
		print("*** "+str(komandoa))
		args = shlex.split(komandoa)
		subprocess.call(args)
		#yosuren indizea bada
		if(komandoa2!=""):
			args = shlex.split(komandoa2)
			subprocess.call(args)

	komandoa = "rm -rf temp"
	args = shlex.split(komandoa)
	subprocess.call(args)


class hitza:
	#objetua sortu
	def __init__(self, num):
		self.num = num
		self.minLeft = 10000000
		self.maxRight = -1
		self.minTop = 10000000
		self.maxBotton = -1
		self.xDim = -1
		self.yDim = -1
		self.xPos = -1
		self.yPos = -1
		self.hitz = ""
		

#teknika probisionala
def lortuIndBoxHitza(hitza, boxHitzak, ind):
	#box-eko hitza eta berezko hitzaren artean antzekotasuna bilatu
	
	#hasierako agorsetzeko
	indLag = ind

	print(str(len(boxHitzak))+"   "+str(ind))

	while(True):
		# gutxienez %50-a berdina izan behar, berdinak direla eateko
		berdinak = 0
		for i in range(len(hitza)):
			for j in range(i,len(boxHitzak[ind].hitz)):
				if hitza[i]==boxHitzak[ind].hitz[j]:
					berdinak += 1
					break

		print("[Konparazioa] "+str(hitza)+" == "+str(boxHitzak[ind].hitz)+" => "+str(berdinak))
		if len(hitza)>len(boxHitzak[ind].hitz):
			luz = len(hitza)
		else:
			luz = len(boxHitzak[ind].hitz)

		if float(berdinak) > float(3*luz/4):
			#hitz hau dela suposatzen da
			indBerria = ind
			return indBerria
		else:
			ind += 1
			if ind > indLag + len(boxHitzak)-3 or ind == len(boxHitzak)-1:
				#ez du aurkitu eta ez da irudia azalduko
				return -1


def tarteaEntrenatu(box):
	#testu bakoitzean hitzen arteko tartea desberdina denez,
	#textua aurreprozesatuz textu horrentzako tarte egokia definitu
	boxak = open(box, 'r')
	aurrekoPos = -1
	batura = 0
	kop = 0

	for box in boxak:

		#box-aren balioak lortu
		letra = box.split(" ")[0]
		leftPos = int(box.split(" ")[1])
		rightPos = int(box.split(" ")[3])
		bottonPos = int(box.split(" ")[4])
		topPos = int(box.split(" ")[2])

		#lehenengo letra bada
		if aurrekoPos == -1:
			aurrekoPos = leftPos

		momentukoTartea = abs(aurrekoPos - leftPos)
		if momentukoTartea < 100:
			batura += momentukoTartea
			kop += 1

		aurrekoPos = rightPos

	tarteBerria = int(float(batura/kop)+2)
	#fitxategia itxi
	boxak.close()
	return tarteBerria



def boxEtaTextBateratu(boxFitxIzena, irudiIzena):
	

	#zuzenduak-en tesseract-ek beste bere zuzentzailea pasatzen dionez,
	#letra kopurua ez da berdina, bakoitzaren hasierako indizea bilatu

	hitzak = [] #box bakoitzaren
	aurrekoPos = int(-1)
	#hasierako hitza sortu
	num = 0
	h = hitza(num)
	#irudiaren dimentsioak lortu
	komandoa = "sh dimLortu.sh "+str(irudiIzena)
	args = shlex.split(komandoa)
	subprocess.call(args)
	#fitxategitik dimentxioa lortu
	dim = open("dim.txt", 'r')
	for line in dim:
		dimY = int(line.split("x")[1].split("\"")[0])

	#hitzen arteko tartea entrenatu
	tartea = tarteaEntrenatu(boxFitxIzena)

	#erabiliko diren fitxategiak kargatu
	#zuzenduak = open("checkme.lst")
	boxak = open(boxFitxIzena, 'r')


	for box in boxak:

		#box-aren balioak lortu
		letra = box.split(" ")[0]
		leftPos = int(box.split(" ")[1])
		rightPos = int(box.split(" ")[3])
		bottonPos = int(box.split(" ")[4])
		topPos = int(box.split(" ")[2])

		if abs(aurrekoPos - leftPos) > tartea:
			print(h.hitz)
			print(abs(aurrekoPos - leftPos))
			#hitz berria da

			h.xDim = int(abs(int(h.minLeft)-int(h.maxRight))) #goiko eta beheko mugen izenak aldatu
			h.yDim = int(abs(int(h.minTop)-int(h.maxBotton)))

			h.xPos = int(h.minLeft)
			h.yPos = int(dimY-h.maxBotton)

			if h.maxBotton != 10000000:
				hitzak.append(h)

			#hitz berria sortu
			num += 1
			h = hitza(num)
			h.hitz = letra
		else:
			h.hitz += letra

		# box-aren balioak lortu
		letra = box.split(" ")[0]
		leftPos = int(box.split(" ")[1])
		rightPos = int(box.split(" ")[3])
		bottonPos = int(box.split(" ")[4])
		topPos = int(box.split(" ")[2])

		#hitza eguneratu
		if h.minLeft > leftPos:
			h.minLeft = leftPos
		if h.maxRight < rightPos:
			h.maxRight = rightPos
		if h.minTop > topPos:
			h.minTop = topPos
		if h.maxBotton < bottonPos:
			h.maxBotton = bottonPos

		aurrekoPos = rightPos

	#fitxategia itxi
	boxak.close()

	#hitzak boxetan itzuli
	return hitzak



def zuzenketaSemiAutomatikoa(textua, box, image, hizkuntza):


	#box-ak markatuta dauden fitxategia
	boxHitzak = boxEtaTextBateratu(box,image)
	boxInd = 0
	textuaOcr = open(textua,"r")#ez kargatu guztiz ondo dagoena, OCR egindakoa baizik
	#zuzendua idazteko
	outfile = open("zuzenduta_str"+str(textua)+".txt", 'w')

	gaizkiHitza = ""
	zuzentzekoAukerak = []
	zuzen = True

	#eus
	if hizkuntza=="eus":
		spellchecker = hunspell.HunSpell('eu_ES.dic','eu_ES.aff')
	#esp
	if hizkuntza=="spa":
		spellchecker = hunspell.HunSpell('/usr/share/hunspell/es_ES.dic','/usr/share/hunspell/es_ES.aff')
	#eng
	if hizkuntza=="eng":
		spellchecker = hunspell.HunSpell('/usr/share/hunspell/en_GB.dic','/usr/share/hunspell/en_GB.aff')

	enc = spellchecker.get_dic_encoding()	


	#hiztegirekin konparatutakoa prozesatu
	for line in textuaOcr:

		zuzentzekoIlara = line
		#hitzetan banatu
		hitzak = line.split(" ")
		#hitz bakoitza zuzendu
		for hitz in hitzak:
			#print(" mmmmmmmmmmmmmmmmmmmmmmmmmmmmm ==> "+str(boxInd))
			hitz = hitz.replace("\n","")
			hitzCod = hitz.replace(".","")
			hitzCod = hitzCod.replace(",","")
			hitzCod = hitzCod.encode('latin-1', 'ignore')

			if spellchecker.spell(hitzCod):
				print(hitz+" => zuzena da")
				zuzen = True
			else:
				print(hitz+" => okerra da")
				suggestions = spellchecker.suggest(hitzCod)
				zuzen = False

			if zuzen == False:

				print("\t 0- [ondo dago]")
				for i in range(len(suggestions)):
					print("\t "+str(i+1)+"- "+str(suggestions[i].decode(enc)))
				print("\t "+str(len(suggestions)+1)+"- [eskuz zuzendu]")

				#boxeko hitza eta zuzentzekoa bat datozen indizea bueltatu
				boxIndLag = boxInd # aurrekoa gordetzeko
				boxInd = lortuIndBoxHitza(hitz, boxHitzak, boxInd)


				if boxInd != -1:

					#irudia ebaki
					#print("::::::::"+str(boxHitzak[boxInd].hitz))
					komandoa = "convert -crop "+str(boxHitzak[boxInd].xDim)+"x"+str(boxHitzak[boxInd].yDim)+"+"+str(boxHitzak[boxInd].xPos)+"+"+str(boxHitzak[boxInd].yPos)+" "+str(textu_osoa)+" abe.tiff"
					args = shlex.split(komandoa)
					subprocess.call(args)
					#irudikatu
					image = Image.open('abe.tiff')
					image.show()


					boxInd = boxIndLag
					#erabiltzaileak nahi duena aukeratu
					while True:
						try:#zenbaki bat sartzen dugula ziurtatu
							aukera = int(input(""))
							if aukera >= 0 and aukera<=len(suggestions)+1:
								break #zenbakia aukeren artean dagoela ziurtatu
							else:
								print("Aukeretan agertzen den zenbaki bat sartu!")

						except ValueError:
							print("Aukeretan agertzen den zenbaki bat sartu!")

					if aukera == 0:
						zuzendutakoHitza = hitz
					elif aukera > 0 and aukera < (len(suggestions)+1):
						zuzendutakoHitza = suggestions[aukera-1].decode(enc)
					elif aukera == len(suggestions)+1:
						zuzendutakoHitza = input("Idatzi hitza zuzenduta => ")


					#irudia pantallatik kendu
					for proc in psutil.process_iter():
						if proc.name() == "display":
							proc.kill()

					#print(str(hitz)+" => "+str(zuzendutakoHitza)+" :::: "+str(zuzentzekoIlara))
					zuzentzekoIlara = zuzentzekoIlara.replace(hitz,zuzendutakoHitza)

		#indizea eguneratu
		boxInd += 1

		#zuzendutako ilara idatzi
		outfile.write(zuzentzekoIlara)

	#azkenekoa ere idatzi behar da			
	outfile.write(zuzentzekoIlara)		




def zuzenketaAutomatikoa(textua, hizkuntza):
	
	#fitxategiak ireki
	textuaOcr = open(textua,"r")#ez kargatu guztiz ondo dagoena, OCR egindakoa baizik
	#zuzendua idazteko
	outfile = open("zuzenduta_str"+str(textua)+".txt", 'w')

	#eus
	if hizkuntza=="eus":
		spellchecker = hunspell.HunSpell('MySpell-3.0/eu_ES.dic','MySpell-3.0/eu_ES.aff')
	#esp
	if hizkuntza=="spa":
		spellchecker = hunspell.HunSpell('/usr/share/hunspell/es_ES.dic','/usr/share/hunspell/es_ES.aff')
	#eng
	if hizkuntza=="eng":
		spellchecker = hunspell.HunSpell('/usr/share/hunspell/en_GB.dic','/usr/share/hunspell/en_GB.aff')

	enc = spellchecker.get_dic_encoding()	

	for line in textuaOcr:

		#hitzetan banatu
		hitzak = line.split(" ")
		#hitz bakoitza zuzendu
		for hitz in hitzak:
			hitz = hitz.replace("\n","")
			hitzCod = hitz.replace(".","")
			hitzCod = hitzCod.replace(",","")
			hitzCod = hitzCod.encode('latin-1', 'ignore')

			if spellchecker.spell(hitzCod):
				print(hitz+" => zuzena da")
			else:
				print(hitz+" => okerra da")
				suggestions = spellchecker.suggest(hitzCod)
				if len(suggestions)>0:
					autocorrected = suggestions[0].decode(enc)
					line = line.replace(hitz,autocorrected)

		#zuzendutako ilara idatzi
		outfile.write(line)	
	#fitzategia itxi
	outfile.close()


def zuzenketaManuala(mySemaitza, textua, lista, box, image):


	#fitxategiak ireki
	zuzenduak = io.open(mySemaitza)#, encoding="ISO-8859-1")

	#box-ak markatuta dauden fitxategia
	boxHitzak = boxEtaTextBateratu(box,image)
	boxInd = 0
	#zein ilaratan gauden jakiteko lista hau erabili behar da
	hitzenLista = open(lista,"r")
	textuaOcr = open(textua,"r")#ez kargatu guztiz ondo dagoena, OCR egindakoa baizik
	#zuzendua idazteko
	outfile = open("zuzenduta_str"+str(textua)+".txt", 'w')

	gaizkiHitza = ""
	zuzentzekoAukerak = []
	zuzen = True

	#lehenengo ilara irakurri
	zuzentzekoIlara = textuaOcr.readline()

	#hiztegirekin konparatutakoa prozesatu
	for line in zuzenduak:
		if "is okay" in line:
			print("+++++++++++++++++++++++++++++++++++++++")
			print(str(line.split("\"")[1].split("\"")[0])+" +++++ Ondo")
			print("+++++++++++++++++++++++++++++++++++++++\n")
			zuzen = True
			#box-eko indizea eguneratu
			boxInd += 1

		if "is incorrect" in line:
			gaizkiHitza = line.split("\"")[1].split("\"")[0]
			print("---------------------------------------")
			print(str(gaizkiHitza)+" ----- Gaizki")
			print("---------------------------------------\n")
			zuzentzekoAukerak = []
			zuzen = False

		if "..." in line:
			aukera = line.split("\"")[1].split("\"")[0]
			zuzentzekoAukerak.append(aukera)

		if "\n" == line:
	
			print("\t 0- [ondo dago]")
			for i in range(len(zuzentzekoAukerak)):
				print("\t "+str(i+1)+"- "+str(zuzentzekoAukerak[i]))
			print("\t "+str(len(zuzentzekoAukerak)+1)+"- [eskuz zuzendu]")

			#boxeko hitza eta zuzentzekoa bat datozen indizea bueltatu
			boxIndLag = boxInd # aurrekoa gordetzeko
			boxInd = lortuIndBoxHitza(gaizkiHitza, boxHitzak, boxInd)

			if boxInd != -1:

				#irudia ebaki
				#print("::::::::"+str(boxHitzak[boxInd].hitz))
				komandoa = "convert -crop "+str(boxHitzak[boxInd].xDim)+"x"+str(boxHitzak[boxInd].yDim)+"+"+str(boxHitzak[boxInd].xPos)+"+"+str(boxHitzak[boxInd].yPos)+" "+str(textu_osoa)+" abe.tiff"
				args = shlex.split(komandoa)
				subprocess.call(args)
				#irudikatu
				image = Image.open('abe.tiff')
				image.show()
			else:
				print("^^^^^^ IRUDIAN EZ DA AURKITU, garrantsitsua bada eskuz begiratu ^^^^^^")
				boxInd = boxIndLag

			#erabiltzaileak nahi duena aukeratu
			while True:
				try:#zenbaki bat sartzen dugula ziurtatu
					aukera = int(input(""))
					if aukera >= 0 and aukera<=len(zuzentzekoAukerak)+1:
						break #zenbakia aukeren artean dagoela ziurtatu
					else:
						print("Aukeretan agertzen den zenbaki bat sartu!")

				except ValueError:
					print("Aukeretan agertzen den zenbaki bat sartu!")

			if aukera == 0:
				zuzendutakoHitza = gaizkiHitza
			elif aukera > 0 and aukera < (len(zuzentzekoAukerak)+1):
				zuzendutakoHitza = zuzentzekoAukerak[aukera-1]
			elif aukera == len(zuzentzekoAukerak)+1:
				zuzendutakoHitza = input("Idatzi hitza zuzenduta => ")


			#irudia pantallatik kendu
			for proc in psutil.process_iter():
				if proc.name() == "display":
					proc.kill()

			#indizea eguneratu
			boxInd += 1

			#hitza irakurri eta ilara jauzia kendu
			momentukoHitza = hitzenLista.readline()
			momentukoHitza = momentukoHitza.replace("\n","")

			if momentukoHitza in zuzentzekoIlara:
				if zuzen == False:
					print(str(momentukoHitza)+" => "+str(zuzendutakoHitza)+" :::: "+str(zuzentzekoIlara))
					zuzentzekoIlara = zuzentzekoIlara.replace(momentukoHitza,zuzendutakoHitza)
			else:
				#zuzendutako ilara idatzi
				outfile.write(zuzentzekoIlara)
				zuzentzekoIlara = textuaOcr.readline()
				#ilera hutsa bada
				while zuzentzekoIlara == "\n":#hau baldintza izan beharrean iterazioak
					outfile.write("\n")
					zuzentzekoIlara = textuaOcr.readline()
				if zuzen == False:
					print(str(momentukoHitza)+" => "+str(zuzendutakoHitza)+" :::: "+str(zuzentzekoIlara))
					#ilara zuzendu
					zuzentzekoIlara = zuzentzekoIlara.replace(momentukoHitza,zuzendutakoHitza)
			#print("      "+str(zuzentzekoIlara))

	#azkenekoa ere idatzi behar da			
	outfile.write(zuzentzekoIlara)			



####################
# programa nagusia #
####################


#argumentu kopurua zuzena al den begiratu
if len(sys.argv)==5:
	#argumentuei izen egokiak ezarri
	textu_osoa = sys.argv[1]
	hizkuntza = sys.argv[2]
	textu_zatia = sys.argv[3]
	textu_zatia_txt = sys.argv[4]

elif len(sys.argv)==3:
	#argumentuei izen egokiak ezarri
	textu_osoa = sys.argv[1]
	hizkuntza = sys.argv[2]
	textu_zatia = ""
	textu_zatia_txt = ""

else:
	print("\n")
	print("Argumentu kopuru okerra: TEXTU_OSOA(.pdf || .tiff || .jpg || .png) HIZKUNTZA [TEXTU_ZATIA] [TEXTU_ZATIA_TXT]")
	print("\n")
	#programa ez da ondo amaitu
	exit(1)


#erabiltzaileak aurreprozesaketa entrenatzea erabaki badu
if textu_zatia != "" and textu_zatia_txt != "":

	#heuristikoa pasa textu onentzat irudiaren aurreprozesaketa egoki bat lortzeko
	komandoa = "python3 algoritmoGenetikoa.py "+str(textu_zatia)+" "+str(textu_zatia_txt)+" "+hizkuntza
	args = shlex.split(komandoa)
	subprocess.call(args)

	#emaitza irakurri
	emaitzak = open(str(textu_zatia)+"emaitzak", 'r')
	for line in emaitzak:
		irakurri = line

	#emaitza interpretatu
	ehunekoa = irakurri.split("[")[0]
	lag = irakurri.split("[")[1].split("]")[0].split(",")
	eraldaketak = []
	for eral in lag:
		eral = eral.replace(" ","")
		eral = eral.replace("\'","")
		eraldaketak.append(eral)

else:#defektuzko aurreprozesaketa
	eraldaketak = []
	eraldaketak.append("null")#hau aldatu daiteke
	eraldaketak.append("null")
	eraldaketak.append("null")
	eraldaketak.append("null")
	eraldaketak.append("null")
	eraldaketak.append("null")
	eraldaketak.append("null")
	eraldaketak.append("null")

#textuak tiff motakoa izan behar du
lag = textu_osoa.split(".")
#pdf-a ahal den begiratu
if lag[len(lag)-1]=="pdf":
	komandoa = "sh pdfTesseract.sh "+str(textu_osoa)+" "+str(textu_osoa)
	args = shlex.split(komandoa)
	subprocess.call(args)
	#pdf-a dtextu_osoaren izena aldatzen da
	textu_osoa = str(textu_osoa)+".tiff"

#textu osoari aplikatu eraldaketak
irudiaEraldatu(eraldaketak, textu_osoa, textu_osoa)

#tesseract aplikatu
komandoa = "tesseract -l "+str(hizkuntza)+" eral"+str(textu_osoa)+" emaitzaMomentu"+str(textu_osoa)
args = shlex.split(komandoa)
subprocess.call(args)


#aukeratu testua zuzentzeko modua
print("EmitzaMomentu"+str(textu_osoa)+" fitxatrgian duzu lortutako emaitza!!")
print("BAINA ORAINDIK GEHIAGO ZUZENDU DAITEKE!!\n")
while True:
	try:
		modua = int(input("[1] Ez zuzendu \n[2] Zuzenketa Automatikoa \n[3] Zuzenketa Semiautomatikoa\n\n"))
		if modua > 0 and modua <5:
			break
	except ValueError:
		print("Aukerak [1-4] tarteko zenbaki osoa izan behar du!\n")

if modua > 1:

	#hiztegian begiratu ea hitzak badauden
	#baldin badago hitza egokitzat emango dugu, bestela zuzentzen saiatuko gara edo erabiltzaileari zuzentzeko esaktu

	if modua == 2:
		print("Zuzenketa Automatikoa")
		zuzenketaAutomatikoa("emaitzaMomentu"+str(textu_osoa)+".txt", hizkuntza)

	if modua == 3:
		#letra bakoitzaren box-ak bilatu
		komandoa = "tesseract -l "+str(hizkuntza)+" eral"+str(textu_osoa)+" "+str(textu_osoa)+"Box batch.nochop makebox"
		args = shlex.split(komandoa)
		subprocess.call(args)
		print("Zuzenketa SemiAutomatikoa")
		zuzenketaSemiAutomatikoa("emaitzaMomentu"+str(textu_osoa)+".txt", str(textu_osoa)+"Box.box", textu_osoa, hizkuntza)

#programa ondo amaitu da
exit(0)










