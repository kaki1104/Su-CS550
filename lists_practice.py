''' Instructions:
   Work with a partner to complete these tasks. Complete as many as you can. Assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''

favenums = [1,1,1]

''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''

holidays = ["Christmas", "Thanksgiving", "Easter", "New Year", "Hannukah", "Kwanza", "Labor Day", "Memorial Day", "Valentines Day", "Columbus Day", "Independence Day", "Veterans Day", "George Washington's birthday", "Inaugration Day"]

''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''

grades = [A,B,C,D,F]

''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
funny = [[True]* 9 + [False] * 9]


''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''

salaries[10.12,15.23,50.34,19.34,32.89]
numEmployees = len(selaries)

''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''

l = []
for i in range (x) :
   for j in range (y):
      l.append (value)


''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''

names = [x for x in range(0,noSiblings+2*oneSibling+3*twoSiblings+4*threeSiblings)]

''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''

months = ["January", "February", "March", "April", "May", "June", "July",
 "August", "September", "October", "November", "December"]

''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''

week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
l = [True, False]


''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''

dorms = ["Memorial","Nichols","Squire","Pitman"]

''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
import random
l = []
n = 0
while n < 3 :
   l.append(random.choice(range(0,100))/100)
   n = n +1


''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''

cards = [x for x in range(0,52)]
for y in range(1,5)
   for x in range(2,15):
      if y == 1:
         cards[x*y-1] = str(x)+"S"
      if y == 2:
         cards[x*y-1] = str(x)+"H"
      if y == 3:
         cards[x*y-1] = str(x)+"D"
      if y == 4:
         cards[x*y-1] = str(x)+"C"
      if x == 11:
         cards[x*y-1].remove(x)
         cards[x*y-1].insert(0,"J")
      if x == 12:
         cards[x*y-1].remove(x)
         cards[x*y-1].insert(0,"Q")
      if x == 13:
         cards[x*y-1].remove(x)
         cards[x*y-1].insert(0,"K")
      if x == 14:
         cards[x*y-1].remove(x)
         cards[x*y-1].insert(0,"A")


''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
a = b = c =d =e = [1, 2, 3, 4, 5, 6,]
if random.choice(a) == random.choice(b) == random.choice (c) == random.choice (d) == random.choice(e) :
   print ("Yahtzee")
else :
   print ("Try Again.")

''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''

for x in range(0,len(numbers)):
   if (numbers[x]//10)%2 == 0 and (numbers[x]%10)%2 == 1 and numbers%3 == 0:
      print("Position "+str(x)+" "+str(numbers[x-1])+" "+str(numbers[x])+" "+str(numbersx+1]))

''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
from random import randint


l = [[randint (0, 25) for x in range(5)] for y in range(5)]
for x in range (5) :
   for y in range (5) :
      if l [x][y] == max (l[x]) and l[x][y] == min (l[y]) :
         print (x, y)

''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''

board = [[] for x in range(0,8)]
board[x] = [0 for x in range(0,8)]
board[row1+1][col1+1] = 1
board[row2+1][col2+1] = 1
if row1 == row2 or col1 == col2:
   attacking = True
for x in range(0,8):
   if row1-x == row2 and col1-x == col2:
      attacking = True
   if row1+x == row2 and col1+x == col2:
      attacking = True

''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
l=[]
   for x in reversed(l):
      print(l)


''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''

temp = doorknobs[3]
doorknobs[3] = doorknobs[1]
doorknobs[1] = temp

''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''

import random
number = []
for x in range (10):
   number.append (random.randrange (1, 101))

ma = max (number)
number.remove(ma)
number.append (ma)


''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''

array = [[] for x in range(0,w)]
array[x] = random.randInt(1,101) for x in range(0,h)
for x in range(0,w):
   for y in range(0,h):
      if array[x][y]%2 == 1:
         if len(array[x][y]) == 2:
            array[x][y] = 22
         else:
            array[x][y] = 2

''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

l = []
for x in range (w) :
   for y in range (h):
      l.append (value)
      l[x][y] = 255 - l[x][y]


''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''



''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
from random import randint

l = [[randint (0, 101) for x in range(N)] for y in range(N)]
n = 0
for y in range (N) :
  for x in range (N) :
   if l[x][y] > l[x+1][y] and l[x][y] > l[x-1][y] and l[x][y] > l[x][y+1]and l[x][y] > l[x][y-1] :
      n = n + 1
   else:
      pass

 print (n)

 

''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
for x in range(0,len(rankings)):
   sum += rankings[x]
average = sum/len(rankings)
sum = 0
for x in range(0,len(rankings)):
   if rankings[x] > average:
      sum += 1
percentage = sum/len(rankings)



''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''

from random import randint

N = 3 
l = [[randint (1, N) for x in range(N)] for y in range(N)]
for y in range (N) :
  for x in range (N) :
    print (l[x][y],end=" ")
  print("")

n = [1,2,3]

for y in range (N) :
   print (all(x in l[y] for x in n) == True )
for x in range (N) :
   print (all(y in l[x] for y in n) == True )

#doesn't work

'''
   27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''

numbers = [random.randInt(1,11) for x in range(0,100)]
for z in range(0,100):
   for y in range(1,11):
   {
      counter = 0
      for x in range(0,100):
         if numbers[x] == y:
            counter += 1
      newList[y-1] = counter
   }
   averages[z] = averages[z] + newList[y-1]
averages[z] = averages[z]/100
print(*averages)



''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''