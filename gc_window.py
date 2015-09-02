from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from random import randint
from Bio.SeqUtils import GC
import sys
#There should be one and only one record, the entire genome:
print "reading"
mito_record = SeqIO.read(open(sys.argv[1]), "fasta")
 
gcs = []

#k is the window size
k = 10000
j = 0
print "Read"
for i in range(0, len(seq_record.seq)) :
	if j <= len(seq_record.seq):
		start=j
		#
		end=j+k
		window_frag=seq_record.seq[start:end]
		print str(round(GC(window_frag),2)) + ",",
		j += k
	else:
		break

#How to visualize results in R with ggplot2: 
#m + geom_density() + geom_vline(xintercept=41.5, col='red') + xlim(40,50) + xlab("GC Content (%)") + ylab("Density") + theme_minimal()
