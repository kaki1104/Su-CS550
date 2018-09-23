#Kaki Su
#September 17, 2018
#Description: 
#sources: 
#how to measure time used to perform a function: https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
#how to make the variables global: https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment
#How to import two values from one input: https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python
#How to clear the terminal: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-consoles
#How to delay printing : https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
#Honor code: I have neither given nor received unauthorized aid.

import random
import os
import time 
import sys

hungerlevel = random.randint (3,11)

def clear():
	os.system('clear')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def hunger () :
	global hungerlevel
	hungerlevel = str(hungerlevel)
	input ("Your current hunger level is "+hungerlevel+" [Press Enter]")
	input ("Your goal is to decrease your hunger level to around 0. [Press Enter]")
	input ("Anything from -2 to 2 will make you happy, but being too full or too hungry will make you unhappy. [Press Enter]")

def start () :
	delay_print ("You are hungry......")
	hunger()
	clear ()
	delay_print ("Now you want to make some food for yourself......")


def cutting () :
	from timeit import default_timer as timer
	input ("\nNow you have to cut them by hitting c on the keyboard five times and hit enter. Make sure to do it fast.\n Are you ready?[Press Enter]")
	start = timer()
	cut = input ("Go!")
	end = timer ()
	if cut == "ccccc" :
		if float(end - start) <= 3 :
			input ("Okay, good. let's move on. [Press Enter]")
			clear ()
		else :
			print ("Oops, you were a little clumsy. The cutting wasn't good enough.[Press Enter]")
			cutting ()
	else : 
		 print ("You didn't cut it the right way. Try again.")
		 clear ()
		 cutting()

def showhunger () :
	global hungerlevel
	hungerlevel = str (hungerlevel)
	input ("Your hunger level is "+hungerlevel+" now. [Press Enter]")

def saladbase ():
	delay_print ("\nWhat greens do you want as your salad base?")
	greens = input ("\nIt looks like you have lettuce, spinach, kale, and arugula in the fridge. All of these will decrease your hunger level by -2. \n Enter a salad base: ")
	if greens == "lettuce" or greens =="spinach" or greens =="kale" or greens =="arugula" :
		delay_print ("taking out "+greens+" from the fridge.........")
		cutting ()
		global hungerlevel 
		hungerlevel = int (hungerlevel) - 2
	else :
		delay_print ("I don't think it's a good idea...")
		saladbase ()

def meatchoice () :
	clear ()
	delay_print ("I think we need some protein.")
	meat = input ("\nDo you want chicken, pork, or beef? These will all decrease your hunger level by 3. \n Enter chicken, pork, beef, or I am vegetarian:")
	if meat == "chicken" or meat == "pork" or meat == "beef" :
		input ("Okay. Let's get some "+meat+" out of the fridge.")
		global hungerlevel 
		cutting ()
		hungerlevel = int (hungerlevel) - 3
		showhunger ()
		clear ()
	elif str.lower (meat) == "i am vegetarian" :
		input ("Let's just get some other stuff in then.")
	else :
		input ("Please enter a valid command.")
		meatchoice ()

def toppingchoice () :
	clear ()
	topping = input ("Do you want toppings? \nType yes or no:")
	if topping == "yes" : 
		input ("Let's see what you have in the fridge... You have tomato, cucumber, avocado, onion, carrot, tofu. [Press enter]")
		top1, top2 = input("You can choose two toppings. \n Enter two toppings and split them by a space:").split()
		if (top1 == "tomato" or top1== "cucumber" or top1 == "avocado" or top1 =="onion" or top1 == "carrot" or top1 == "tofu") and (top2 == "tomato" or top2== "cucumber" or top2 == "avocado" or top2 =="onion" or top2 == "carrot" or top2 == "tofu") :
			if top1 == top2 :
				print ("okay. I guess you like "+top1+" a lot.")
				global hungerlevel 
				hungerlevel = int (hungerlevel) - 2
			elif top1 != top2 :
				input (""+top1+" and " +top2+" seem like good choices!")
				hungerlevel = int (hungerlevel) - 2
		else :
			input ("Please enter two valid toppings.")
			toppingchoice ()
	elif topping == "no" : 
		input ("Okay, you don't really like toppings I guess. [no change in hunger level] [Press enter]")
	else :
		delay_print ("uh...what?")
		toppingchoice()


def salad() :
	delay_print ("Feeling healthy, huh?")
	saladbase()
	input ("Phew. Now you get to choose your toppings. [Press enter]")
	meatchoice ()
	toppingchoice ()

def sandwichbase () :
	input ("let's choose what type of bread to use.")
	bread = input ("What greens do you want as your salad base? It looks like you have whole grain, whole wheat, multi grain, and rye. (hunger level -2) \nEnter a bread type:")
	if bread == "whole grain" or bread =="whole wheat" or bread == "multi grain" or bread =="rye" :
		delay_print ("taking out "+bread+" bread from the fridge...")
		cutting ()
		global hungerlevel 
		hungerlevel = int (hungerlevel) - 5
		showhunger ()
	else :
		delay_print ("I don't think it's a good idea...")
		sandwichbase ()

def sandwich ():
	delay_print ("You're pretty hungry, aren't you?")
	sandwichbase ()
	input ("Now you get to choose what to put inside.")
	meatchoice ()
	toppingchoice()


def result ():
	clear ()
	input ("Yumyumyum! You enjoyed your food. [Press Enter]") 
	clear ()
	showhunger ()
	clear ()
	if  -2 <= int (hungerlevel) <= 2 :
		print ("You have successfully satisfied your hunger! Congrats!")
	elif -2 >= int (hungerlevel) :
		print ("Oops... I think you ate too much. You're feeling kinda gross. Be careful next time!")
	elif 2 <= int (hungerlevel) :
		input ("Oops... I think you ate too little. You're still hungry...")
		tryagain = input ("Do you want to try again?")
		if tryagain == "yes" :
			system ()
		else :
			print ("ok, whatever. babai.")
		
	

def system () :
	clear ()
	start ()
	delay_print ("What do you want to make?")

	loop = 1
	while loop == 1:
		recipe = input (" \nYou can make a salad (decreases hunger level by 2-7) or a sandwich (decreases hunger level by 5-10). \n  Enter salad or sandwich:")

		if str.lower(recipe) == "salad":
			salad ()
			loop = 0
		elif str.lower(recipe) == "sandwich":
			sandwich ()
			loop = 0
		else :
			print ("I don't really know how to make "+recipe+"...")
			loop = 1
		
	result ()

system ()

	





