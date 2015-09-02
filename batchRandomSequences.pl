#!/usr/bin/perl -w
#usage: perl batchRandomSequences.pl DIRECTORYNAME N
#where DIRECTORYNAME is the directory of fasta sequences, and N is the number of sequences that should be chosen randomly from each sequence.
#The results are outputted to a new directory called DIRECTORYNAMERANDOMIZEDOUTPUT.
#Selects N random sequences from all fasta files in directory B
use List::Util qw(first max maxstr min minstr reduce shuffle sum);

#Directory to target
$dir = $ARGV[0];

#Number of sequences to get
$seqnum = $ARGV[1];

#opens the directory
opendir(DIR, $dir) or die $!;

my @seqFiles;

#Loops through all files in the directory
while (my $file = readdir(DIR)) {
 	# Use a regular expression to ignore files beginning with a period
    next if ($file =~ m/^\./);

    #Check for FASTA or fas file format
    next if ($file !~ /.fasta/ && $file !~ /.fas/);
    #Add filename to array
    push @seqFiles, $file;
}

#Make output directory
system("mkdir -p " . $dir . "RandomizedOutput");


foreach my $seqf (@seqFiles){
	#open the sequence file
	open(my $in,  "<",  $dir . "/" . $seqf) or die "Can't find that sequence file!";
	@lines = <$in>;
	close($in);

	#Convert the sequence files lines to string
	$seqFile = "";
	foreach (@lines){
		$seqFile .= $_;
	}

	#Split into individual sequences
	@seqs = split(/>/, $seqFile);

	#Add back in the > symbol to each sequence
	foreach(@seqs){
		$_ = ">$_"
	}

	#Shuffle the sequences randomly
	@seqs = shuffle @seqs;

	#Choose the first N sequences
	@seqs = splice(@seqs, 0, $seqnum);

	#Get filename without extension
	#Print them to output.fasta
	open (MYFILE, ">>", $dir . "RandomizedOutput/" . $seqf);
	print MYFILE @seqs;
	close (MYFILE); 

}


closedir(DIR);
