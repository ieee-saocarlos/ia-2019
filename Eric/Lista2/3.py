"""
Faça um programa que a partir da lista [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] imprima:
*Uma lista com somente números pares.
*Uma lista com somente números  ímpares.
*Uma lista inversa a lista inicial (sem uso de comandos prontos como reverse).
*Uma lista com somente números primos.
"""


def main():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # cria a lista de pares
    evenlist = [i for i in mylist if i % 2 == 0]
    # cria a lista de ímpares
    oddlist = [j for j in mylist if j % 2 == 1]
    # cria a lista invertida
    reverselist = mylist[::-1]
    # primairo primo
    primelist = [2]

    # encontra os outros primos e adiciona na lista de primos
    for k in mylist[1:]:
        for p in primelist:
            if k % p == 0:
                break
            else:
                primelist.append(k)
                break

    print("números pares:", evenlist)
    print("números ímpares:", oddlist)
    print("lista invertida:", reverselist)
    print("primos:", primelist)


if __name__ == '__main__':
    main()
