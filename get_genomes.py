import urllib2
import os
with open('./.listing') as f:
	for line in f:
		name = line.split()[8].strip()
		url = "ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/" + name + "/latest_assembly_versions"
		try:
			response = urllib2.urlopen(url, timeout=5)
			newurl = url + "/" + response.read().split()[8]
			print newurl
			os.system("wget -r " + newurl + "/* -A '*.faa.gz' -O " + name + ".faa.gz")
		except:
			print "ERROR"
