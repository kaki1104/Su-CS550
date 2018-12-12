
#Kaki Su and Stephanie Hotz
#November 11, 2018
#We recommend using a white background for the terminal so that the colors come out nicely.
#This program contains a dictionary of periodic table, including each element's name, symbol, number and weight. It can display other traits of that element if you enter one of the information. It can also add the weights together and give you the weight of a molecule when you enter its formula.
#Sources for lists:
#https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python
#Sources for dictionary: 
#https://www.tutorialspoint.com/python/dictionary_get.htm
#https://docs.python.org/3/howto/regex.html
#https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
#sources for coloring in terminal: 
#https://www.geeksforgeeks.org/print-colors-python-terminal/ 
#http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

#I have neither given nor received unauthorized aid. Jiaqi Su

from Element import Element #imports the Element class from another file
from PeriodicTable import PeriodicTable #imports the PeriodicTable class from another file
import os
import sys
import time

def clear(): #function to clear the terminal 
		os.system('clear')

def delay_print(s): #function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
    for c in s:
    	sys.stdout.write(c)
    	sys.stdout.flush()
    	time.sleep(0.02)

def main () :
	pt = PeriodicTable('elements.csv') #imports things from PeriodicTabel class as pt
	clear () #clears terminal so that it's easy to read.
	delay_print ("\nWelcome to the periodic element dictionary! \nYou can choose to: \n\u001b[31mDisplay information about an element, \n\u001b[33mCalculate the weight (g/mol) for a compound, \n\u001b[32mCalculate mols for a certain weight of a compound, \u001b[0mor \n\u001b[34mFind the element that has the nearest weight as the weight that you enter\u001b[0m.")
	#used ANSI escape code to color specific phrases.
	while True : #will loop until user quits.
		choice = input ("\n\nEnter \u001b[31mdisplay, \u001b[33mcompound, \u001b[32mmoles, \u001b[34mnearest, \u001b[0mor quit: ")
		if str.lower(choice) == "display" : #will run the display function in pt
			clear ()
			info = input ("\nEnter an element name, number, symbol, or weight: ")
			print (pt.display(info))

		elif str.lower(choice) == "compound": #will run the calcWeight function in pt
			clear ()
			compound = input ("Enter a compound: ")
			print (str(pt.calcWeight(compound)))

		elif str.lower(choice) == "moles" : #will run the calcMoles function in pt
			clear ()
			try:
				compound, grams = input ("Enter a compound and its weight in grams, split by a space: ").split()
				print (pt.calcMoles(compound, grams))
			except ValueError: #will catch it when the user doesn't enter two commands or gives a string for the weight/a float for the compound
				delay_print ("\u001b[31mAre you sure you entered two commands the right way? Try again.\u001b[0m")

		elif str.lower(choice) == "nearest": #will run the nearestWeight function in pt
			clear ()
			try: 
				weight = input ("Enter a weight: ")
				print(pt.nearestWeight(float(weight)))
			except ValueError:
				delay_print ("\u001b[31mAre you sure you entered one number? Try again.\u001b[0m")

		elif str.lower(choice)  == "quit" : #will quit the program
			clear
			delay_print ("See you later! Bye!\n")
			exit ()

		else : #if the user enters an invalid command
			delay_print ("\u001b[31mPlease enter a valid command.\u001b[0m")
      
main()