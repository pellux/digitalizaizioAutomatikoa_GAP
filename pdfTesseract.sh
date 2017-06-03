#!/bin/sh

#OHARRA => Direktorioan ezin du beste .tif fitxategirik egon

if [ $# -lt 2 ]; then
	echo "Bi argumentu behar ditu: [sarrera.pdf][irteera.tiff]  (luzapenak ez idatzi argumentuetan)"
	exit 1
fi

echo "---------------------------"
echo "----pdf-a prozesatzen------"
echo "---------------------------\n"

#pdf-a irudieta banatu
gs -dNOPAUSE -dBATCH -sDEVICE=tiffg4 -sOutputFile=scan_%d.tif "$1" > /dev/null
#irudiak bateratu
convert -quiet -level 0%,77% -normalize -monochrome *.tif "$2.tiff" > /dev/null
#irudiak ezabatu
rm *.tif
echo "** $2.tiff fitxategia sortu da **\n"
exit 0

