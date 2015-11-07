#Predicts codon frequencies for a FASTA file with one or more sequences (e.g. contigs)

from Bio import SeqIO
import sys

def predict(seqs):

	CodonsDict = {'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0, 
	'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0, 
	'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0, 
	'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0, 
	'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0, 
	'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0, 
	'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0, 
	'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0, 
	'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0, 
	'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0, 
	'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0, 
	'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0, 
	'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0} 

	# this dictionary shows which codons encode the same AA 
	SynonymousCodons = { 
	'CYS': ['TGT', 'TGC'], 
	'ASP': ['GAT', 'GAC'], 
	'SER': ['TCT', 'TCG', 'TCA', 'TCC', 'AGC', 'AGT'], 
	'GLN': ['CAA', 'CAG'], 
	'MET': ['ATG'], 
	'ASN': ['AAC', 'AAT'], 
	'PRO': ['CCT', 'CCG', 'CCA', 'CCC'], 
	'LYS': ['AAG', 'AAA'], 
	'STOP': ['TAG', 'TGA', 'TAA'], 
	'THR': ['ACC', 'ACA', 'ACG', 'ACT'], 
	'PHE': ['TTT', 'TTC'], 
	'ALA': ['GCA', 'GCC', 'GCG', 'GCT'], 
	'GLY': ['GGT', 'GGG', 'GGA', 'GGC'], 
	'ILE': ['ATC', 'ATA', 'ATT'], 
	'LEU': ['TTA', 'TTG', 'CTC', 'CTT', 'CTG', 'CTA'], 
	'HIS': ['CAT', 'CAC'], 
	'ARG': ['CGA', 'CGC', 'CGG', 'CGT', 'AGG', 'AGA'], 
	'TRP': ['TGG'], 
	'VAL': ['GTA', 'GTC', 'GTG', 'GTT'], 
	'GLU': ['GAG', 'GAA'], 
	'TYR': ['TAT', 'TAC'] 
	} 

	
	# Count codons
	CodonsNormalized = CodonsDict
	for seq in seqs:
		start = 0
		end = 3
		while end <= len(str(seq.seq)):
			codon = str(seq.seq[start:end])
			if codon in CodonsDict.keys():
				CodonsDict[codon] += 1
			start += 3
			end += 3

	#Normalize by AA
	for aa in SynonymousCodons.keys():
		total = 0
		for codon in SynonymousCodons[aa]:
			total += CodonsDict[codon]
		for codon in SynonymousCodons[aa]:
			CodonsNormalized[codon] = float(CodonsDict[codon]) / float(total)

	print "{",
	i = 0
	for codon in sorted(CodonsNormalized.keys()):
		if i != 0:
			print ", '" + codon + "':" +  str(round(CodonsNormalized[codon],3)),
		else:
			print "'" + codon + "':" +  str(round(CodonsNormalized[codon],3)),
		i += 1
	print "}",
if __name__ == "__main__":
	handle = open(sys.argv[1], "rU")
	records = list(SeqIO.parse(handle, "fasta"))
	handle.close()
	predict(records)
