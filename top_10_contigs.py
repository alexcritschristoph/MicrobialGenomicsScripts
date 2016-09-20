#Usage: python filter_contigs.py filename
from Bio import SeqIO
import sys
import operator

handle = open(sys.argv[1], "rU")
l = SeqIO.parse(handle, "fasta")
counter = 0
contig_lengths = {}
contigs = {}
for s in l:
    if len(str(s.seq)) > 5000:
		     contigs[s.id] = s.seq
		     contig_lengths[s.id] = len(str(s.seq))

sorted_x = sorted(x.items(), key=operator.itemgetter(0))
sorted_x.reverse()

for i in range(0,10):
     print str(sorted_x[i][0]) + ":" + str(sorted_x[i][1])
