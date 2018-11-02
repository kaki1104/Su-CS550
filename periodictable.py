#periodictable.py

class Element :

 def __init__ (self, element, number, symbol, weight) :
 	self.element = element
 	self.number = number
 	self.symbol = symbol
 	self.weight = weight

 def __str__ (self) : 
 	return "Information about " + self.element + " (" + self.symbol + ") :\nAtomic Number: " + self.number + "\nAtomic Weight: " + self.weight + "u"

class Periodic Table :


def main () :
	h = Element("Hydrogen", "1", "H", "1.01")
	print (h)

main ()