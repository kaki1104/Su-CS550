import random
import matplotlib.pyplot as plt

totaltry = 1000
totalplay = 100

results = []
for j in range (totaltry) :
	total = 0
	for i in range (totalplay):
		flip = random.randint (1,100)
		if flip == 1 :
			total += flip
	results.append (total)

display = [0 for i in range (10)]
for i in range (len (results)):
	display[results[i]] += 1

r = [x for x in range (10)]


plt.bar (r, display, color = (.5, 0., .5, 1.))
plt.ylabel ("Percentage of fifty-fifty")
plt.xlabel ("Number of Flips")
plt.title ("How probable is fifty-fifty?")
plt.show ()