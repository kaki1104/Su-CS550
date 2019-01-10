#19: after simulating the walks using the code from the in-class work, it seemed that it was the best. 
#Monte Carlo simulation allows the decision-maker to see a range of  possible outcomes and probabilities that will occur as a result of their action. It include extreme possibilities to allow for better decision making.

#imagine you are throwing darts at a square dartboard, which has a circle perfectly inscribed in the square. Let's say the location of the center of the dartboard is 0,0, and the side length of the square is 2, giving the circle a radius of 1. Keep track of the number of times that your dart lands within the circle in 100 tries. Now, multiply that number by 4, and divide by the number of darts you threw. What value do you get? Repeat the simulation, but with 1000 darts... and 10,000 darts... and 100,000 darts. What do you notice about the output?

import random
import math

n = 0
c = 0

while n <= 100000 :
	x = random.uniform (-1, 1)
	y = random.uniform (-1, 1)

	if math.sqrt (x ** 2 + y ** 2) <= 1 :
		c = c + 1
	n = n + 1

print (c) #number of times the dart lands in the circle. about 78.6 percent?
print (c * 4 / n) #gets pi !
#the outcome gets narrower as we repeat the simulation with more tries, and pi also gets more accurate.