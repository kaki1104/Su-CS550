#guessnumber.py

import random
number = random.randint(1,100)

def guess() :
	estimate = input ("Guess the number! It's an integer in between 1 to 100.")
	estimate = float (estimate)

	if estimate == number :
		print ("Congrats! The number was right!")
		exit()

	while estimate != number :	
		if estimate >= number :
			print ("Too high.")
			guess()
		elif estimate <= number :
			print ("Too low.")
			guess()

guess()

