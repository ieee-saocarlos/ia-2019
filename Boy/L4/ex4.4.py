"""2**15=32768. A soma dos dígitos do número resultante é dada por 3+2+7+6+8=26.
Faça um programa que encontre a soma dos dígitos do número resultante de 2**1000.
"""
from math import floor


def somaDigitos(x):
    s=0
    while x>=1:
       k=x%10
       x=floor(x/10)
       s+=k
    return s
print(2**1000)
print(somaDigitos(2**1000))#1189