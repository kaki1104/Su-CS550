
#calculates windspeed when user puts in temperature and velocity in the command line

import sys 
temperature = sys.argv[1] 
velocity = sys.argv [2]

windspeed = 35.74 + 0.6215*float(temperature) + (0.4275*float(temperature) - 35.75) * float(velocity)**0.16
print (windspeed)
