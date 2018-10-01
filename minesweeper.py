#https://stackoverflow.com/questions/36695422/replace-an-element-in-a-2d-list

import sys
import random

w = int (sys.argv [1])+2
h = int (sys.argv [2])+2
b = int (sys.argv [3])

if b >= w * h :
	print ("We can't place that many bombs...")
	quit()

l = [[0] * (w) for x in range (h)]

loop = 0
while loop < b :
	x = random.randint (1, w-1)
	y = random.randint (1, h-1)
	l[y][x] = str("*")
	loop = loop + 1


for y in range (1,w-1) :
	for x in range (1,h-1) :
		if l[x][y] == "*" : 
			if l[x+1][y+1] != "*" :
				l[x+1][y+1] = int(l[x+1][y+1]) + 1
			if l[x+1][y-1] != "*" :
				l[x+1][y-1] = int(l[x+1][y-1]) + 1
			if l[x+1][y] != "*" :
				l[x+1][y] = int(l[x+1][y]) + 1
			if l[x][y+1] != "*" :
				l[x][y+1] = int(l[x][y+1]) + 1
			if l[x][y-1] != "*" :
				l[x][y-1] = int(l[x][y-1]) + 1
			if l[x-1][y] != "*" :
				l[x-1][y] = int(l[x-1][y]) + 1
			if l[x-1][y+1] != "*" :
				l[x-1][y+1] = int(l[x-1][y+1]) + 1
			if l[x-1][y-1] != "*" :
				l[x-1][y-1] = int(l[x-1][y-1]) + 1
		
for y in range (1,w-1) :
	for x in range (1,h-1) :
		print (l[x][y],end=" ")
	print("")
