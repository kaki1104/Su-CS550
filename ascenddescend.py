#September 12, 2018
# This program will tell you if the three values entered in the command line is either strictly ascending or decending.
#Sources: http://thomas-cokelaer.info/tutorials/python/boolean.html
#		  https://linuxconfig.org/python-boolean-operators

import sys 
x = sys.argv[1] 
y = sys.argv [2]
z = sys.argv [3]

truth = (float(x)<float(y)<float(z)) or (float(x)>float(y)>float(z))
print (truth)