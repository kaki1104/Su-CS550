#Kaki Su
#September 26, 2018
 
import random
import math

l = []
for x in range (10) :
	l.append(random.randrange (101))
print ("original: ",l)

for x in l:
    if x % 3 == 0:
        l.remove(x)

l.sort()
l.reverse ()
print ("modified: ",l)
