#!/usr/bin/python

import sys
import re


tstr1 = "<html>Hello</html>"
tstr2 = "<html>Hello World</html>"
tstr3 = "<html><body> It's new </body></html>"


for text in sys.argv[2:]:
	if re.search(pat,text):
		result = "FOUND"
	else:
		result = "NOT FOUND"
	print pat, text, result
