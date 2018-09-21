#Kaki Su
#September 17, 2018
#Description: 
#sources: https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
#Honor code: I have neither given nor received unauthorized aid.

import random
hungerlevel = random.randint (3,11)
hungerlevel = str(hungerlevel)

def hunger () :
	input ("your current hunger level is "+hungerlevel+"↓")
	input ("your goal is to decrease your hunger level to around 0. Anything from -2 to 2 will make you happy, but being too full or too hungry will result to failure.↓")
	input ("if you forget, you can check your hunger level by entering hungerlevel at any time.↓") #acutally make this work

def start () :
	input ("you are hungry......↓")
	hunger()
	input ("you want to make some food for yourself...↓")


def menu () :
	recipe = input ("What do you want to make? \n You can make a salad (decreases hunger level by 3-7) or a sandwich (decreases hunger level by 5-10). \n Enter salad or sandwich.")

	if recipe == "salad" :
		salad ()
	elif recipe == "sandwich" :
		sandwich ()
	else :
		print ("I don't really know how to make "+recipe+"...")
		menu ()

def cutting () :
	from timeit import default_timer as timer
	input ("now you have to cut them by hitting c on the keyboard five times and hit enter. ready....↓")
	start = timer()
	cut = input ("go!")
	end = timer ()
	if cut == "ccccc" :
		if float(end - start) <= 3 :
			input ("okay, good. let's move on.↓")
		else :
			print ("oops, you were a little clumsy. The cutting wasn't good enough.")
			cutting ()
	else : 
		 print ("You didn't cut it the right way. Try again.")
		 cutting()

def saladbase ():
	greens = input ("What greens do you want as your salad base? It looks like you have lettuce, spinach, kale, and arugula in the fridge.")
	if greens == "lettuce" or greens =="spinach" or greens =="kale" or greens =="arugula" :
		input ("taking out "+greens+" from the fridge...")
		cutting ()
	else :
		print ("I don't think it's a good idea...")
		saladbase ()

def saladmeat () :
	meat = input ("I think we need some proteins. (hunger level -3) Do you want chicken, pork, or beef? \n Enter chicken, pork, beef, or I am vegetarian.")
	if meat == "chicken" or meat == "pork" or meat == "beef" :
		input ("Okay. Let's get some "+meat+" out of the fridge.")
	elif meat == "I am vegetarian" :
		input ("Let's just get some other toppings then.")
	else :
		input ("Please enter a valid command.")
		saladmeat ()


def saladtopping () :
	topping = input ("Do you want toppings? Type yes or no.")
	if topping == "yes" :
		toppings = input ("Let's see what you have in the fridge... You have tomato, cucumber, avocado, onion, carrot, tofu.")
	elif topping == "no" : 
		input ("wait, but you're still going to be super hungry if you just eat leaves...")
		saladtopping ()
	else :
		input ("Please type yes or no.")
		saladtopping()


def salad() :
	input ("feeling healthy, huh?")
	saladbase()
	input ("Phew. now you get to choose your toppings.")
	saladmeat ()
	saladtopping ()


def sandwich ():
	input ("hmmm.. you're pretty hungry, aren't you?")

start ()
menu()


	





