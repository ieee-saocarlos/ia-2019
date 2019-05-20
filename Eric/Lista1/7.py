"""Faça um programa que leia uma string, leia um número n e transforme as n primeiras letras em maiúsculas e o restante
 em minúscula"""


def main():
    f = 0
    n = 0
    s = input("digite uma frase")

    while f == 0:
        n = int(input("digite as n primeiras letras que serão transformadas em maiúsculas"))
        if n <= len(s):
            break
        print("tente um n menor que o tamanho da frase")

    s = s[:n].upper() + s[n:].lower()
    print(s)


if __name__ == "__main__":
    main()