#A quick python script for concatenating multiple gene alignments.
#Useful for creating concatenated protein phylogenies.
#Usage: python concat_alignments.py ./directory_with_alignments/*.fa

import glob, os, sys
from Bio import SeqIO

os.chdir(sys.argv[1])
concat = {}

for file in glob.glob("*.fa"):
	input_handle = open(file, "rU")
	for record in SeqIO.parse(input_handle, "fasta") :
	    if record.id in concat.keys():
	    	concat[record.id] += str(record.seq)
	    else:
	    	concat[record.id] = str(record.seq)

for c in concat:
	print ">" + c
	print concat[c]
