
#To run this code: python MCLtoReshape2.py -m <insert file path> -g <insert genomes file> -o ./ 

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au


import csv
import sys
import os.path


def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

input_file = sys.argv[sys.argv.index('-m')+1]
genomes_file = sys.argv[sys.argv.index('-g')+1]
output_file = sys.argv[sys.argv.index('-o')+1]

dict = {}

count = 0

#Create a dictionary from the MCL file, where each line is a separate functional cluster (as a key)
#and all the proteins inside the cluster are values

for line in import_file(input_file):
	for il in line:
		count += 1
		FC = "FC-" + str(count)
		key, value = FC , il
		dict[key] = value

print("Dictionary of functional clusters created.")

#Create a list of every genome and every protein associated with that genome

genomeIDs = []		

for line in import_file(genomes_file):
	for il in line:
		if il[0] is not '>':
			pass
		if il[0] is '>':
			sp1 = il.split(' ')
			query = sp1[0]
			queryb = query[1:]
			start = il.rfind('[')
			stop = il.rfind(']')
			if start < 0:
				pass
			else:
				genome = il[start+1:stop]
				genomeIDs.append(genome + '\t' + queryb)

print("List of genome and protein IDs created.")

#Now begin to sort which genome has which protein, and what functional cluster it belongs to

output_liste = []


print("Sorting functional clusters to each genome ...")

total = float(len(genomeIDs))

count = 0

for x in genomeIDs:
	count += 1
	perc = (count/total)*100
	print("Progress of clusters sorted:" + '\t' + '\t' + str(perc))
	spline = x.split('\t')
	genome = spline[0]
	protein = spline[1]
	for key, value in dict.items():
		spline = value.split('\t')
		for y in spline:
			if y == protein:
				output_liste.append(genome + '\t' + protein + '\t' + key)
			else:
				pass

print("Functional clusters sorted! Writing output.")

output = open(os.path.join(output_file, "MCLtoReshape2input.txt"), "w")

output.write('Genome' + '\t' + 'Protein' + '\t' + 'FC' + '\n')

for line in output_liste:
    output.write(line + '\n')
