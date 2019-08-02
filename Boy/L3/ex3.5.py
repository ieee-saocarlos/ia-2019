#EX.:
'''Faça um programa que calcule (por meio de funções):
A diferença entre os fatoriais de dois números, sendo:
num1 = 3;
num2 = 7.
O produto interno(*produto escalar) dado dois vetores (listas), sendo:
lista1 = [13,52,75,12,8];
lista2 = [6,87,1,54,-6].
A raiz quadrada de dois números (até a 3ª casa decimal) sendo:
num1 = 43;
num2 = 98.
O logaritmo de um número em uma base, sendo:
num = 876;
base = 34.
'''

#Programa

import math

def fatorial(n):
    if(n==0):
        return 1
    else:
        return n*fatorial(n-1)


def subFat(n1,n2):
     return fatorial(n1)-fatorial(n2)


def  prodEsc(vet1,vet2):
    S=0

    if(len(vet1)<=len(vet2)):
        x=len(vet1)
    else:
        x=len(vet2)
    for c in range(x):
        S+=vet1[c]*vet2[c]
    return S

def raizes(n1,n2):
    lRaizes=[round(math.sqrt(n1),3),round(math.sqrt(n2),3)]
    return lRaizes


def logaritimo(logaritimando,base):
    return math.log(logaritimando,base)


print(subFat(7,3))
lista1 = [13,52,75,12,8]
lista2 = [6,87,1,54,-6]
print(prodEsc(lista1,lista2))
print(raizes(43,98))
print(logaritimo(876,34))