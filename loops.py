# loops.py

# num = int(input("Pick a number between 1 and 5"))

# while num<1 or num>5:
# 	num = int(input("This number is not in the right range."))

# print ("success!")

# def check (choice, a, b)
# 	while choice != and choice != b 
# 		choice= input ("please choose "+a+" or "+b+"")
# 		return choice

while True :
	try:
		num = int(input("Pick a number between 1 and 5."))
		while num<1 or num>5:
 			num = int(input("This number is not in the right range. enter a number between 1 and 5."))
 			break #breaks immediate loop
	except ValueError :
		print ("That's not a number. Try again.")

print ("success!")
