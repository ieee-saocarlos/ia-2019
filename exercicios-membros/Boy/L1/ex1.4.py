N= input('Digite um valor:') #Se quiser pode ser 600851475143
N=int(N)
i =0
mp=0
while 0 <= i <=N:
    c=0
    j=2
    while j < i :
        if (i%j!=0):
            c = c+1
        j=j+1
        while(N%i==0 and i == c+2):
             N= N/i
             mp=i

    i= i + 1
print(mp)
