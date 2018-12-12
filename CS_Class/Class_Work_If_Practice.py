## Class_Work_If_Practice
## December 12, 2018
## Working with a partner to complete various tasks.
## Eilidh & Jiaqi


''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if (variableGrade == "A"):
  print("Good Work.")
 
 
''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
 if int(yard) < 17 :
 	yard = yard * 2
 
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if (success == True):
  print("Congradulations!")
 
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
 if word[:2] = "f" :
 	print ("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
if (celcius == True):
  ## Convert to farenheit
  temp = (1.8 * temp) + 32
 
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
 
 averageCost = int(totalCost)/numItems
 if numItems <= 0 :
 	print ("no items")
 
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
''' 
if (pollution < cutoff):
  print("Safe condition.")
else:
  print("Unsafe condition.")


''' 8.
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
 
 if 90 <= score <= 100 :
 	grade = "A"
 elif 80 <= score <= 89 :
 	grade = "B"
 elif 70 <= score <= 79 :
 	grade = "C"
 elif 60 <= score <= 69 :
 	grade = "D"
 elif score <= 60 :
 	grade = "F"
 
''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
if (letter.isdigit()):
  print("Digit.")
elif (letter.isalpha()):
  if (letter.lower() == letter):
    print("Lowercase.")
  else:
    print("Uppercase.")
else:
  print("Symbol.")
 
 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
if neighbors >= 50 :
	residence = "city"
elif neighbors >= 25 :
	residence = "suburbia"
elif neighbors >= 1 :
	residence = "rural"
elif neighbors == 0 :
	residence = "middle of nowhere"
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
if (doesSignificantWork == True) and (makesBreakThrough == True):
  nobelPrizeCandidate = True
else:
  nobelPrizeCandidate = False
    
 
 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
 if tax == True :
 	price = price * (1+taxRate)
 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
if (word[-2:] == "ly"):
  type = "Adverb"
elif (word[-3:] == "ing");
  type = "Gerund"
elif (word[-1:] == "s"):
  type = "Plural"
else:
  type = "Error"
 
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
 if currentNumber % 2 == 0 :
 	currentNumber = currentnumber * 3 + 1
 else :
 	currentNumber = currentNumber / 2
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
if (year % 4 == 0):
  leapYear = True
  if (year % 100 == 0) and (year % 400 == 0):
    leapYear = True
  else:
    leapYear = False
else:
  leapYear = False
 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
 
l = [a, b, c]
result = min (l)

''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if (int % 2 == 0) and (int % 5 == 0) and ((-100) <= int <= 100):
  special = True
else:
  special = False
 
 
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
 
for char in letter :
	if char == "a" or char == "e" or char == "o" or char == "u" or char == "i" :
		code = code + 1
	elif char == "y":
		code = code - 1
	else: 
		pass
 
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
if (dayOfWeek[3:] == "sun") or (dayOfWeek[3:] == "sat"):
  isWeekend = True
else:
  isWeekend = False
 
 
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
 
if month == ("January" or "March" or "May" or "July" or "August" or  "October" or "December") : 
	numDays = 31
elif month == "Feburuary" :
	numDays = 28
else :
	numdays = 30


 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
if (angle1 + angle2 + angle3 == 180):
  validTriangle = True
else:
  validTriangle = False
 
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
 if electricity <= 50 :
 	payment = 50 * electricity
 elif electricity <= 150 :
 	payment = 250 + 75 * (electricity-50)
 elif electrcity <= 250 :
 	payment = 1000 + 120 * (electricity-150)
 else :
 	payment = (2200 + 150 (electricity - 250)) * 1.2
 
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
if (language == "English"):
  greeting = "Hello"
elif (language == "French"):
  greeting = "Bonjour"
elif (language == "Spanish"):
  greeting = "Hola."
else:
  greeting = "Sup Dude."
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes'''


import random

list1 = [1, 2, 3, 4, 5]
number = random.choice(list1)
list2 = ['dog', 'cat', 'elephant', 'human', 'home']
noun = random.choice(list2)
phrase = str(number) + " " + str(noun)
  
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
if (userInput == "bacon"):
  print("Why did you type bacon?")
else:
  print("I like bacon.")
 
 
''' 26.
	If a string, verb, contains the letters "ing", print "I am (verb)."
'''

if "ing" in verb :
	print ("I am " + verb + ".")

##