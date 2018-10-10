
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

def main():
    n = int(sys.argv[1])
    moves(n, True)

main ()

#The program takes the n from the user input. It moves the top n-1 discs to an empty pole. Then it moves the largest disc to the other empty pole, and then it finishes the job by moving n-1 discs onto the largest disc. 
#Say the input is 3. First, it loops through the moves function, continuously simplifying it until it reaches the smallest n (=1). Since it loops through it twice, it becomes right and then back to left. Then it continues to 