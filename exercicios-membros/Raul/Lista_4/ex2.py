from random import *

a = 3
b = 4
c = 5
loop = 1

while loop == 1:
    if a + b + c == 1000:
        print (a,b,c) # 375, 200, 425
        resp = a * b * c
        loop = 0
    else:
        a += 1
        while (a**2) + (b**2) != (c**2):
            a = randint(4,500)
            b = randint(5,500)
            c = ((a**2) + (b**2)) ** 0.5


print (resp) # 31875000