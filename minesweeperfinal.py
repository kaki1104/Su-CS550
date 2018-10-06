#Kaki Su
#October 5th, 2018
#This is a minesweeper game.
#sources: How to replace an eleent in a 2d list: https://stackoverflow.com/questions/36695422/replace-an-element-in-a-2d-list
#comparing two lists: https://www.quora.com/How-can-I-do-a-comparison-of-two-lists-in-Python-with-each-value
#How to clear the terminal: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-consoles
#How to delay printing : https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
#Honor code: I have neither given nor received unauthorized aid. Jiaqi Su

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
	try: 
		w = int (sys.argv [1]) + 2
		h = int (sys.argv [2]) + 2
		b = int (sys.argv [3])
		if b >= w * h :
			print ("We can't place that many bombs...")
			quit ()
	except ValueError :
		delay_print ("You need to enter three numbers. Try again. \n")
		quit ()
	except IndexError :
		delay_print ("You need to enter three numbers. Try again. \n")
		quit ()

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
		clear ()
		for y in range (1,w-1) :
			for x in range (1,h-1) :
				print (l[x][y],end=" ")
			print("")

	def tryagain () : #gives user the option to play the game again no matter if they win or lose.
		delay_print ("Would you like to play again?")
		yesorno = input ("\nEnter yes or no: ")
		if yesorno == "yes" :
			main ()
		elif yesorno == "no" :
			delay_print ("See you next time!\n")
			quit()
		else: 
			delay_print ("Please enter yes or no. ")
			tryagain ()

	def action() :
		try:
			showm ()
			for y in range (1,w-1) :
				for x in range (1,h-1) : #goes through all numbers on board
					if m[x][y] != l[x][y] :
						revealflag, x, y = input ("You can choose a space to either reveal or flag. \nEnter the row, column and either reveal or flag, each split by a space (ex. flag 1 1, reveal 2 3): ").split()
						x = int (x)
						y = int (y)
						if x > (w-2) or x < 1 or y > (h-2) or y <1 : #if the user input is out of range
							delay_print ("You can only select a number up to the board size. Try again.")
							input (" [Press Enter]")
							action ()
						elif revealflag == "flag" : #scenarios when the user flags a position within range
							if m[x][y] == "□" :
								m[x][y] = str("*")
								action ()
							elif m[x][y] == "*" : #can't flag twice
								delay_print ("You already flagged that position.")
								deflag = input ("\nWould you like to de-flag that space?\nType yes or no: ")
								if deflag == "no" :
									action ()
								elif deflag == "yes" : #makes it back to original
									m[x][y] = "□"
									action ()
							else:
								delay_print ("You already revealed this position, so you can't flag it. Try again.")
								input (" [Press Enter]")
								action ()
						elif revealflag == "reveal" : #scenarios when the user reveals a position within range
							if m [x][y] == "□" : #when the board is not yet revealed
								if l[x][y] != "*" : #when user is trying to reveal a number
									m[x][y] = l[x][y] #reveals solution for selected grid
									i = 0
									while i < w or i < h : #will go through all the grids on the board to reveal all grids around a revealed 0 as many times as the number of rows/columns it has, because else it will just go through the board once and reveal only the grids to the right or the bottom. 
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
									action ()
								else : # if the user reveals a bomb = game over
									showl () #will show the solution like the original minesweeper game
									delay_print ("You've hit the bomb! Game over!\n")
									tryagain ()
							else: 
								delay_print ("You've already revealed this position. Try a different space.")
								input (" [Press Enter]")
								action ()
						else: #if the user entered something else invalid
							delay_print ("You must enter reveal or flag a position. Try again.")
							input (" [Press Enter]")
							action()
			delay_print ("Congrats! You beat the game!\n")
			tryagain ()
		except ValueError :
			delay_print ("Are you sure you entered the command the right way? Try again.")
			input (" [Press Enter]")
			action ()
		except IndexError:
			delay_print ("Are you sure your position was in the right range? Try again.")
			input (" [Press Enter]")
			action ()
	action ()

main ()

