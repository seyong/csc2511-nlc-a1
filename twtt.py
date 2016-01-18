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

def main(args):
	if(len(args) < 4):
		print "Wrong number of arguments"
		print "Usage: python twtt.py <input_filename> <group_number> <output_filename>"
		sys.exit()

	input_filename = args[1]
	gr_number = args[2]
	output_filename = args[3]

	print 'Number of arguments:', len(args), 'arguments.'
	print 'Input csv filename: ', input_filename, len(input_filename)
	print 'Group Number: ', gr_number
	print 'Output filename: ', output_filename

####
# Read CSV file
####
	with open(input_filename,'r') as f:
		reader = csv.reader(f)
		try:
			for row in reader:
				tweet = Tweet(row)
				#print row
				tweet.desc()
		except csv.Error as e:
			sys.exit(" file %s, line %d: %s" % (input_filename, reader.line_num,e))

####
# Pre-processing
####

class Tweet(object):
	#
	#def __init__(self,polar,tid,date,query,user,text):
	def __init__(self,data):
		self.polar = data[0]
		self.tid = data[1]
		self.date = data[2]
		self.query = data[3]
		self.user = data[4]
		self.text = data[5]
	
	def preprocess(self):
		# remove all html tags and attributes
		self.text
		# replace html characer codes with ascii 
		# all urls are removed
		# remove The first charcter in Twt user names and hashtages
		# Each sentence within a tweet is on its own line
		# Ellipsis (i.e. '...') and other kinds of multiple punctuations are not split
		# Each token, including punctuation and clitics is separated by spaces
		# Each token is tagged with its part-of-speech
		# Before each tweet is demarcation '<A=#>', which occurs on its own line, where # is the numeric class of the tweet (0,2, or 4)

	def desc(self):
		print "Polar: %s" % str(self.polar)
		print "Tweet id: %s" % str(self.tid)
		print "Date: %s" % str(self.date)
		print "Query: %s" % str(self.query)
		print "User: %s" % str(self.user)
		print "Text: %s" % str(self.text)


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
	main(sys.argv)
