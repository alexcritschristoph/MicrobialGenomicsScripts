with open('./results.blast') as f:
	nano = []
	natro = []
	cyano = []
	contigs = {}
	contig_genes = []
	for line in f:
		gene = line.split()[0]
		contig = int(gene.split("_")[0])
		taxa = line.split("[")[1].split()[0]
		if contig not in contigs.keys():
			contigs[contig] = []
		if gene not in contig_genes:
			contigs[contig].append(taxa)
			contig_genes.append(gene)


all_genes = {}
with open('./all_genes') as f:
	for line in f:
		c = int(line.split(">")[1].split("_")[0])
		g = line.split("_")[1]
		all_genes[c] = g


seqs = {}
from Bio import SeqIO
handle = open("halite_bins.009.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
    seqs[int(record.id)] = record.seq
handle.close()

from collections import Counter

for contig in sorted(contigs.keys()):
	c = Counter(contigs[contig])
	
	## Conditions for accepting a contig.
	## Here it's a greater number of blastp products on that contig to the specified genome
	## compared to the others, and at least 25% of all products on that contig match to that genome.
	if c['Halothece'] > (c['Natronomonas'] + c['Candidatus']):
		if c['Halothece'] > 0.25 * int(all_genes[contig]):
			print ">" + str(contig)
			print seqs[contig]
