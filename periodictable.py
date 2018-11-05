#periodictable.py

class Element :
	
	def __init__ (self, element, number, symbol, weight) :
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def __str__ (self) : 
		return "\nInformation about " + self.element + " (" + self.symbol + ") :\nAtomic Number: " + self.number + "\nAtomic Weight: " + self.weight + "u"

	__repr__ = __str__



def main () :
	file = open('elements.csv')
	allelements=[]
	for line in file:
		part = line.split(',')
		allelements.append(Element(part[0],part[1],part[2],part[3]))
	print (allelements)
main ()