#Translates DNA sequences in all 6 reading frames, ignoring start / stop codons.

from Bio import SeqIO
from Bio.Seq import Seq
import sys

input_handle = open(sys.argv[1], "rU")
for record in SeqIO.parse(input_handle, "fasta") :
	#Frame 1
	original = record.seq
	print ">" + str(record.id) + "_1"
	print str(record.seq.translate()).replace("*","")
	#Frame 2
	print ">" + str(record.id) + "_2"
	record.seq = Seq(str(record.seq)[1:])
	print str(record.seq.translate()).replace("*","")
	#Frame 3
	print ">" + str(record.id) + "_3"
	record.seq = Seq(str(record.seq)[1:])
	print str(record.seq.translate()).replace("*","")

	record.seq = original.reverse_complement()

	#Frame -1
	print ">" + str(record.id) + "_-1"
	print str(record.seq.translate()).replace("*","")
	#Frame -2
	record.seq = Seq(str(record.seq)[1:])
	print ">" + str(record.id) + "_-2"
	print str(record.seq.translate()).replace("*","")
	#Frame -3
	record.seq = Seq(str(record.seq)[1:])
	print ">" + str(record.id) + "_-3"
	print str(record.seq.translate()).replace("*","")
