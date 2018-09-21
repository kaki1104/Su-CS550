def cutting () :
	from timeit import default_timer as timer
	input ("now you have to cut them by hitting c on the keyboard five times and hit enter. ready....")
	start = timer()
	cut = input ("go!")
	end = timer ()
	if cut == "ccccc" :
		if float(end - start) <= 3 :
			print ("okay, good. let's move on.")
		else :
			print ("oops, you were a little clumsy. The cutting wasn't good enough.")
			cutting ()
	else : 
		 print ("You didn't cut it the right way. Try again.")
		 cutting()

cutting ()