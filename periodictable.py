#On my honor, I have neither given nor received unauthorized aid.

#This is the Periodic Table Class file (one of three for this project). This creates the Periodic Table to be used in the main part of the program.

#By Stephanie and Kaki

#PERIODIC TABLE

#SOURCES
#https://docs.python.org/3/howto/regex.html
#https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python

#IMPORTS
import re #This is the regular expressions module. It is used to find patterns in strings. This program uses it to take apart the compound that is given.
from Element import Element #This imports the Element class from the file Element.py
#CLASS
#This is the class for the periodic table that holds funtions that relate multiple elements.
class PeriodicTable:

	def __init__ (self, pfile): # Here, the file is opened and each line is split into different parts which are added to a dictionary.
		self.allelements = {}
		file = open('elements.csv')
		for line in file:
			part = line.split(',')
			if part[0] == "Element":
				continue #This eliminates the first first line of the file which is just text
			oneelement = Element(part[0], part[1], part[2], part[3]) # In this, the object from Class Element is intialized and set into a dictionary with the chemical symbol as the key for each element.	
			self.allelements[part[2]] = oneelement	

	def __str__ (self) : #This defines the string of all of the elements
		info = ""
		for e in self.allelements :
			info = str (e)
		return info
  
	__repr__ = __str__

#FUNCTIONS
	def display (self,given) :

		for symbol, element in self.allelements.items(): #This goes through the dictionary of elements and labels them as symbol, element
			if given in (element.getWeight(),element.getSymbol(),element.getNumber(),element.getElement()): #This checks to see if the given is equal to any of the element's attributes.
				return (element) #If it is, it will return the element.
			elif str.lower(given) in (str.lower(element.getSymbol()),str.lower(element.getElement())): #This will return the element even if the user enters the information in lower case
				return (element) 
			elif symbol == 'Lr' and given not in (element.getWeight(),element.getSymbol(),element.getNumber(),element.getElement()):
				return ("\u001b[31m"+ given + " is not a valid element attribute. Please try again.\u001b[0m")

	def calcWeight(self, compound) : # This funtion gives the atomic weight of a compund

		checker = '' # This checker will be used later to check if the compound calculated is the same as the one entered.

		matcher = re.compile('([A-Z][a-z]*)([0-9]*)') #This matcher funtion goes through the coumpound entered and matches a capital [A-Z] and any following letters [a-z] (the star says to find as many lowercase letters as possible) with the number [0-9](this star has the same function as the first for the numbers).

		parts = re.findall(matcher, compound) #This uses the matcher that was just set up to go through the compound given
		totalWeight = 0

		for part in parts: # This uses a for loop to go through each part that was identified in the matcher.
			if part[1]:	
				multiplier = float(part[1]) #If part[1] (the number after the symbol) exists then that becomes the multiplier for the weight of the element
			else:
				multiplier = 1 #If not, the multiplier is 1

			element = self.allelements.get(part[0]) # This retrieves the element from the dictionary using the chemical symbol key that was given in the compound and labeled as part[1].

			if not element: # This is some error checking to account for things that look like element (Egg, Pn, etc.)
				return ("\u001b[31m" + part[0]+ " is not a valid element in your compound. Please try again.\u001b[0m")

			weightofElement = element.getWeight() #The weight is set to the weight that was retrieved from the dictionary by using the getWeight() function from the Element Class.

			totalWeight = float(totalWeight) + float(weightofElement) * float(multiplier) #This is where the weight is multiplied by the number given and then added to the total

			#The checker is built by adding the parts together
			checker += part[0] + part [1]

		if checker == compound: #This checks if the compound that was calculated is the one entered
			return str(totalWeight)
		else:
			return("\u001b[31mYou entered an invalid compound. Please try again.\u001b[0m")

	def calcMoles(self, compound, grams) :	#This Calculates the moles that are in a number of grams of a compund.
		moles = float(grams)/float(self.calcWeight(compound))
		return str(moles) + " mols" #The grams of the element are given by the user and divided by atomic weight found by the calcWeight function. 

	def nearestWeight(self, weight): #This Function finds the element with the nearest weight to the one entered

		lowest = float(10000) #Initializing lowest as an impossibly high number, so the new number will definetly be lesser.

		lowestElement = '' #Initializing the element

		for symbol, element in self.allelements.items(): #This goes through the dictionary of elements and labels them as symbol, element.

			if abs(float(element.getWeight())-weight) < lowest: #The difference is taken between the number entered and the atomic weight of the element being tested and is compared to the current least difference.
			#If the difference is greater, it will move on to the next element, if it is lesser, the lesser number will become the new lowest.
				lowest = abs(float(element.getWeight())-weight)
				lowestElement = element

		return lowestElement  #This returns the element that had the closest atomic weight to the one entered
