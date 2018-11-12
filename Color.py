# Python program to print colored text and background 
def Red(skk): 
	print("\u001b[31m {}\u001b[0m" .format(skk)) 
def Green(skk): 
	print("\u001b[32m {}\u001b[0m" .format(skk)) 
def Yellow(skk): 
	print("\u001b[33m {}\u001b[0m" .format(skk)) 
def Blue(skk): 
	print("\u001b[34m {}\u001b[0m" .format(skk)) 
def Black(skk): 
	print("\u001b[30m {}\u001b[0m" .format(skk)) 


Print ("This is "Black("black")" and "Blue("blue")" and "Yellow("yellow")" and "Green("green")" and "Red("red")" haha." )