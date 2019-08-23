import math
x=int(input('Enter the number \n'))
a=int(math.sqrt(x))
if a*a==x:
    print("Perfect Number")
else:
    print("Not Perfect")