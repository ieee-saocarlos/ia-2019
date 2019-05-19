inicio=[1,2,3,4,5,6,7,8,9,10]
par=[]
impar=[]
inverso=[]
primos=[]
divisores=[]
n=0
print(inicio)
#lista par e impar
for x in range (10):
    if (inicio[x]%2==0):
        par.append(x)
    else:
        impar.append(x)
print(par)
print(impar)
#inverso
for x in range (9,-1,-1):
    inverso.append(inicio[x])
print(inverso)
#primo
for x in range (10):
    for y in range (1,inicio[x]+1):
      if (inicio[x] % y == 0) :
       divisores.append(x)
       n=len(divisores)
    if n==2:
       primos.append(inicio[x])
    divisores.clear()
    n=0
print(primos)