#To run this code: python GetBRITEinfo.py -i <KO annotated input list> -o ./

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au

import csv
import sys
import os.path
import urllib.request as ur
from bs4 import BeautifulSoup

myko = sys.argv[sys.argv.index('-i')+1]
output_file = sys.argv[sys.argv.index('-o')+1]

def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

koliste = []

for line in import_file(myko):
	for il in line:
		koliste.append(il)

output_liste = []

total = float(len(koliste))
count = 0

for x in koliste:
	count += 1
	perc = (count/total)*100
	print("Percent complete:" + '\t' + str(perc))
	if x[0] is not 'F':
		pass
	else:
		sp = x.split('\t')
		#print(len(sp))
		if len(sp) < 2:
			pass
		else:
			fc = sp[0]
			query = sp[1]
			if query is '':
				pass
			elif query[0] is 'K':
				url = "http://rest.kegg.jp/get/" + query
				html = ur.urlopen(url).read()
				soup = BeautifulSoup(html, features="html.parser")
				text = soup.get_text()
				lines = (line.strip() for line in text.splitlines())
				chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
				text = '\n'.join(chunk for chunk in chunks if chunk)
				tmp = text.split('\n')
				brite = tmp.index('BRITE')
				information = tmp[brite+2:brite+5]
				output_liste.append(fc + '\t' + query + '\t' + information[0] + '\t' + information[1] + '\t' + information[2])
			else:
				pass

output = open(os.path.join(output_file, myko + "_BRITEinfo.txt"), "w")

for line in output_liste:
    output.write(line + '\n')

