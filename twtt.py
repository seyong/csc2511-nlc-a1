#!/usr/bin/python

################
#
# Pre-processing, tokenizing, and tagging [25 marks]
#		Created by Seyong Ha, 2016 Jan. 13
#		Python version 2.7
#  
#		twtt.py program takes three args. the input .csv filename, ur group number, and the output filename. 
#
################

import sys
import csv

# command line arguments passed through 'sys.argv' as a list
input_filename = sys.argv[1]
gr_number = sys.argv[2]
output_filename = sys.argv[3]

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Input csv filename: ', input_filename, len(input_filename)
print 'Group Number: ', gr_number
print 'Output filename: ', output_filename

####
# Read CSV file
####
with open(input_filename, 'rb') as f:
	reader = csv.reader(f)
	try:
		for row in reader:
			print row
	except csv.Error as e:
		sys.exit(" file %s, line %d: %s" % (input_filename, reader.line_num,e))

####
# Pre-processing
####


####
# Tokenizing
####


####
# Tagging
####


