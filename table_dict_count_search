import os, sys, csv

filename = sys.argv[1]

#counting lines of file#
def count_lines(filename):
    num_lines=0
    with open(filename) as file:
        for line in file:
            lines = line.split()

            num_lines += 1
        print ('this file contains {} lines'.format(num_lines))

#creating a dictionary#		
file = csv.DictReader(open('SampleAnnot.csv'))

#for row in file:   #look at dictionary contents
#	print row

#searching a column#
def count_mnix(file, value):
    count = 0
    struct_acro = []
    for row in file:
        mni_x = int(row["mni_x"])
        if mni_x <= value:
            count = count + 1
            struct_acro.append(row["structure_acronym"])
    print ('there are {} entries with mni_x <= {}'.format(count,value))
    print ('their structure acronyms are {}'.format(struct_acro))

#unique structure acronyms#
def unique_structacro(file):
    output = set()
    for row in file:
        output.add(row["structure_acronym"])
    print ('list of all unique structure acronyms:{}'.format(output))

		
## MAIN ## 

filename = sys.argv[1]
file = csv.DictReader(open(filename))
count_lines(filename)
count_mnix(file, -35)
file = csv.DictReader(open(filename))

unique_structacro(file)
