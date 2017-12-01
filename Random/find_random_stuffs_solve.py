#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
g = []

line = f.readline()

while True:
	for number in line.split():
		#if('.' in number)
			#g.appendleft(float(number))
		#else:
		g.append(int(number))

	num1 = g[0]
	num2 = g[1]
        g.clear()

	for value in range(num1,(num2+1)):
	        if value % 7 == 0 and value % 5 != 0:
			g.append(value)
	
	i = 0
	length = len(g)
	while i < (length-1):
		sys.stdout.write(str(g[i]) + ',')
		i = i + 1
	sys.stdout.write(str(g[(length - 1)]))
	print
        g.clear()

        line = f.readline()
        if not line: 
            break
