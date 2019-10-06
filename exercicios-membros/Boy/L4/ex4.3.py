"""n / 2	Se n par
3n + 1	Se n ímpar
E começando com o número 13, chegamos a seguinte sequência:
134020105168421
É visto que a sequência acima contém 10 termos (contando o 13 e o 1). Ainda que não seja provado (Problema de Collatz) , acredita-se que qualquer número que inicia essa sequência finaliza em 1.
Faça um programa que encontre o número inicial, menor que um milhão, que produza a maior sequência.
Assim que a sequência é iniciada, os números podem ser maiores que um milhão
"""

def fpar(n,s):

    return n/2


def fimpar(n,s):

    return (3*n) + 1


def f(n,s=1):
    while(n!=1):
        if(n%2==0):
            s += 1
            n=fpar(n,s)
        else:
            s += 1
            n=fimpar(n,s)
    return s

def test(max):
    melhor = {'inicio': 0, 'tamanhoSequencia': 0}
    for c in range (1,max):
        s=f(c)

        if(s>melhor['tamanhoSequencia']):
            melhor['inicio']=c
            melhor['tamanhoSequencia']=s
    return melhor


vencedor=test(1000000)
print(vencedor)#{'inicio': 837799, 'tamanhoSequencia': 525}
