"""Faça um programa que peça 10 números e imprima uma lista com esses valores. """


def main():
    # lista onde serão colocados os números
    numbers = []
    # pede os 10 números
    for i in range(1, 11):
        n = input('digite o {}o número'.format(i))
        numbers.append(n)
    # printa a lista com os números
    print(numbers)


if __name__ == '__main__':
    main()
