"""
A partir da matriz abaixo, a qual representa em cada linha uma pessoa, apresentando seu nome, seu peso (em Kg)
e sua altura (em cm); faça um programa que peça informações da pessoa com nome “Juliana”, peso 83 Kg e 172 cm de altura,
adicione na matriz abaixo, imprima as informações de cada pessoa em ordem alfabética e calcule as médias dos pesos e das
alturas.

[[“Mateus”, 82, 174],
[“João”, 74, 169],
[“Laura”, 59, 158],
[“Marcos”, 112, 190],
[“Gisele”, 47, 159],
[“Ana Clara”, 70, 165]]
"""


def main():
    matrix = [
        ["Mateus",    82,  174],
        ["João",      74,  169],
        ["Laura",     59,  158],
        ["Marcos",    112, 190],
        ["Gisele",    47,  159],
        ["Ana Clara", 70,  165]
    ]

    nome = input("Digite o nome da pessoa que quer adicionar:")
    peso = input("Digite o peso dessa pessoa:")
    altura = input("Digite a altura dessa pessoa:")

    matrix.append([nome, int(peso), int(altura)])
    matrix.sort()

    p = 0
    a = 0
    print("Nome das pessoas:")
    for pessoa in matrix:
        print(pessoa[0])
        p += pessoa[1]
        a += pessoa[2]

    print("\nMédia de peso:", p / (len(matrix)))
    print("Média de altura:", a / (len(matrix)))


if __name__ == '__main__':
    main()