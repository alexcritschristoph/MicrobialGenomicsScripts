import pysam
import sys


gene_list = sys.argv[1]
bam = sys.argv[2]

f = open(gene_list)
positions = []
for line in f.readlines():
	positions.append([line.split()[0], int(line.split()[1]), int(line.split()[2].strip())])
f.close()

samfile = pysam.AlignmentFile(bam, "rb")

for pos in positions:
	iter = samfile.fetch(pos[0], pos[1], pos[2])
	i = 0
	for x in iter:
		i += 1

	b = 0 
	b2 = 0
	cov = []
	for pileupcolumn in samfile.pileup(pos[0], pos[1], pos[2], stepper = 'nofilter'):

		if pileupcolumn.reference_pos >= pos[1] and pileupcolumn.reference_pos < pos[2]:
			cov.append(pileupcolumn.nsegments)
			b2 += 1
			if pileupcolumn.nsegments > 0:
				b += 1

	coverage = round(float(sum(cov)) / float(len(cov)),3)
	print(pos[0] + "\t" + str(pos[1]) + "\t" + str(pos[2]) + "\t" + str(i) + "\t" + str(coverage) + "\t" + str(float(b) / (pos[2]-pos[1])))
