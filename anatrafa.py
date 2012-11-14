#!/usr/bin/python

def analyze(TF):
	import yeastgenome

	print "So, let's try to find out, what the transcription factor "+TF+" is for ..."

	# query YeastGenome to determine, if there is such a TF

	print "First, asking SGD, whether "+TF+" is a yeast protein."
	if not yeastgenome.ORF_exists(TF):
		print "No! Seems there is no such ORF in yeast."
		print "Please redefine your search. You may want to consult http://yeastgenome.org/ to verify your ORF."
		return

	# query Yeastract to retrieve TF's target genes

	# query YeastGenome to retrieve GO terms and protein descriptions

	# calculate frequency of GO terms

	# print results

if __name__ == "__main__":
	from sys import argv
	analyze(argv[1])
