#Kaki Su
#October 5th, 2018
#This is a minesweeper game.
#sources: How to replace an eleent in a 2d list: https://stackoverflow.com/questions/36695422/replace-an-element-in-a-2d-list

import sys
import random
import os
import time

def clear(): #function to clear the terminal 
		os.system('clear')

def delay_print(s): #function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def main () :

	w = int (sys.argv [1]) + 2
	h = int (sys.argv [2]) + 2
	b = int (sys.argv [3])
	if b >= w * h :
		print ("We can't place that many bombs...")
		quit()

	l = [[0] * (w) for x in range (h)] #the solution list
	m = [["□"] * (w) for x in range (h)] #the list that is shown to the user that will be ammended throughout

	loop = 0
	while loop < b : #generates as many bombs as the user input within the grids
		x = random.randint (1, w-2)
		y = random.randint (1, h-2)
		l[x][y] = str("*")
		loop = loop + 1 

	for y in range (1,w-1) : #looks around the bomb and adds number around the bomb to show how many bombs are adjacent to each grid
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

	def showm () :
		clear ()
		for y in range (1,w-1) :
			for x in range (1,h-1) :
				print (m[x][y],end=" ")
			print("")

	def showl() :
		for y in range (1,w-1) :
			for x in range (1,h-1) :
				print (l[x][y],end=" ")
			print("")

	def revealzero () :
		loop = 0
		while loop < w - y or loop < h - x :
			for y in range (1,w-1) :
				for x in range (1,h-1) :
					if m[x][y] == 0 :
						m[x-1][y-1] = l[x-1][y-1]
						m[x-1][y+1] = l[x-1][y+1]
						m[x-1][y] = l[x-1][y]
						m[x][y-1] = l[x][y-1]
						m[x][y+1] = l[x][y+1]
						m[x+1][y-1] = l[x+1][y-1]
						m[x+1][y] = l[x+1][y]
						m[x+1][y+1] = l[x+1][y+1]
						loop = loop + 1

	def tryagain () :
		yesorno = input ("Would you like to play again?\nEnter yes or no: ")
		if str.lower(yesorno) == "yes" :
			main ()
		elif str.lower (yesorno) == "no" :
			delay_print ("See you next time!\n")
			quit()
		else: 
			delay_print ("Please enter yes or no.")
			tryagain ()

	def action() :
		try:
			showm ()
			for y in range (1,w-1) :
				for x in range (1,h-1) :
					if m[x][y] != l[x][y] :
						revealflag, x, y = input ("You can choose a space to either reveal or flag. \nEnter the row, column and either reveal or flag, each split by a space (ex. flag 1 1, reveal 2 3): ").split()
						x = int (x)
						y = int (y)
						if revealflag == "flag" :
							if m[x][y] == "□" :
								m[x][y] = str("*")
								action ()
							elif m[x][y] == "*" :
								delay_print ("You already flagged that position...........")
								action ()
							else:
								delay_print ("You already revealed that position...........")
								action ()
						elif revealflag == "reveal" :
							if m [x][y] == "□" :
								if l[x][y] != "*":
									m[x][y] = l[x][y]
									i = 0
									while i < w or i < h :
										for y in range (1,w-1) :
											for x in range (1,h-1) :
												if m[x][y] == 0 :
													m[x-1][y-1] = l[x-1][y-1]
													m[x-1][y+1] = l[x-1][y+1]
													m[x-1][y] = l[x-1][y]
													m[x][y-1] = l[x][y-1]
													m[x][y+1] = l[x][y+1]
													m[x+1][y-1] = l[x+1][y-1]
													m[x+1][y] = l[x+1][y]
													m[x+1][y+1] = l[x+1][y+1]
										i = i + 1
									action()
								elif l[x][y] == "*" : 
									clear ()
									showl ()
									delay_print ("You've hit the bomb! Game over!\n ")
									tryagain ()
							else: 
								delay_print ("You've already revealed this position......................")
								action ()
						else: 
							delay_print ("You must enter reveal or flag.....................")
							action()
			delay_print ("Congrats! You beat the game!\n")
			tryagain ()
		except ValueError :
			delay_print ("Are you sure you entered the command the right way?")
			action ()
		except IndexError:
			delay_print ("Are you sure your position was in the right range?")
			action ()

	action ()

main ()

