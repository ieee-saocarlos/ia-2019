import random
n = random.randint(20,50)
print(n)
i=0
Alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Lista=[]
while(i<n):
    Lista.append(random.choice(Alfabeto))

    i=i+1
Lista.sort()
print(Lista)
i=0
ind=[]
while (i<26) :
    ind.append(Lista.count(Alfabeto[i]))
    i=i+1
i=0
j=0
mr=0
n=0
print(ind)
while(i<26):
    while(j<26):
        if(ind[j]>=ind[i] and ind[j]>mr):
            mr=ind[j]
            print(mr)
            n=j
        j=j+1
    i=i+1
m=[[mr,Alfabeto[n]]]
for c in range(0,26):
    if(ind[c]== mr and c!=n):
        m.append([mr,Alfabeto[c]])
print(m)






