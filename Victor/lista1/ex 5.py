s=0
x=0
b=1
c=1
while x <= 4000000:
    if x%2==0:
        s=s+x
    x=b+c
    b=c
    c=x
print(s)


