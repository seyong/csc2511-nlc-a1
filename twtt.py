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
# Add tagger library path, but doesn't work well
sys.path.append('./tagger')
import csv
import NLPlib
from twitter import Tweet
import re

# command line arguments passed through 'sys.argv' as a list
# check the number of argument

def main(args):
	# For class 0, use lines [GID x 5500 ... (GID+1) x 5500 -1 ]
	# For class 4, use liens 800,000 + [GID x 5500 ... (GID+1) x 5500 -1]
	# my group_id = 100
	LINES_BTW_CLASS = 800000
	c0start = -1
	c0end = -1
	c4start = -1
	c4end = -1
	is_group_exist = False
	#print len(args)
	## arguments checking
	if(len(args) == 4):
		input_filename = args[1]
		output_filename = args[3]
		try:
			group_id = int(args[2])
			c0start = (group_id * 5500)
			c0end = ((group_id+1) * 5500)-1
			c4start = LINES_BTW_CLASS + c0start
			c4end = LINES_BTW_CLASS + c0end
			is_group_exist = True
		except ValueError:
			print "Parameter (%s) is not a numeric" % args[2]
	elif(len(args) == 3):
		# variables must be a stirngs. input and output
		input_filename = args[1]
		output_filename = args[2]
		group_id = -1
	else:
		print "Wrong number of arguments"
		print "Usage: python twtt.py <input_filename> <group_number> <output_filename>"
		sys.exit()


	print 'Number of arguments:', len(args), 'arguments.'
	print 'Input csv filename: ', input_filename, len(input_filename)
	if(group_id != -1):
		print 'Group ID: ', group_id
	print 'Output filename: ', output_filename

####
# Read CSV file and Write the preprocessing results
####
	tagger = NLPlib.NLPlib() # init tagger
	wfp = open(output_filename,"w") # file pointer for writing result into outputfile
	count = 0
	with open(input_filename,'r+') as f:
		reader = csv.reader(f)
		if(group_id != -1): #group id is provided
			try:
				for i,row in enumerate(reader):
					if(i >= c0start and i<=c0end):
						count = count +1
						tweet = Tweet(row)
						tweet.do_preprocess()
						tweet.tagging(tagger) 
						result =  tweet.printable_tweet()
						#print result
						wfp.write(result+"\n")
					elif(i >= c4start and i<=c4end):
						count = count + 1
						tweet = Tweet(row)
						tweet.do_preprocess()
						tweet.tagging(tagger) 
						result =  tweet.printable_tweet()
						#print result
						wfp.write(result+"\n")


			except csv.Error as e:
				sys.exit(" file %s, line %d: %s" % (input_filename, reader.line_num,e))
		else: # group _id is not provided, use all data
			try:
				for i,row in enumerate(reader):
					tweet = Tweet(row)
					tweet.do_preprocess()
					tweet.tagging(tagger) 
					result =  tweet.printable_tweet()
					#print result
					wfp.write(result+"\n")
			except csv.Error as e:
				sys.exit(" file %s, line %d: %s" % (input_filename, reader.line_num,e))
	print "Count is %s" % count	
	wfp.close()


if __name__ == '__main__':
	main(sys.argv)
