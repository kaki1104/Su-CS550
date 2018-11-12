
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