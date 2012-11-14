#!/usr/bin/python

#
# Saccharomyces Genome Database (SGD)
# http://yeastmine.yeastgenome.org/yeastmine/api.do?subtab=python
#
# YeastMine example script
#

from intermine.webservice import Service

service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

# List all GO annotations for a specified gene. Searches for the
# primaryIdentifier (SGDID), secondaryIdentifier (Systematic Name), symbol
# (Standard Gene Name) and wild card queries (such as *YAL*) are supported. 
# Manually curated, high-throughput, and computational GO annotations are
# included. Genes include Uncharacterized and Verified ORFs, pseudogenes,
# transposable element genes, RNAs, and genes Not in Systematic Sequence of
# S228C.

template = service.get_template('Gene_GO')

# You can edit the constraint values below
# A    Gene    Show GO annotations for gene:

rows = template.rows(
				A = {"op": "LOOKUP", "value": "YAL018C", "extra_value": "S. cerevisiae"}
				)
for row in rows:
	print row
