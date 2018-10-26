#bankaccount

class Bankaccount : 

	def __init__ (self, name, number, pin, balance) :
		self.name = "Kaki"
		self.number = 13474062
		self.pin = 1104
		self.balance = 0

	def deposit (self):
		self.balance += float(amount)
		status = "You have deposited "+amount+" dollars."
		return status

	def withdraw (self):
		if self.balance > 0 :
			self.balance -= float (amount)
			status = self.name + " played and it was fun."
		else:
			status = "Your do not have money to withdraw in your account. Oops."
		return status

	def stats (self) :
		info = "\nName: " + self.name
		info += "\nBalance: " + self.balance
		return info

person1 = Bankaccount ("Kaki", 1999, 1104, 100)
person2 = Bankaccount ("Mom", 1971, 813, 1000)

name, pin = input ("Enter your account number and pin, with a space in between. \nEnter here: ").split
if name == person1.number and person1.pin :
	print (person1.stats())
	choice = input ("What would you like to do?: ")
	if choice == "deposit" :
		print (person1.deposit())
	elif choice == "withdraw" :
		print (person1.withdraw())
	else :
		print ("You can't do that.")