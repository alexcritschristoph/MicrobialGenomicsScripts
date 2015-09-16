# MicrobialGenomicsScripts
A selection of (very) short scripts for analyzing microbial genomes. I have created this repository as a place to store and share any useful scripts for analyzing microbial genomes.

###Usage:

*gc_window.py*

Calculates GC% for a window size across a genome. Default is 10 kbp, and can be changed in the code if needed.

`python gc_window.py genome.fna`

*translate_all_frames.py*

Translates a FASTA file of DNA sequences in all 6 reading frames, ignoring start / stops. 

`python translate_all_frames.py sequences.fna`

*isoelectric.py*

Calculates the isoelectric points for all proteins in a proteome and outputs in a list which can be easily imported into R . Useful for showing the isoelectric point distribution of a new halophilic proteome.

`python isoelectric.py proteins.faa`

*simulate_assembly.py*

Naively simulates a metagenomic assembly by taking in a directory of genomes and generating randomly sized and spaced contigs from those genomes.

`python simulate_assembly.py ./directory_with_fasta_genomes/`

*batchRandomSequences.pl*

Generates random subsets of N reads for a batch of fasta files in a directory. Useful if you want to quickly get a random sample of reads for a large number of samples.

`perl batchRandomSequences.pl DIRECTORYNAME N`

*filter_contigs.py*

Filters a contig file to a minimum contig length.

`python filter_contigs.py contigs.fna min_contig_length`

*random_forest.py*

Basic demonstration of how to import training data and create a random forest classifier using sklearn.

*concat_alignments.py*

concatenating multiple gene / protein alignments.

`python concat_alignments.py ./directory_with_alignments/*.fa`

*get_genomes.py*

Automatically / recursively downloads genomes from NCBI's FTP.

*filter_contigs_by_blastp.py*

A script for filtering contigs by comparing them to specific known reference proteomes. The input is the blast results of the predicted prodigal products of the contigs to a database of the known reference proteomes and the predicted protein fasta file itself.
