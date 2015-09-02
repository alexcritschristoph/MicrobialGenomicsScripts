#Usage: python filter_contigs.py filename min_contig_length
from Bio import SeqIO
import sys
handle = open(sys.argv[1], "rU")
l = SeqIO.parse(handle, "fasta")
counter = 0
for s in l:
	if len(s.seq) >= sys.argv[2]:
		print ">" + s.id
		print s.seq
		counter += 1
