"""Considerando 2a5 e 2b5, para ab, temos a seguinte combinação:

Se os resultados forem colocados em ordem crescente, retirando os números repetidos, chegamos a seguinte sequência de 15 termos:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
Faça um programa que determine a quantidade de termos distintos gerados pela sequência ab para 2a100 e 2b100.


"""



def eleva(minBase,maxBase,minExp,maxExp):
    conjunto=set()
    for a in range (minBase,maxBase+1):
        for b in range (minExp,maxExp+1):
            set1={int(a**b)}
            conjunto = conjunto.union(set1)
    conjunto = list(conjunto)
    conjunto.sort()

    return conjunto

conjunto=eleva(2,100,2,100)
print(conjunto) 
print(f'Número de termos:{len(conjunto)}')#9183