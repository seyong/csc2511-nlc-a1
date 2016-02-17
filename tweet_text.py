#!/usr/bin/python
#! -*- encoding:utf-8 -*-

class TweetText(object):
	
	def __init__(self):
		self.polar = -1
		self.sentences = []

	def set_polar(self,polar):
		self.polar = polar
	
	def add_sentences(self,s):
		s = s.strip()
		self.sentences.append(s)

	def get_polar(self):
		return self.polar
	
	def get_sentences(self):
		return self.sentences

	def get_number_of_sentences(self):
		return len(self.sentences)
	

