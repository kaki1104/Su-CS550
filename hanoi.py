
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

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

def main():
    n = int(sys.argv[1])
    moves(n, True)

main ()