from math import floor


def digitos(x):
    digitos = list()
    while x>=1:
        k=x%10
        x=floor(x/10)
        digitos.append(k)
    return digitos


def fatorial(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*fatorial(x-1)


def test(max):
    n = list()
    for c in range (3,max+1):
        k = digitos(c)
        s = 0
        for d in range (len(k)):
           s += fatorial(k[d])
        if(s == c):
          n.append(c)
    return n


def somaDelista(lis):
    s=0
    for c in range (len(lis)):
        s+=lis[c]
    return s

lista=test(1000000)
print(lista)#[145, 40585]
print(somaDelista(lista))#40730

