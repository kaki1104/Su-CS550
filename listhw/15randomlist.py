import random

l = []
for x in range (15) :
	l.append(random.randrange (101))

print (l)

loop = 0
while loop == 0 :
	num = int(input ("\nChoose a number from 0-100:  "))
	
	if num < 0 or num > 100 : 
		print ("Invalid number.")
		loop = 0
	else: 
		l.append (num)
		loop = 1

l.sort()
l.reverse ()
print (l)
