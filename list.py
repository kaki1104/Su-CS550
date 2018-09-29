import random as r

# #empty list
a = []

 #add something to list
a.append (4) 
a.append (5)
a.append (3)
a.insert (2,1)
a = [2] + a

#print (a [0], a[4], a[7])

print(a)

b= [1, 1, 4, 5, 3]
b.remove (4)
print (b)

del b[0]
print (b)

print (b.pop())
print (b)

#last thing in the list
print (b[len(b)-1]) 
print (b[-1]) #shortcut

c = 5 
d = 7
c, d = 5, 7
c, d = d, c #swap


e= [1,2,3,7,5,6,4]

e [3], e[6] = e[6], e[3]

f =[]
for x in range (1, 701, 7): #(start, stop, step)
	f.append (x)

print (f)
print (len(f))

g=[]
for x in range (10) :
	g.append(r.randrange (100))

g.sort()
print (g)
print (sorted(g)) #same thing

