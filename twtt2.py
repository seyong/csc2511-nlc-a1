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
# Add tagger library path
sys.path.append('./tagger')
import csv
import NLPlib

# command line arguments passed through 'sys.argv' as a list
# check the number of arguments

def main():
	if(len(sys.argv) < 4):
		print "Wrong number of arguments"
		print "Usage: python twtt.py <input_filename> <group_number> <output_filename>"
		sys.exit()

	input_filename = sys.argv[1]
	gr_number = sys.argv[2]
	output_filename = sys.argv[3]

	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Input csv filename: ', input_filename, len(input_filename)
	print 'Group Number: ', gr_number
	print 'Output filename: ', output_filename

class Tweet(object):
	#
	def __init__(self,polar,tid,date,query,user,text):
		self.polar = polar
		self.tid = tid
		self.date = date
		self.query = query
		self.user = user
		self.text = text

	def desc(self):
		print "Polar: " % self.polar
		print "Tweet id: " % self.tid
		print "Date: " % self.date
		print "Query: " % self.query
		print "User: " % self.user
		print "Text: " % self.text


####
# Tokenizing
####


####
# Tagging
####

#Tagger example
# tagger = NLPlib.NLPlib()
# sent = ['tag','me']
# tags = tagger.tag(sent)

if __name__ == '__main__':
	main()
