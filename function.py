#function.py
#lesson on python function

#def greetings (someone) :
	#print ("Hello", someone)

#greetings ("Alex")
#greetings ("Daniel")
#greetings ("a")
#greetings (True)


def start ():
	input ("You are here to save the princess!")
	input ("She has been kidnapped by Bowser and Bowser Jr.")
	result = input("type 1 to save the princess or \ntype 2 to turn back.") #do multiple inputs if you want the user to enter for every sentence
	if result =="1":
		savePrincess()	
	elif result == "2":
		shame()
	else:
		print ("I don't know what that "+result+" means. Please type 1 or 2.")
		start()

def savePrincess():
	direction=input ("choose left or right.")
	if direction == "right":
		print  ("oops, there is a bear.")
	elif direction == "left":
		print ("hmmm.... This route is oddly peaceful.")
	else:
		print ("I don't know what that "+direction+" means. Please type right or left.")
		savePrincess()


def shame():
	print ("Wow, you are clearly a coward.")
start() 

