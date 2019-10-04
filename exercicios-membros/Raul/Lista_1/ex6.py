import random as random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista = []
lista_2 = []
repeticao = []
letra_repetida = ['', 0]

for _ in range(random.randint(20, 51)):
    lista.append(random.choice(letras))
    lista_2.append(lista[-1])

for letra in letras:
    repeticao.append([letra, 0])
    while letra in lista:
        repeticao[-1][1] += 1
        lista.remove(letra)
    if repeticao[-1][1] > letra_repetida[1]:
        letra_repetida[0] = repeticao[-1][0]
        letra_repetida[1] = repeticao[-1][1]

print (lista_2)
for letrass in repeticao:
    if letrass[1] == letra_repetida[1]:
       print ("A letra {} repete {} vezes".format(letrass[0], letrass[1]))