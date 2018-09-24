#Kaki Su
#September 23, 2018
#Description: In this game, you will make a salad or a sandwich to satisfy your hunger level, which is assigned randomly in the beginning of the game. Your choices in the ingredients will affect how much satisfaction you will get, and your goal is to not be too full, but also not too hungry. While making food, the user must also perform certain tasks such as cutting food through pressing the keyboard quickly. 
#sources: 
#how to measure time used to perform a function: https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
#how to make the variables global: https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment
#How to import two values from one input: https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python
#How to clear the terminal: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-consoles
#How to delay printing : https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
#ascii art: https://www.asciiart.eu/computers/smileys
#Honor code: I have neither given nor received unauthorized aid.

import random
import os
import time 
import sys

hungerlevel = random.randint (3,10)

def clear(): #function to clear the terminal 
	os.system('clear')


def delay_print(s): #function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def hunger () : #explanation of hunger level system
	global hungerlevel
	hungerlevel = str(hungerlevel)
	input ("Your current hunger level is "+hungerlevel+" [Press Enter]")
	input ("Your goal is to decrease your hunger level to around 0. [Press Enter]")
	input ("You will be happy if you end up with a hunger level between -2 and 2, but being too full or too hungry will make you unhappy. [Press Enter]")

def start () : 
	delay_print ("You are hungry......")
	hunger()
	clear ()
	delay_print ("Now you want to make some food for yourself......")

def cutting () : #the cutting task, used for both salad and sandwich
	clear ()
	from timeit import default_timer as timer
	input ("Now you have to cut them by hitting c on the keyboard five times and hit enter. Make sure to do it fast.\n Are you ready?[Press Enter]")
	start = timer()
	cut = input ("Go! ")
	end = timer ()
	if cut == "ccccc" :
		if float(end - start) <= 3 : #if the task was performed under 3 seconds
			input ("Okay, good. let's move on. [Press Enter]")
			clear ()
		else :
			print ("Oops, you were a little clumsy. The cutting wasn't good enough.[Press Enter]")
			cutting ()
	else : 
		 delay_print ("You didn't cut it the right way........")
		 input ("\nTry again. [Press enter]")
		 clear ()
		 cutting()

def saladbase (): 
	clear ()
	delay_print ("\nWhat greens do you want as your salad base?")
	greens = input ("\nIt looks like you have lettuce, spinach, kale, and arugula in the fridge. All of these will decrease your hunger level by -2. \n Enter a salad base: ")
	if greens == "lettuce" or greens =="spinach" or greens =="kale" or greens =="arugula" :
		delay_print ("taking out "+greens+" from the fridge.........")
		cutting ()
		global hungerlevel 
		hungerlevel = int (hungerlevel) - 2 #decreases hunger level by three
	else :
		delay_print ("Are you sure you entered the right words? Try again..........")
		saladbase ()

def meatchoice () : #the choice of meet, works for both sandwich and salad
	clear ()
	delay_print ("I think we need some protein......   ")
	meat = input ("\nDo you want chicken, pork, or beef? These will all decrease your hunger level by 3. \n Enter chicken, pork, beef, or I am vegetarian: ")
	if meat == "chicken" or meat == "pork" or meat == "beef" :
		delay_print ("Okay. Let's get some "+meat+" out of the fridge..........")
		global hungerlevel 
		cutting ()
		hungerlevel = int (hungerlevel) - 3
		clear ()
	elif str.lower (meat) == "i am vegetarian" :
		input ("Let's just get some other stuff in then. [Press enter]")
	else :
		input ("Please enter a valid command. [Press enter]")
		meatchoice ()

def toppingchoice() : #made a seperate function from topping() because it was easier to put recursions in it.
	try:
		top1, top2 = input ("You can choose two toppings. \n Enter two toppings and split them by a space: ").split()
		if (top1 == "tomato" or top1== "cucumber" or top1 == "avocado" or top1 =="onion" or top1 == "carrot" or top1 == "tofu") and (top2 == "tomato" or top2== "cucumber" or top2 == "avocado" or top2 =="onion" or top2 == "carrot" or top2 == "tofu") :
			if top1 == top2 :
				print ("okay. I guess you like "+top1+" a lot.")
				global hungerlevel 
				hungerlevel = int (hungerlevel) - 2
			else :
				input (""+top1+" and " +top2+" seem like good choices!")
				hungerlevel = int (hungerlevel) - 2
		else :
			delay_print ("Are you sure you typed the right words?")
			input ("Please enter two valid toppings.")
			toppingchoice ()
	except ValueError :
		delay_print ("Are you sure you typed the right words?")
		toppingchoice ()

def topping () : #choices of toppings, works for both salad and sandwich
	clear ()
	top = input ("Do you want toppings? \nType yes or no: ")
	if top == "yes" : 
		delay_print ("Let's see what you have in the fridge.........   ")
		input ("\nYou have tomato, cucumber, avocado, onion, carrot, tofu. [Press enter]")
		toppingchoice()
	elif top == "no" : 
		input ("Okay, you don't really like toppings I guess. [no change in hunger level] [Press enter]")
	else :
		delay_print ("uh...what? Enter yes or no.")
		toppingchoice()

def sandwichbase () : 
	clear ()
	input ("Let's choose what type of bread to use. [Press enter]")
	bread = input ("What type of bread do you want to use for your sandwich? It looks like you have whole grain, whole wheat, multi grain, and rye. All of these will decrease your hunger level by -5. \nEnter a bread type: ")
	if bread == "whole grain" or bread =="whole wheat" or bread == "multi grain" or bread =="rye" :
		delay_print ("taking out "+bread+" bread..................")
		cutting ()
		global hungerlevel 
		hungerlevel = int (hungerlevel) - 5 #decreases hunger level by 5, but not shown to the user
	else :
		delay_print ("Are you sure you typed in the right words? Try again.........")
		sandwichbase ()

def showhunger () : #function that shows your hunger level in the end
	global hungerlevel
	hungerlevel = str (hungerlevel)
	input ("Your hunger level is "+hungerlevel+" now. [Press Enter]")

def salad() :
	clear ()
	input ("Feeling healthy, huh? [Press enter]")
	saladbase()
	delay_print ("Phew. Now you get to choose your toppings......         ")
	meatchoice ()
	topping () 

def sandwich ():
	clear ()
	delay_print ("You're pretty hungry, aren't you?         ")
	sandwichbase ()
	input ("Now you get to choose what to put inside. [Press enter]")
	meatchoice ()
	topping()

def system () :
	clear ()
	start ()
	delay_print ("What do you want to make?")

	loop = 1
	while loop == 1: #will make the user try again until they enter either salad or sandwich
		recipe = input (" \nYou can make a salad (decreases hunger level by 2-7) or a sandwich (decreases hunger level by 5-10). \n  Enter salad or sandwich: ")

		if str.lower(recipe) == "salad":
			salad ()
			loop = 0
		elif str.lower(recipe) == "sandwich":
			sandwich ()
			loop = 0
		else :
			print ("I don't really know how to make "+recipe+"...")
			loop = 1	

	clear ()
	delay_print ("Yumyumyumyumyumyum........................")
	input ("You enjoyed your "+recipe+"! [Press Enter]") 
	clear ()
	showhunger ()
	clear ()
	if  -2 <= int (hungerlevel) <= 2 : #if the hunger level is in the right range
		delay_print ("You have successfully satisfied your hunger! Congrats!")
		delay_print ("\n      _.-'''''-._\n    .'  _     _  '.\n   /   (o)   (o)   \ \n   |               |\n   |  \         /  |\n    '.  `'---'`  .'\n      '-._____.-'                            The End.")
	elif -2 >= int (hungerlevel) : #if the hunger level is too low=too full
		delay_print ("Oops... I think you ate too much. You're feeling kinda gross. Be careful next time!\n")
	elif 2 <= int (hungerlevel) : #if the hunger level is still too high =still hungry
		delay_print("Oops... I think you ate too little. You're still hungry...")
		tryagain = input ("\n Do you want to try again? \n Enter yes or no:")
		if str.lower(tryagain) == "yes" :
			input ("I like your guts! Let's play again! [Press enter to continue]")
			system ()
		elif str.lower(tryagain) == "no":
			input ("Oh well. I will see you next time.")
		else :
			print ("Huh?  I don't know what you just said. Whatever. babai.\n                                         The end.")	

system ()

	





