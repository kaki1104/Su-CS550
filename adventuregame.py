#Kaki Su
#September 17, 2018
#Description: 
#sources: 
#Honor code: I have neither given nor received unauthorized aid.


input ("you are very hungry......")
input ("you want to make some food for yourself...")


def menu () :
	recipe = input ("What do you want to make? You can make salad, steak, or pasta.")

	if recipe == "salad" :
		salad ()
	elif recipe == "steak" :
		input ("hmmm.. you're feeling really hungry, aren't you?")
			#steak ()
	elif recipe == "pasta" :
		input ("okay, you're lazy, I get it.")
			#pasta ()
	else :
		print ("I don't really know how to make "+recipe+"...")
		menu ()

def cutting () :
	cut = input ("now you have to cut them by hitting c on the keyboard five times, quickly!")
	cut = str(cut)
	if cut == "ccccc" :
		 print ("okay, good. let's move on.")
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

def saladtopping () :
	topping = input ("Do you want toppings? Type yes or no.")
	if topping == "yes" :
		toppings = input ("Let's see what you have in the fridge... You have tomato, cucmber, avocado, onion, carrot, tofu, bacon.")
	elif topping == "no" : 
		input ("wait, but you're still going to be super hungry...")
		saladtopping ()
	else :
		input ("Please type yes or no.")
		saladtopping()




def salad() :
	input ("feeling healthy, huh?")
	saladbase()
	input ("Phew. now you get to choose your toppings.")
	saladtopping ()


menu()


	





