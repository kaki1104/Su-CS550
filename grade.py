#September 15, 2018
#This program will tell you the corresponding grade when you enter a number ranging from 0 to 5.

import sys
value = float (sys.argv[1])

if value < 0 or value > 5 :
	print ("Please enter a number between 0-5.")

elif value >= 4.85 :
	print ("A+")

elif value >= 4.7 :
	print ("A")

elif value >= 4.5 :
	print ("A-")

elif value >= 4.2 :
	print ("B+")

elif value >= 3.85 :
	print ("B")

elif value >= 3.5 :
	print ("B-")

elif value >= 3.2 :
	print ("C+")

elif value >= 2.85 :
	print ("C")

elif value >= 2.5 :
	print ("C-")

elif value >= 2 :
	print ("D+")

elif value >= 1.5 :
	print ("D")
else :
	print ("I think you failed...")

