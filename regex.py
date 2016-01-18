#!/usr/bin/python

import sys
import re

pat = sys.argv[1]

for text in sys.argv[2:]:
	if re.search(pat,text):
		result = "FOUND"
	else:
		result = "NOT FOUND"
	print pat, text, result
