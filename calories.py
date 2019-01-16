"""import random
import math

n = 0
a = 

while n <= 1000 :

	parties = random.randint (0, 8)
	calories = random.randint (50, 500)
	servings = random.randint (1, 30)

	r = parties * calories * servings

	if 0 < r < 10000

print (r)"""

import random
import matplotlib.pyplot as plt

num_parties = random.randint (0, 8)
calories = random.randint (50, 500)
servings = random.randint (1, 30)

results = []
for k in range  (10000) :
	num_parties = random.randint (0, 8)
	total_calories = 0
	for j in range (num_parties) :
		cookies = random.randint (1,30)
		for i in range (cookies):
			calories = random.randint (50, 300)
			total_calories += calories
	results.append (total_calories)

display = [0 for i in range (10000)]
for i in range (len (results)):
	display[results[i]] += 1

r = [x for x in range (cookies)]
d = [x for x in range (cookies)]

plt.bar (r, display, color = (.5, 0., .5, 1.))
plt.ylabel ("Number of Trials")
plt.xlabel ("Number of Heads")
plt.title ("Bell Curve")
plt.show ()