import random

m = 0
l = [0,0,0,0,0,0,0,0,0,0,0]
while m < 1000 :
	n = 0
	s = 0
	while n < 10 :
		r = random.choice((0, 1))
		s = s + r
		n = n + 1
	l[s] = l[s] + 1
	m = m + 1

print (l)

