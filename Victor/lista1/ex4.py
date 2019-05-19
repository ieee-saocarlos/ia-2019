import math
lista=[]
lista_2=[]
x=600851475143
y=(x//2)
ln=len(lista)
for i in range (y,1,-2 ):
    if (x%i==0):
     for t in range (2,i):
        if (i % t == 0) :
            lista.append(i)
            ln = len(lista)
     if (ln==0):
      lista_2.append(i)
      print(lista_2[0])
      ln2 = len(lista_2)
      if (ln2==0):
         print(x,"é primo")
lista.clear()


