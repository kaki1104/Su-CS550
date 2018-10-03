#https://stackoverflow.com/questions/36695422/replace-an-element-in-a-2d-list

import sys
import random
import os

def clear(): #function to clear the terminal 
	os.system('clear')

w = int (sys.argv [1])+2
h = int (sys.argv [2])+2
b = int (sys.argv [3])

if b >= w * h :
	print ("We can't place that many bombs...")
	quit()

l = [[0] * (w) for x in range (h)]
m = [["□"] * (w) for x in range (h)]

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

def showboard () :
	clear ()
	for y in range (1,w-1) :
		for x in range (1,h-1) :
			print (m[x][y],end=" ")
		print("")

def action() :
	try:
		for y in range (1,w-1) :
			for x in range (1,h-1) :
				revealflag, x, y = input ("You can choose a space to either reveal or flag. \nEnter the position and whetehr you would like to reveal or flag, split by two spaces (ex. flag 1 1): ").split()
				x = int (x)
				y = int (y)
				if revealflag == "flag" :
					m[x][y] =  str("F")
					showboard()
				elif revealflag == "reveal" : 
					if l[x][y] != "*":
						m[x][y] = l[x][y]
						if m [x][y] == 0 :
							m[x-1][y-1] = l[x-1][y-1]
							m[x-1][y+1] = l[x-1][y+1]
							m[x-1][y] = l[x-1][y]
							m[x][y-1] = l[x][y-1]
							m[x][y+1] = l[x][y+1]
							m[x+1][y-1] = l[x+1][y-1]
							m[x+1][y] = l[x+1][y]
							m[x+1][y+1] = l[x+1][y+1]
						showboard()
					elif l[x][y] == "*" :
						print ("You've hit the bomb! Game over!")
						quit()
				else: 
					print ("You must enter reveal or flag.")
					action()
					
	except ValueError :
		print ("Are you sure you entered the command the right way?")
		action ()
	except IndexError:
		print ("Are you sure your position was in the right range?")
		action ()

showboard()
action()

for y in range (1,w-1) :
	for x in range (1,h-1) :
		print (l[x][y],end=" ")
	print("")



