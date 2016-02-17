#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import HTMLParser


# Todo
# some punctuations are not handled at this moment
#  # $ . , : ( ) " `` ' "
# Only few of emoticons are considered
# compound noun is not processed
class Tweet(object):
	""" Custom Twitter Class for Natural Language Processing """
	ABBREVS = ["Ch","Dr","Drs","Gen","Lt","MR","MRS","Md","Messrs","Mmes","Mr","Mrs","No","Prof","Rep","Sr","St","Supt","Vol","dr","vs"]
	ABBREVS2 = ["Ala","Ariz","Assn","Atty","Aug","Ave","Bldg","Blvd","Calif","Capt","Cf","Col","Co","Colo","Conn","Corp","DR","Dec","Dept","Dist","Ed","Eq","FEB","Feb","Fig","Figs","FLA","Ga","Gen","Gov","HON","Ill","Inc","Inc","JR","Jr","Kan","Ky","La","Ltd","MRMass","Mar","Mich","Minn","Mo","Mt","Oct","Nov","Okla","Op","Ore","Pa","Pp","Prop","Rd","Ref","Reps","Rev","Rte","Sen","Stat","Tech","Tex","Va","Wash","al","av","ave","ca","cc","chap","cm","cu","dia","eqn","etc","fig","figs","ft","gm","hr","in","kc","lb","lbs","mg","ml","mm","mv","nw","oz","pl","pp","sec","sq","st","vr"]
	EMOTIS = {"$smiley$" : [":-)",":)",": )",":D",": D", "=)",":}",":^)",":]",":>","(-:","(:","(=","{:","(^:","[:","<:"],
						"$laugh$" : [":-D","8D","xD","XD","=D","x-D","X-D"],
						"$wink$":[";-)",";)",";-]",";]",";^)","; )"],
						"$sad$":[">:[",":-(",":(",":-c",":c",":-[",":["],
						"$playful$":[":p",":P",":-p",":-P",":b","=p","=P","x-p",";p","; p",";-p",";P",";-P"]
						}

	def __init__(self,row):
		self.polar = row[0]
		self.twtid = row[1]
		self.date = row[2]
		self.query = row[3]
		self.user = row[4]
		self.tweet = row[5]
		self.raw_tweet = row[5]
		self.htmlparser = HTMLParser.HTMLParser()

	# Preprocess
	# remove html tags and attrs first. tokenize by white space. 
	# 
	def do_preprocess(self):
		self.remove_html_tags_attrs()
		self.remove_url()
		self.remove_hash_and_at()
		self.replace_html_code_to_str()
		self.convert_emoti_to_sym()
		self.set_eos()
		self.separate_clitics()
		self.separate_possessive_s()
		self.convert_RT_to_sym()
		self.shorten_whitespace()
		#self.separate_punctuations()

	def remove_html_tags_attrs(self):
		pat = r"<[^>]+>"
		self.tweet = re.sub(pat," ",self.tweet)

	def replace_html_code_to_str(self):
		pat = r"&...;?"
		for m in re.finditer(pat,self.tweet):
			converted = self.htmlparser.unescape(m.group(0)).encode('utf-8')	
			self.tweet = re.sub(m.group(0),converted, self.tweet)

	# Make emoticons in tweet as a symbol, prevent from being processed in later stage
	def convert_emoti_to_sym(self):
		for k in self.EMOTIS.keys():
			for emo in self.EMOTIS[k]:
				self.tweet = self.tweet.replace(emo,k)

	# The first character in Twitter user names and hash tags are removed.
	def remove_hash_and_at(self):
		pat = r"(^|\s)(@|#)(.*?)($|\s)"
		for m in re.finditer(pat,self.tweet):
			#self.tweet = re.sub(m.group(2),"$HASH_SHARP$",self.tweet)
			self.tweet = re.sub(m.group(2)," ",self.tweet)

	def remove_url(self):
		pat = r"(^|\s)http(.*?)($|\s)"
		self.tweet = re.sub(pat," ",self.tweet)

	# Each sentence within a tweet is on its own line. 
	# Algorithm
	# - Place putative sentence boundaries after all occurences of . ? ! ; : -
	# - Move the boundary after following quotation marks, if any. 
	# - Disqualify a period boundary in the following circumstances
	# - 1 If it is preceded by a known abbreviation of a sort that does not normally occur sentence finally, but is commonly followed by a  capitalized proper name, such as Prof. or vs.
	# - 2 If is is preceded by a known abbreviation and not followed by an uppercase word. This will deal correctly with most usage of abbreviations like etc. or Jr. which can occur sentences medially or finally.
	# - Disqualify a boundary with a ? or ! if:
	# - 3	It is followed by a lowercase letter (or a known name.)
	# - Regard other putative sentence boundaries as sentences boundareis. 
	def set_eos(self):
		eos = "$EOS$"
		""" Add EOS mark after punctuation marks, be ware of  multiple punctuations """
		self.tweet = re.sub(r"(\.*(\.))"," \\1"+eos,self.tweet)
		self.tweet = re.sub(r"(\?*(\?))"," \\1"+eos,self.tweet)
		self.tweet = re.sub(r"(!*(!))"," \\1"+eos,self.tweet)
		self.tweet = re.sub(r"(,*(,))"," \\1"+eos,self.tweet)
		""" if the eos meets following quotation marks, move it """
		self.tweet = re.sub("\$EOS\$\""," \"$EOS$",self.tweet)

		"""1.For well known abbreviations, which occurs in the middle of sentences """
		for match in re.finditer(r"([a-zA-Z]*?)(\.)\$EOS\$",self.tweet):
			cand = match.group(1)
			if(cand in self.ABBREVS):
				self.tweet = re.sub(cand+"."+"$EOS$",cand+". ",self.tweet)

		""" 2. For well known abbreviations, and not followed by an uppercase word """
		for match in re.finditer(r"([a-zA-Z]*?)(\.)\$EOS\$\s*[^A-Z]",self.tweet):
			cand = match.group(1)
			if(cand in self.ABBREVS2):
				self.tweet = re.sub(cand+"."+"$EOS$ ", cand+". ",self.tweet)

		self.tweet = re.sub("\$EOS\$","\n",self.tweet)
	
	def separate_possessive_s(self):
		possessive_s = ["('s)","s(')"]
		for m in re.finditer("(^|\\s)([a-zA-Z]+)('s)(\\s)",self.tweet):
			self.tweet = re.sub("(^|\\s)([a-zA-Z]+)('s)(\\s)", " \\2 \\3 ",self.tweet)
		for m in re.finditer("(^|\\s)([a-zA-Z]+s)(')(\\s)",self.tweet):
			self.tweet = re.sub("(^|\\s)([a-zA-Z]+s)(')(\\s)", " \\2 \\3 ",self.tweet)
			
				
	def separate_clitics(self):
		clitics = ["'m", "'ve","'d","'ll"]
		for c in clitics:
			for m in re.finditer(c+"\\s",self.tweet):
				self.tweet = re.sub(m.group(0), " "+m.group(0),self.tweet)
		""" special case, n't """
		for m in re.finditer("(^|\\s)([a-zA-Z]+)n't\\s",self.tweet):
			if m.group(2) == "ca": #""" can't"""
				self.tweet = re.sub("(^|\\s)([a-zA-Z]+)(n't\\s)", " \\2n \\3", self.tweet)
			elif m.group(2) == "wo": #""" won't"""
				self.tweet = re.sub("(^|\\s)([a-zA-Z]+)(n't\\s)", " will \\3", self.tweet)
			else:
				self.tweet = re.sub("(^|\\s)([a-zA-Z]+)(n't\\s)", " \\2 \\3", self.tweet)
	
	def separate_punctuations():
		""" period, question mark, comman, exclamation is handled in set_eos function """
		return ""
				
	def convert_RT_to_sym(self):
		for m in re.finditer("RT",self.tweet):
			self.tweet = re.sub(m.group(0), "$RT$", self.tweet)

	def get_tweet(self):
		return self.tweet
		#header = "<A=" + str(self.polar) + ">"
		#return header + "\n" + self.tweet	
		#return header + "".join(re.split("(\W+)",self.tweet))

	def shorten_whitespace(self):
		self.tweet = self.tweet.strip()
		for m in re.finditer(r"([ \t]+)",self.tweet):
			self.tweet = re.sub(r"([ \t]+)"," ",self.tweet)

	def tagging(self,tagger):
		""" sentence by sentence tagging """
		token_set = []
		tag_set = []
		sentences = re.split("\n",self.tweet)
		for s in sentences:
			token_set.append(re.split(" ",s.strip()))
	
		for tokens in token_set:
			tag_set.append(tagger.tag(tokens))

		preprocessed_tweet = ""
		for i in range(0,len(token_set)):
			tokens = token_set[i]
			tags = tag_set[i]
			for j in range(0,len(tokens)):
				preprocessed_tweet = preprocessed_tweet + tokens[j] +"/"+tags[j] +" "
			preprocessed_tweet = preprocessed_tweet + "\n"

		self.tweet = preprocessed_tweet

	def printable_tweet(self):
		header = "<A=" + str(self.polar) + ">"
		return header + "\n" + self.tweet	
	
	
		
