from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
import sys
handle = open(sys.argv[1], 'rU')
records = list(SeqIO.parse(handle, "fasta"))
for record in records:
	prot = ProteinAnalysis(str(record.seq))
	print prot.isoelectric_point()
