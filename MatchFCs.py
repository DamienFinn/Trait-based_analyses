
#To run this code: python MatchFCs.py -g <genome long format file> -a <annotated FCs file> -o ./

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au


import csv
import sys
import os.path
import re

def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

genome_file = sys.argv[sys.argv.index('-g')+1]
annotated_file = sys.argv[sys.argv.index('-a')+1]
output_file = sys.argv[sys.argv.index('-o')+1]

annotated_liste = []

#Read in the annotated FCs file 

for line in import_file(annotated_file):
	for il in line:
		annotated_liste.append(il)

print("Read in the list of annotations")

#Now begin matching Brite to FCs present in genomes

output_liste = []

output_liste.append("HighRank" + '\t' +	"LowRank" + '\t' +	"Genome" + '\t' +	"variable" + '\t' +	"value" + '\t' + "Brite2" + '\t' + "Brite3")	

nlen = len(annotated_liste)

curFC = 0

for line in import_file(genome_file):
	for il in line:
		spline = il.split('\t')
		X = spline[3]
		Xa = re.sub('"', '', X) 
		counter = 0
		curFC += 1
		print("Completed:" + '\t' + str(curFC) + '\t' + "clusters.")
		for y in annotated_liste:
			counter += 1
			spline2 = y.split('\t')
			Y = spline2[0]
			Z = spline2[3]
			W = spline2[4]
			if Xa == Y:
				output_liste.append(il + '\t' + Z + '\t' + W)
				break
			else: 
				if counter == nlen:
					output_liste.append(il + '\t' + "Uncharacterised" + '\t' + "Uncharacterised")
			
				 
output = open(os.path.join(output_file, genome_file + "matchedFCs.txt"), "w")

for y in output_liste:
	output.write(y + '\n')















