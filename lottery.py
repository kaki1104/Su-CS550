#Kaki Su
#January 15, 2019
#This code seeks to simulate the optimal decision to make the most money out of $200 with lottery.
#I chose to set the price at $2 because many lottery tickets in real life is that price, and set the prize 100 times the ticket value while the percentage of winning that prize at 1/100. I was curious what would happen if you would get the money back theoretically. I thought that in real life, people face many similar dilemmas in dealing with theoretical values because situations like gambling blinds people's judgements and "intuitions".
#I have neither given nor received unauthorized aid. Jiaqi Su


import random

# simulation 1 

m = 0
l = [0, 0]
lose = 0
prize = 200

while m < 1000:
	n = 0
	money = 200
	while n < 100 :
		win = random.randint (1, 100)
		r = random.randint (1, 100)
		money = money - 2
		if r == win :
			money = money + prize
		n = n + 1

	if money <= 0 :
		lose = lose + 1

	m = m + 1


print (lose)



#Simulation 2

l = [0,0,0]
p = 0

while p < 1000 :
	n = 0
	while True :
		win = random.randint (1, 100)
		r = random.randint (1, 100)
		n = n + 1
		if n <= 30 :
			if r == win :
				l[0] = l[0] + 1
				break
		elif 30 < n <= 100 :
			if r == win :
				l[1] = l[1] + 1
				break
		elif n > 100 :
			if r == win :
				l[2] = l[2] + 1
				break
	p = p + 1



print (l)



#simulation 3 


prize = 200
m = 0
total = 0

while m < 1000 : #repeat the simulation 1000 times
	n = 0
	money = 200
	while n < 100 : #even if we change n, the result does not change!
		win = random.randint (1, 100)
		r = random.randint (1, 100)
		n = n + 1
		if r == win :
			money = money + 200
			break
		else :	
			money = money - 2
	total = total + money
	m = m + 1
	
print (total/1000) #returns the average money you ended up with after 1000 simulations



