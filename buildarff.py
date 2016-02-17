#!/usr/bin/python
#! -*- encoding: utf-8 -*-

##################
# Assignments 1-2
# Gathering feature information
# Created by Seyong Ha
#
# Extract 20 features from the tweet data
# - Counts(17)
#		First person pronouns
#		Second person pronouns
#		Third person pronouns
#		Coordinating conjunctions
#		Past-tense verbs
#		Future-tense verbs
#		Commas
#		Colons and semi-colons
#		Dashes
#		Parentheses
#		Ellipses
#		Common nouns
#		Proper nouns
#		Adverbs
#		wh-words
#		Modern slang acroynms
#		Word all in upper case (at least 2 letters long)
# - Average length of sentences (in tokens)
# - Average length of tokens, excluding punctuation tokens (in characters)
# - Number of sentences
###################

import sys
import re
from tweet_text import TweetText
from feature_extractor import Extractor

def main(args):
	is_num_read_exist = False

	######################
	# Arguments checking
	######################
	if(len(args) ==3):
		input_filename = args[1]
		output_filename = args[2]
		num_read = 9999999
	elif(len(args) == 4):
		input_filename = args[1]
		output_filename = args[2]
		try:
			num_read = int(args[3])
			is_num_read_exist = True
			print "Number of read is %d" % num_read
		except ValueError:
			print "Parameter (%s) is not a numeric" % args[3]
	else:
		print "Wrong number of arguments"
		print "Usage: python buildarff.py <input_filename> <output_filename> [number_of_tweets_per_class]"
		sys.exit()

	arff_fp = open(output_filename,"w")
	init_arff_format(arff_fp)
	sentences = []			
	feature_extractor = Extractor()
	count_list = {0:0,2:0,4:0}
	with open(input_filename,"r") as ifp:
		lines = ifp.readlines()
		# if <A=?> is appear, append liens into sentences, until another <A=?> shows up
		tweet = None
		for l in lines:
			m = re.match("<A=(\\d)>(.*)",l)
			if(m is not None): 
				# found start of tweet
				polar = int(m.group(1))
				# save previous tweet, if exists
				if(tweet is None): #no previous tweet
					tweet = TweetText()
					tweet.set_polar(polar)	
				else: #save previous tweet
					#save previous
					#print tweet.get_polar()
					if(count_list[tweet.get_polar()] >= num_read):
						tweet = TweetText()
						tweet.set_polar(polar)	
						continue
					else:
						count_list[tweet.get_polar()] +=1 
						feature_extractor.load_tweet(tweet)
						arff_fp.write(feature_extractor.get_features_result()+"\n")
						# init new TweetText
						tweet = TweetText()
						tweet.set_polar(polar)	
			else:
				if(re.match(r"^\n$", l) is None):
					if(tweet is not None):
						tweet.add_sentences(l)
				
	arff_fp.close()

def init_arff_format(fp):
	fp.write("@relation twit_classification\n")
	fp.write("\n")
	fp.write("@attribute 1st_person_pro numeric\n")
	fp.write("@attribute 2nd_person_pro numeric\n")
	fp.write("@attribute 3rd_person_pro numeric\n")
	fp.write("@attribute coordinate_conjunctions numeric\n")
	fp.write("@attribute past_tense_verbs numeric\n")
	fp.write("@attribute future_tense_verbs numeric\n")
	fp.write("@attribute commas numeric\n")
	fp.write("@attribute colons_and_semi_colons numeric\n")
	fp.write("@attribute dashes numeric\n")
	fp.write("@attribute parentheses numeric\n")
	fp.write("@attribute ellipses numeric\n")
	fp.write("@attribute common_nouns numeric\n")
	fp.write("@attribute proper_nouns numeric\n")
	fp.write("@attribute adverbs numeric\n")
	fp.write("@attribute wh_words numeric\n")
	fp.write("@attribute modern_slang_acronyms numeric\n")
	fp.write("@attribute words_all_in_upper numeric\n")
	fp.write("@attribute avg_len_of_sentences numeric\n")
	fp.write("@attribute avg_len_of_tokens numeric\n")
	fp.write("@attribute num_of_sentences numeric\n")
	fp.write("@attribute num_of_emoti numeric\n")
	fp.write("@attribute emotion {0,4}\n")
	fp.write("\n")
	fp.write("@data\n")

if __name__ == "__main__":
	main(sys.argv)

