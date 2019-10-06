num = [1,2,3,4,5,6,7,8,9,10]
pares=[]
impares= []
reversa=[]
primos=[]
for c in range(0,10):
    if (num[c] % 2 == 0):
      pares.append(num[c])
print(pares)
for c in range(0,10):
    if (num[c] % 2 != 0):
      impares.append(num[c])
print(impares)
for c in range(0,10):
      reversa.append(num[9-c])
print(reversa)
for c in range(0,10):
    z=0
    j=2
    while (j<num[c]):
        if(num[c]%j==0):
            z+=1
        j += 1
    if (z == 0 and num[c] != 1):
        primos.append(num[c])

print(primos)

