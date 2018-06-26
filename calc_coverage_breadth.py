import pysam
import sys


gene_list = sys.argv[1]
bam = sys.argv[2]
read_length = sys.argv[3]

f = open(gene_list)
positions = []
for line in f.readlines():
	positions.append([line.split()[0], int(line.split()[1]), int(line.split()[2].strip()), line.split()[3]])
f.close()

samfile = pysam.AlignmentFile(bam, "rb")

for pos in positions:
	iter = samfile.fetch(pos[0], pos[1], pos[2])
	i = 0
	for x in iter:
		i += 1

	b = 0 
	b2 = 0
	for pileupcolumn in samfile.pileup(pos[0], pos[1], pos[2], stepper = 'nofilter'):

		if pileupcolumn.reference_pos >= pos[1] and pileupcolumn.reference_pos < pos[2]:
			b2 += 1
			if pileupcolumn.nsegments > 0:
				b += 1
	print(pos[0] + "\t" + pos[3] + "\t" + str(pos[1]) + "\t" + str(pos[2]) + "\t" + str(i) + "\t" + str(float(i)*int(read_length) / (pos[2]-pos[1])) + "\t" + str(float(b) / (pos[2]-pos[1])))
