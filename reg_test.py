#!/usr/bin/python

import sys
import re

# All html tags and attributes are removed
# Html character codes are replaced with an ASCII equivalent
# ALL URLs (tokens beginning with http or www) are removed
# The first character in Twitter user names(@) and hash tags(#) are removed
# Each sentences within a tweet is on its own line

tstr1 = "<html>Hello</html>"
tstr2 = "<html>Hello World</html>"
tstr3 = "<html><body> It's new </body></html>"

pattern = r"<.*?>"
print re.sub(pattern,"",tstr1)
print re.sub(pattern,"",tstr2)
print re.sub(pattern,"",tstr3)

