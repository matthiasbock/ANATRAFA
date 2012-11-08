#!/usr/bin/python

#
# Python library to access the
# Saccharomyces Transcription Factor Database (Yeastract)
# http://yeastract.org/
#

def query_ORF(ORF):
	from httpclient import HttpClient
	browser = HttpClient()
	browser.GET('http://yeastract.com/view.php?existing=locus&orfname=YPL089c')
	return str(browser.Page)

def get_promotor(ORF):
	# http://yeastract.com/download.php?type=promoter&id=YPL089c
	return

def get_gene_sequence(ORF):
	# http://yeastract.com/download.php?type=gene&id=YPL089c
	return

def find_documented_regulators(ORF):
	# view-source:http://yeastract.com/findregulators.php?type=doc&genes=YPL089c
	return

def find_potential_regulators(ORF):
	# http://yeastract.com/findregulators.php?type=pot&genes=YPL089c
	return

def find_documented_regulated_genes(TF):
	# http://yeastract.com/findregulated.php?type=doc&tfs=Yap1p
	return

def find_potential_regulated_genes(TF):
	# http://yeastract.com/findregulated.php?type=pot&tfs=Yap1p
	return
