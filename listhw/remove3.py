import random
import math

l = []
for x in range (10) :
	l.append(random.randrange (101))
print ("original: ",l)

for x in l:
    if x % 3 == 0:
        l.remove(x)

for x in l: #when only performed once, there only some of the numbers divisible by 3 was taken away, and some remained on the list for unknown reason. By performing the function twice, there were no mistakes observed anymore.
    if x % 3 == 0:
        l.remove(x) 

l.sort()
l.reverse ()
print ("modified: ",l)
