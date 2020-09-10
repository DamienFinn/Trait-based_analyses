
#To run this code: python IdentifyTraits.py -m <MCL tab file> -g <cat genomes file> -o ./

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au


import csv
import sys
import os.path
import numpy

def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line


MCL_file = sys.argv[sys.argv.index('-m')+1]
genomes_file = sys.argv[sys.argv.index('-g')+1]
output_file = sys.argv[sys.argv.index('-o')+1]

MCLliste = []

#Read in the first column of the MCL file and call them as FCs
count = 0

for line in import_file(MCL_file):
	for il in line:
		count += 1
		sp = il.split('\t')
		MCLliste.append("FC." + str(count) + '\t' + sp[0])

#Find the corresponding AA sequence

with open(genomes_file, 'r') as file:
    genomedata = file.read().replace('\n', '')

proteinlist = genomedata.split('>')

output_liste = []

total = float(len(MCLliste))
count = 0

for y in MCLliste:
	count += 1
	sp3 = y.split('\t')
	reference = sp3[1]
	for x in proteinlist:
		sp = x.split(' ')
		query = sp[0]
		sp2 = x.split(']')
		sequence = sp2[-1]
		if reference == query:
			output_liste.append('>' + y + '\n' + sequence)
			perc = (count/total)*100
			print("Percent complete:" + '\t' + str(perc))

tmp = numpy.array_split(numpy.array(output_liste),24)

count = 0

for chunk in tmp:
	count += 1
	output = open(os.path.join(output_file, "File_" + str(count) + "_FCs_identified_AA_seqs.fa"), "w")
	for line in chunk:
		output.write(line + '\n')	

    
					
			














