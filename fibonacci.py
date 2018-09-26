#fibonacci.py

import sys
n = float (sys.argv[1])

def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 1            
   else:                      
      return fib(n-1) + fib(n-2)      

for n in range (0,int(n+1)) :
 	print (fib (n))
