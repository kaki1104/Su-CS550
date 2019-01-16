import random


m = 0
walkhome = 0

while m < 10000:
	n = 0 
	place = [0, 0]
	while n <= 22 :

		direction = [[1,0], [0,1], [-1,0], [0,-1]]
		d = random.choice (direction)
		place = [(place[0] + d[0]), (place[1] + d[1]) ]
		n = n + 1

	distance = abs (place[0]) + abs (place [1])
	if distance <= 4 :
		walkhome = walkhome + 1
	m = m + 1

print (walkhome)


#print ("Your distance from home is " + str (distance) )