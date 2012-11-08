#!/usr/bin/python

def query(ORF):
	from httpclient import HttpClient
	
	browser = HttpClient()
	browser.GET('http://yeastract.com/view.php?existing=locus&orfname=YPL089c')
	
	return str(browser.Page)
