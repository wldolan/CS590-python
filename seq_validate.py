import os, sys

command =sys.argv[1]
filename1 = sys.argv[2]
filename2 = sys.argv[3]

#validate function
def validate_base_sequence(seq):
   return len(seq) == (seq.count('T') +
                       seq.count('C') +
                       seq.count('A') +
                       seq.count('G') +
					   seq.count('-'))
                       
					   
#SAMESIZE function				   
def samesize(filename1,filename2):
    with open(filename1) as file:
       seq1=[(part[2].replace('\n',''))
            	for part in
        		[entry.partition('\n')
				for entry in file.read().split('>')[1:]]]
    seq1=seq1[0]
    
    with open(filename2) as file:
       seq2=[(part[2].replace('\n',''))
               for part in
               [entry.partition('\n')
                for entry in file.read().split('>')[1:]]]
    seq2=seq2[0]
    
    if (len(seq1) == len(seq2)): 
        print ('sequences are of equal length')
    else:
        print ('sequences are not of equal length {}, {}'.format(len(seq1), len(seq2)))
	
#read and validate
def validate(filename1, filename2):
    with open(filename1) as file:
       seq1=[(part[2].replace('\n',''))
               for part in
               [entry.partition('\n')
                for entry in file.read().split('>')[1:]]]
    seq1=seq1[0]
    if validate_base_sequence(seq1) is False:
        print ('The first file contains invalid characters')
    
    with open(filename2) as file:
       seq2=[(part[2].replace('\n',''))
               for part in
               [entry.partition('\n')
                for entry in file.read().split('>')[1:]]]
    seq2=seq2[0]
    if validate_base_sequence(seq2) is False:
        print ('The second file contains invalid characters')

    if validate_base_sequence(seq1) is True and validate_base_sequence(seq2) is True:
        print ('Both sequences are valid')
		
if command == 'validate':
    result = validate(filename1, filename2)
    
elif command == 'samesize':
    result = samesize (filename1, filename2)
    
