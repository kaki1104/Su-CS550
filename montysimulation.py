#Kaki Su
#January 7, 2019
#I think that it does not matter because either way a pennie slot will be revealed and you have no means to tell anything apart based on that reveal.

import random

l = ["car" ,"penny", "penny"]
w = 0
n = 0

#when you don't switch
while n < 1000 :

	l = ["car" ,"penny", "penny"]
	r = random.choice(l) #0 will be the car key, 3 and 2 will be the pennies
	l.remove ("penny")
	if r == "car" :
		w = w + 1 
	n = n + 1

print (w)
#result: you win the car roughly 1/3 of the time

#when you switch
w = 0
n = 0
while n < 1000 :

	l = ["car" ,"penny", "penny"]
	r = random.choice(l) #0 will be the car key, 3 and 2 will be the pennies
	l.remove (r)
	l.remove ("penny")
	if l[0] == "car" :
		w = w + 1
	n = n + 1

print (w)
#you win the car roughly 2/3 of the time.
#This actually makes sense, because if you don't change after revealed the possibility of winning the car remains 1/3. But if you did switch after a penny is revealed, the only scenario where you will not get the caris when your original choice was the car, so the possibility of getting the car will be 2/3. 
