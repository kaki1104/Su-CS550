#class notes on class
#try not to print or ask for input 

class Dog : #capital letter,singular
	#constructor
	def __init__ (self, name, energy, fullness) :
		self.fullness = fullness
		self.energy = energy
		self.happiness = 5
		self.name = "Fido"

	#methods/functions

	def play (self):
		if self.energy > 0 and self.fullness > 0 :
			self.happiness += 1
			self.fullness -= 1
			self.energy -= 1
			status = self.name + " played and it was fun."
		else:
			status = "hmm... "+self.name+" is tired. Maybe try a nap or some food?"
		return status

	def eat (self):
		if self.fullness <= 10 :
			self.happiness += 1
			self.fullness += 1
			status = self.name + " played and it was fun."
		else:
			status = ""+self.name+" is full. Maybe go out and play?"
		return status

	def stats (self) :
		info = "\nName: " + self.name
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nFullness: " + str(self.fullness)
		return info



dog1 = Dog ("Tetris", 8, 2)
dog2 = Dog ("Bat", 5, 7)
# print (dog1.name)

dog1.play()
dog2.play()
dog1.play()

while True: 
	print (dog1.stats())
	choice = input ("What would you like to do with your dog? \nEnter here: ")
	if choice == "play" :
		print (dog1.play())
	elif choice == "eat" :
		print (dog1.eat())
	else :
		print ("You can't do that.")
