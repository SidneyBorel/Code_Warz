#!/usr/bin/env python

import sys
f = open(sys.argv[1], "r")

while True:
	line = f.readline().strip()
	if not line: break
	reverse = line[::-1]
#	print "here"
	print (line == reverse)

