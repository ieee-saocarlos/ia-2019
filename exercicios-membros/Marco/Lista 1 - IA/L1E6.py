# Exercicio 6 - Lista 1 : determine qual letra mais se repete e quantas vezes essa letra se repetiu dentro da Lista

import random
letras =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l1=[]
a=0
c=0
repetidas=[]
for i in range(random.randint(20,51)):
   l1.append(random.choice(letras))
print("A lista criada, foi:",l1)
for j in range(len(l1)):
       if l1[0]==l1[j]:
           a=a+1
           b=l1[0]
repetidas.append(b)
for i in range(len(l1)):
  for j in range(len(l1)):
    if l1[i]==l1[j]:
      c=c+1
      d=l1[i]
      if (c==a):
        repetidas.append(d)
        a=c
      elif (c>a):
        repetidas.clear()
        repetidas.append(d)
        a=c
  c=0 

set_1=set(repetidas)


print ("Numero de repeticoes:",a)
print("Letras repetidas :",set_1)