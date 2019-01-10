import random
import matplotlib.pyplot as plt

results = []
for j in range  (1000) :
	total = 0
	for i in range (10):
		flip = random.randint (0,1)
		total += flip
	results.append (total)

display = [0 for i in range (11)]
for i in range (len (results)):
	display[results[i]] += 1

r = [x for x in range (11)]
d = [x for x in range (11)]

plt.bar (r, display, color = (.5, 0., .5, 1.))
plt.ylabel ("Number of Trials")
plt.xlabel ("Number of Heads")
plt.title ("Bell Curve")
plt.show ()