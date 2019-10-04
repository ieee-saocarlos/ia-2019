import math
s=0
for x in range (1,1000):
    t=x**x
    s=s+t
    z=int(math.log10(t))
print(z)
