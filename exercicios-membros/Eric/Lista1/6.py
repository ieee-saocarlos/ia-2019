"""Faça um programa que crie uma lista com tamanho aleatório n, entre 20 e 50, composta de letras aleatórias e determine
 qual letra mais se repete e quantas vezes essa letra se repetiu. Se houver mais de uma letra se repetindo um número
 maior de vezes, imprimir todas as letras que mais se repetem."""


import random
import string
from collections import Counter


# generator that yields r random numbers
def letters(r):
    for i in range(r):
        yield random.choice(string.ascii_letters)


def main():
    # chooses a random number between 20 and 30
    r = random.randint(20, 50)
    # counts how many times each letter appears
    a = Counter(letters(r)).most_common(r)
    # shows only the most common letters
    for j in range(r-2):
        if a[j][1] == a[0][1]:
            print(a[j])
        else:
            break


if __name__ == "__main__":
    main()
