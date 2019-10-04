i=0
a=0
b=1
s=0
while i==0:
    F=a+b
    a=b
    b=F
    if(F>4000000):
        i=1
    if(F%2==0):
        s=s+F
print(s)