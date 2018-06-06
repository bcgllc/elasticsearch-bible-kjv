###
# Import CSV and Import into Elasticsearch
# Anthony Crawford
# December 2014
# Provided Free and Open Source
# Comes with NO warranty whatsoever
###

import os
import sys
import errno
#import datetime, time, calendar
import json
import hashlib

# Third Party Packages
from elasticsearch import Elasticsearch

if len(sys.argv) == 0:
	print 'Missing parameter ui:port for elasticsearch'
	exit

# Set ES Parameters
index_name = 'bible'
doc_type_name = 'kjv'
es = Elasticsearch(sys.argv[0])

# Import CSV
import csv
import sys

files = []
for filename in os.listdir('csv'):
    if filename.endswith(".csv"):
        files.append(filename)

print
print "Importing CSV files into Elasticsearch Index: \'bible\'"
print

for file in files:
	print file
	f = open('csv/'+file, 'rb')
	try:
		reader = csv.reader(f)
		for row in reader:
			bible_testament = row[0]
			bible_book = row[1]
			bible_chapter = row[2]
			bible_verse = row[3]
			bible_text = row[5]
			hash_row = bible_testament + bible_book + bible_chapter + bible_verse + bible_text
			hashed = hashlib.sha256(''.join(hash_row)).hexdigest()

			json_es = {
				'testament':bible_testament,
				'book':bible_book,
				'chapter':bible_chapter,
				'verse':bible_verse,
				'text':bible_text,
				'hash':hashed,
			}

			res = es.index(index=index_name, doc_type=doc_type_name, body=json_es)
			if res['result'] == False:
				print
				print "!!!!!!!!!!!!!!!!!!!!!!!"
				print "!!! ES ENTRY FAILED !!!"
				print "!!!!!!!!!!!!!!!!!!!!!!!"
				print
				f.close()
				sys.exit()

	finally:
		f.close()

es.indices.refresh(index=index_name)

print
print "Refeshing Indexes..."
print
print "Import Completed."
print

sys.exit()
