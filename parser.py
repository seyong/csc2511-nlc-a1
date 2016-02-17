#!/usr/bin/python
#! -*- encoding=utf-8 -*-

class CMDParser:
	input_filenames = ""	
	def parse(args):
		if(len(args) ==4):
			input_filenames = args[1]
			output_filename = args[3]
			try:
				group_number = int(args[2])
				is_group_exist = true
			except ValueError:
				print "Parameter (%s) is not a numeric" % args[2]
		elif(len(args) == 2)
