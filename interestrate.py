
import math
import sys

t = sys.argv[1] 
P = sys.argv [2]
r = sys.argv [3]

value = float(P) * float(math.e) ** ((float(r)/100) * float(t))

print (value)