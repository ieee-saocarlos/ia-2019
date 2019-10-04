"""Faça um Programa que peça a temperatura em Fahrenheit, transforme e mostre a temperatura em graus Celsius"""

def main():
    # asks for temperature in fehrenheits
    f = int(input("Digite a temperatura em Fahrenheit (apenas números): \n"))
    # using the given equation get the value in celsius
    c = (5/9)*(f-32)
    # prints the result with two decimal algarisms
    print(round(c, 2), "ºC")


if __name__ == "__main__":
    main()
