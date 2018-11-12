#Kaki Su and Stephanie Hotz
#This program contains a dictionary of periodic table, including each element's name, symbol, number and weight. It can display other traits of that element if you enter one of the information. It can also add the weights together and give you the weight of a molecule when you enter its formula.
#Sources: https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python
#I have neither given nor received unauthorized aid. Jiaqi Su
import os
import sys
import time

file = open('elements.csv')

def clear(): #function to clear the terminal 
		os.system('clear')

def delay_print(s): #function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

class Element :
	
	def __init__ (self, element, number, symbol, weight) :
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def getElement(self):
		return self.element

	def getNumber(self):
		return self.number

	def getSymbol(self):
		return self.symbol

	def getWeight(self):
		return self.weight

	def __str__ (self) : 
		info = ""
		info += "\nInformation about " + self.element 
		info += " (" + self.symbol + ") "
		info += ":\nAtomic Number: " + self.number 
		info += "\nAtomic Weight: " + self.weight + "u"
		return info

	__repr__ = __str__

file = open('elements.csv')
allelements = []
for line in file:
	part = line.split(',')
	allelements.append(Element(part[0],part[1],part[2],part[3]))

class PeriodicTable:

	def __init__ (self, pfile):
		self.allelements = {}
		file = open('elements.csv')
		for line in file:
			part = line.split(',')
			oneelement = Element(part[0], part[1], part[2], part[3])
			self.allelements[part[2]] = oneelement	

	def __str__ (self) :
		info = ""
		for e in self.allelements :
			info = str (e)
		return info

	def display (self, info) :
		for e in self.allelements :
			if str.lower(e.element) == str.lower(info) or e.number == info or str.lower(e.symbol) == str.lower(info) or e.weight == info :
				return (self.allelements[int(e.number)])

	def calcWeight(self, compound):
		matcher = re.compile('([A-Z][a-z]*)([0-9]*)')
		parts = re.findall(matcher, compound)
		totalWeight = 0

		for part in parts: 

			if part[1]:	
				multiplier = float(part[1])

			else:
				multiplier = 1

			element = self.allelements.get(part[0])
			#adderrorcheckinghere
			weightofElement = element.getWeight()
			totalWeight = float(totalWeight) + float(weightofElement) * float(multiplier)
		return totalWeight


	def calcMoles(self, compound, grams):
		
		return float(grams)/self.calcWeight(compound)

def main () :
	pt = PeriodicTable()
	clear ()
	delay_print ("\nWelcome to the periodic element dictionary! \nYou could choose to display information about an element, calculate the weight for a molecule, calculate mols for a certain weight of an element. ")
	choice = input ("\nEnter display, molecule, or mols: ")
	if choice == "display" :
		clear ()
		info = input ("\nEnter an element name, number, symbol, or weight: ")
		print (pt.display(info))
	if choice == "compound" :
		clear ()
		compound = input ("Enter a compound: ")
		print (pt.calcWeight(compound))
	if choice == "moles" :
		clear ()
		compound, grams = input ("Enter a compound and its weight in grams, split by a space: ").split
		print (pt.calclMoles(compound, gram))


main ()

print (PeriodicTable().self.allelements)