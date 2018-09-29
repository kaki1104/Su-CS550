#https://stackoverflow.com/questions/36695422/replace-an-element-in-a-2d-list

import sys
import random

w = int (sys.argv [1])
h = int (sys.argv [2])
b = int (sys.argv [3])

l = [[0]*w for x in range (h)]

loop = 0
while loop < b :
	x = random.randint (0, w-1)
	y = random.randint (0, h-1)
	l[y][x] = str("*")
	loop = loop + 1

for x in range (len (l)) :
	loop = 0
	while loop < b :
		if l[x][y] != "*" : 
			try: 
				l[x+1][y+1] = int(l[x+1][y]) + 1
				l[x+1][y-1] = int(l[x+1][y]) + 1
				l[x][y] = int(l[x+1][y]) + 1
				l[x][y+1] = int(l[x+1][y]) + 1
				l[x][y-1] = int(l[x+1][y]) + 1
				l[x-1][y] = int(l[x+1][y]) + 1
				l[x-1][y+1] = int(l[x+1][y]) + 1
				l[x-1][y-1] = int(l[x+1][y]) + 1
				loop + 1
			except ValueError :
				pass
			loop = loop + 1
		elif l[x][y] == "*" :
			pass
		

for x in range (len (l)) :
	print (*l[x])
