import random

class Card :
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __str__ (self, number, suit)
		return ""+self.number+" of "+self.suit+""

class Deck : 

	number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

	def __init__(self) :
		self.cards = []
		for number in range (13) :
			for number in range (4) :
				card = Card (number, suit)
				self.cards.append (card)

	def __str__ (self) :
		return self.cards

	def draw (self,number,suit) :
		return random.choice (self.cards)

	def shuffle (self) :
		random.shuffle (self.cards)
		return self.cards

def main () :
	


