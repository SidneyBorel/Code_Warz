#!/usr/bin/env python
import binascii

import sys

f = open(sys.argv[1], "r")

line = f.readline()
for number in line.split():
	sys.stdout.write(number.decode("hex"))
print

