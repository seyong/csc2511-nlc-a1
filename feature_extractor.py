#!/usr/bin/python
#! -*- encoding:utf-8 -*-
import re

class Extractor(object):

	punc = "[#\$\.,;:()\"\'`]"
	first_person = ["I","me","my","mine","we","us","our","ours"]
	second_person = ["you","your","yours","u","ur","urs"]
	third_person = ["he","him","his","she","her","hers","it","its","they","them","their","theirs"]
	future_tense = ["'ll","will","gonna"]
	mslangs = ["smh","fwb","lmfao","lmao","lms","tbh","rofl","wtf","bff","lylc","brb","atm","imao","sml","btw","bw","imho","fyi","ppl","sob","ttyl","imo","ltr","thx","kk","omg","ttys","afn","bbs","cya","ez","f2f","gtr","ic","jk","k","ly","ya","nm","np","plz","ru","so","tc","tmi","ymi","ur","u","sol"]

	def __init__(self):
		self.test = ""

	def load_tweet(self,tweet):
		self.tweet = tweet
	
	def get_features_result(self):
	 return "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%.1f,%.1f,%.1f,%d,%d" % (self.cal_fpp_count(), self.cal_spp_count(), self.cal_tpp_count(),self.cal_coord_conj_count(),self.cal_past_verb_count(),self.cal_future_verb_count(), self.cal_commas_count(), self.cal_colons_and_semi_colons_count(), self.cal_dashes_count(), self.cal_parentheses_count(),self.cal_ellipses_count(), self.cal_common_nouns_count(), self.cal_proper_nouns_count(), self.cal_adv_count(), self.cal_wh_words_count(), self.cal_modern_slang_count(), self.cal_words_in_upper_count(), self.cal_avg_len_of_sen(),self.cal_avg_len_of_tokens(),self.cal_num_of_sentences(),self.cal_num_emoti(),self.tweet.get_polar())

	def cal_num_emoti(self):
		count = 0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ')
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word in ["$smiley$","$laugh$","$wink$","$sad$","$playful$"]):
					count +=1
		return count

	def cal_fpp_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				#print "detected W %s/ T %s %d" % (word,tag,len(tag))
				if(tag == "PRP" or tag == "PRP$"):
					for p in self.first_person:
						if(re.search(p,word) is not None):
							count += 1
		return count	

	def cal_spp_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "PRP" or tag is "PRP$"):
					for p in self.second_person:
						if(re.search(p,word) is not None):
							count += 1
		return count	

	def cal_tpp_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "PRP" or tag is "PRP$"):
					for p in self.third_person:
						if(re.search(p,word) is not None):
							count += 1
		return count	

	def cal_coord_conj_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "CC"):
					count += 1
		return count	

	# Do it later
	def cal_past_verb_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag in ["VBD","VBN"]):
					count += 1
		return count	

	# DO it later
	def cal_future_verb_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word in self.future_tense):
					count += 1
		return count	

	def cal_commas_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is ","):
					count += 1
		return count	

	def cal_colons_and_semi_colons_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word is ":" or word is ";"):
					count += 1
		return count	

	def cal_dashes_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word is "-"):
					count += 1
		return count	

	def cal_parentheses_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word is "(" or word is ")"):
					count += 1
		return count	

	def cal_ellipses_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is ":"):
					if(re.search(r"(\.\.)(\.+)",word) is not None):
						count += 1
		return count	

	def cal_common_nouns_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "NN" or tag is "NNS"):
					count += 1
		return count	

	def cal_proper_nouns_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "NNP" or tag is "NNPS"):
					count += 1
		return count	

	def cal_adv_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag is "RB" or tag is "RBR" or tag is "RBS"):
					count += 1
		return count	

	def cal_wh_words_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(tag in ["WDT","WP","WP$","WRB"]):
					count += 1
		return count	

	def cal_modern_slang_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(word in self.mslangs):
					count += 1
		return count	

	def cal_words_in_upper_count(self):
		count = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				word = m.group(1)
				if(len(word) >= 2):
					if(re.search("[A-Z]{"+str(len(word))+",}",word) is not None):
						count += 1
		return count	

	#(in tokens)
	def cal_avg_len_of_sen(self):
		summ = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			summ = summ + len(tokens)

		return summ/self.tweet.get_number_of_sentences()

	#(in characters, excluding punctuations)
	def cal_avg_len_of_tokens(self):
		num_token = 0.0
		char_in_token = 0.0
		for s in self.tweet.get_sentences():
			tokens = s.split(' ') #tokens is list
			num_token += len(tokens)
			for token in tokens:
				m = re.search(r"(.+)/(.+)",token)
				tag = m.group(2)
				if(re.search(self.punc,tag) is not None):
					# not a punctuation
					char_in_token  += len(m.group(1))

		return char_in_token / num_token

	def cal_num_of_sentences(self):
		return self.tweet.get_number_of_sentences()

