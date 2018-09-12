#September 12, 2018
#This program calculates effective temperature when user puts in temperature and velocity in the command line
#sources: none

import sys 
temperature = sys.argv[1] 
velocity = sys.argv [2]

windchill = 35.74 + 0.6215*float(temperature) + (0.4275*float(temperature) - 35.75) * float(velocity)**0.16
print ("The wind chill is "+str(windchill)+" degrees Farenheit")
