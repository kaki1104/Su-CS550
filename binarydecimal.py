
import sys
n = float (sys.argv[1])


def todecimal (bi):
	to_return = 0
	for i, num in enumerate (bi[::-1]): #:: takes and reverses list #enumerate 
		to_return += int (num) *2 **i
	return to return

def rec_fib (n):
	if n== 0 or n==1:
		return 1
	return rec_fib (n-1) + rec_fib (n-2)