
import sys

def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        print(str(n) + ' left')
    else:
        print(str(n) + ' right')
    moves(n-1, not left)

#def main():
#    n = int(sys.argv[1])
n = 3
moves(n, True)

#main ()

#The program takes the n from the user input. It moves the top n-1 discs to an empty pole. Then it moves the largest n disc to the other empty pole, and then it finishes the job by moving n-1 discs onto the largest disc. 
#Say the input is 3. First, it loops through the moves function, continuously simplifying it until it reaches the smallest n (=1). 
#When n= 1, the function produces "1 left" becasue the two recursive funtions in the definition both produces nothing and returns since n-1 = 0, and the if statement in the middle will produce "1 left" since n=1 and left is true. 
#When n=2, the two recursive functions will each produce 1, right because it takes the function for n-1 (which in this case is 1) and reverses the right/left. The middle if statement produces "2 left" because n=2 and left is true. 
#Thus, when n=3, the two recursive functions each produces the results when n=2, which is "1 right, 2 left, 1 right". The middle if statement  will simply give "3 left" becuase n =3 and left is true. Thus, the result if "3 left" in the middle of two sets of "1 left, 2 rgith, 1 left"