#recursion.py

def add (x,y) :
	return x+y

print (add (5,6)) #will print 11


def fact (n) :
	if n is 0 or n is 1:
		return 1
	else: 
		return n*fact(n-1)

print (fact (3))


def count (text) :
	num = 0
	for char in text :
		if char == "x" :
			num = num + 1
	return num
print (count("xxxxx"))

def crazy_eights (text):
	num = 0
	for char in text :
		if char == "8" :
			num = num + 1
	return num

print (crazy_eights("x888x8xx"))

def euclid (a,b) :
	c = int (a % b)
	b % c

print (euclid (100, 40))
