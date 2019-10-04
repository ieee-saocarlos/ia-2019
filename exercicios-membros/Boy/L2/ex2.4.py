import math
lista=[15,9,-3,7,99,-3,0,-5,8,15,-6,-3,99,15,0,15]
cres=[]
cressemr=[]
cressemrpar=[]
cressemrimpar=[]
semr=lista[:]
decressemr=[]
vez=[]
m=math.inf
M=-m
for c in range (0,16):
    if(lista[c]>M):
        M=lista[c]
    if(lista[c]<m):
        m=lista[c]
for c in range (m, M+1):
    for q in range(0,16):
        if(c == lista[q]):
            cres.append(c)
print('a)',cres)

for c in range (0,16):
    w=0
    for q in range (0,len(semr)):
        if(lista[c]==semr[q]):
            w+=1

    while(w>1):
        semr.remove(lista[c])
        w-=1


for c in range (M, m-1,-1):
    for q in range(0,len(semr)):
            if(c == semr[q]):
                decressemr.append(c)
print('b)',decressemr)
for c in range (m, M+1):
    for q in range(0,len(semr)):
        if(c == semr[q]):
            cressemr.append(c)

for c in range (0,len(semr)):
    if(cressemr[c]%2==0):
        cressemrpar.append(cressemr[c])
    if(cressemr[c]%2!=0):
        cressemrimpar.append(cressemr[c])

print('c par)',cressemrpar )
print('c impar)',cressemrimpar )

for c in range(len(semr)):
    g=0
    for d in range(len(lista)):
        if(semr[c]==lista[d]):
            g+=1
    vez.append([semr[c],g])


print('d)',vez)

