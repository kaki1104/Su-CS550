
class Element :	#this Element class defines the variables for an individual element in a periodic table
  
	def __init__ (self, element, number, symbol, weight) : #defines the initial values 
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def getElement(self): #returns element name
		return self.element

	def getNumber(self): #returns element number
		return self.number

	def getSymbol(self): #returns element symbol
		return self.symbol

	def getWeight(self): #returns element weight
		return self.weight

	def __str__ (self) : #gives the format of how each element is displayed so that it is easy to read for the user.
		info = ""
		info += "\nInformation about " + self.element 
		info += " (" + self.symbol + ") "
		info += ":\nAtomic Number: " + self.number 
		info += "\nAtomic Weight: " + self.weight + "u"
		return info
  
	__repr__ = __str__