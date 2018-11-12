#Kaki Su and Stephanie Hotz
#This program contains a dictionary of periodic table, including each element's name, symbol, number and weight. It can display other traits of that element if you enter one of the information. It can also add the weights together and give you the weight of a molecule when you enter its formula.
#Sources: https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python
#I have neither given nor received unauthorized aid. Jiaqi Su

from Element import Element
from PeriodicTable import PeriodicTable
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
	pt = PeriodicTable('elements.csv')
	clear ()
	delay_print ("\nWelcome to the periodic element dictionary! \nYou could choose to display information about an element, calculate the weight for a molecule, calculate mols for a certain weight of an element. ")
	while True :
		choice = input ("\nEnter display, molecule, moles, or quit: ")
		if str.lower(choice) == "display" :
		  clear ()
		  info = input ("\nEnter an element name, number, symbol, or weight: ")
		  print (pt.display(info))
		elif str.lower(choice) == "compound":
		  clear ()
		  compound = input ("Enter a compound: ")
		  print (pt.calcWeight(compound))
		elif str.lower(choice) == "moles" :
		  clear ()
		  compound, grams = input ("Enter a compound and its weight in grams, split by a space: ").split()
		  print (pt.calcMoles(compound, grams))
		elif str.lower(choice)  == "quit" :
		  clear 
		  delay_print ("See you later! Bye!       ")
		  exit ()

main ()