
#To run this code: python FilterPSIBlast.py -i <insert file path> -o ./ 

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au


import csv
import sys
import os.path


def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

input_file = sys.argv[sys.argv.index('-i')+1]
output_file = sys.argv[sys.argv.index('-o')+1]

count1 = 0
count2 = 0

outputliste = []

for line in import_file(input_file):
	for il in line:
		count1 += 1
		spline = il.split('\t')
		check = spline[2]
		if float(check) > 50.00:
			count2 += 1
			outputliste.append(spline[0] + '\t' + spline[1] + '\t' + spline[2])
		else:
			pass

print("Original count of PSI-Blast sim scores:")
print(count1)

print("Filtered count of only > 50% similarity:")
print(count2)

output = open(os.path.join(output_file, input_file + "PSIBlastfiltered.txt"), "w")

for line in outputliste:
    output.write(line + '\n')
    









