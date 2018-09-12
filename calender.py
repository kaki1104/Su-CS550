

import sys 
month = sys.argv[1] 
day = sys.argv [2]
year = sys.argv [3]

y0 = int(year) - int((14 - int(month)) / 12)
x = y0 + int(y0/4) - int(y0/100) + int(y0/400)
m0 = int(month) + 12 * int((14 - int(month)) / 12) - 2
result = (int(day) + x + (31*m0) / 12) % 7

print (int(result))