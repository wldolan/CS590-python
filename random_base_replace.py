import os
import sys
from random import randint


filename =sys.argv[1]
r = sys.argv[2]

def readfile(filename):
	with open(filename) as file:
		seq=[(part[2].replace('\n',''))	
		for part in
			[entry.partition('\n')
		for entry in file.read().split('>')[1:]]]
	seq=seq[0]
	return (seq)

def replace_n_base_randomly_using_expression(base_seq, n):
    for i in range (n):
        position = randint(0, len(base_seq) - 1)
        base_seq = (base_seq[0:position] +
                 'TCAG'.replace(base_seq[position], '')[randint(0,2)] +
                 base_seq[position+1:])
    print (base_seq)
			

## MAIN ##
filename =sys.argv[1]
n = int(sys.argv[2])
base_seq = readfile(filename)
print (base_seq)
replace_n_base_randomly_using_expression(base_seq, n)


