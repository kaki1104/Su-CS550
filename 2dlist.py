
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #three lists in a list

print (l [0][0]) #prints first number in the first list
print (l [1][0]) #prints first number in the second list

#list with ten 0s
m = []
for x in range (10) :
	m.append (0)
print (m)
#short cut:
n = [0]*10
print (n)

#2D list 
o = []
for x in range (10) :
	p = [0] * 10
	o.append (p)
print (o)
#alternative
q = [[0]*10 for x in range (10)]
print(q)
#make it so that theres only one list in a row, more organized
for x in range (len (q)) :
	print (*q[x]) #adding * will take away the brackets