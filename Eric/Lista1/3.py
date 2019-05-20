"""Faça um programa que leia 2 strings e imprima elas seguido de seu comprimento. Informe também se as duas strings
possuem o mesmo comprimento e se são iguais ou diferentes no conteúdo, caso contrário, dizer que as strings são
diferentes"""

def main():
    # asks for the strings
    first = input("digite a primeira string:\n")
    second = input("digite a segunda string:\n")
    # prints the string and length
    print(first, "- tamanho:", len(first))
    print(second, "- tamanho:", len(second))
    # prints if the strings are different or equal
    if first == second:
        print("As duas string são iguais")
    else:
        print("As duas strings são diferentes")


if __name__ == "__main__":
    main()
