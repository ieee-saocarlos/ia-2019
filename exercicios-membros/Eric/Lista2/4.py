"""
Faça um programa que pegue a lista  [ 15 , 9 , -3 , 7 , 99 , -3 , 0 , -5 , 8 , 15 , -6 , -3 , 99 , 15 , 0 , 15 ]
e imprima:

*Uma lista de forma crescente (sem utilizar comandos).
*Uma lista de forma decrescente e sem números repetidos.
*Duas listas, sendo uma delas com números pares e a outra com números ímpares,
de forma crescente e sem números repetidos.
*Quantas vezes cada número aparece na lista.
"""

from collections import Counter


def sort_list(mylist):
    sorted_list = []
    for number in mylist:
        i = 0
        if not sorted_list:
            sorted_list.append(number)
            i = len(sorted_list)

        j = 0
        while len(sorted_list) > i:
            if sorted_list[i] >= number:
                j = 1
                sorted_list.insert(i, number)
                break
            else:
                i += 1

        if j == 0:
            sorted_list.append(number)

    return sorted_list


def main():
    my_list = [15, 9, -3, 7, 99, -3, 0, -5, 8, 15, -6, -3, 99, 15, 0, 15]
    my_list_2 = list(dict.fromkeys(my_list))

    sorted_list = sort_list(my_list)

    list_2 = (sort_list(my_list_2))
    sorted_reverse_nr = list_2[::-1]

    even_list = [i for i in my_list_2 if i % 2 == 0]
    sorted_even_list = sort_list(even_list)

    odd_list = [j for j in my_list_2 if j % 2 == 1]
    sorted_odd_list = sort_list(odd_list)

    print(sorted_list)
    print(sorted_reverse_nr)
    print(sorted_even_list)
    print(sorted_odd_list)
    print(Counter(my_list).most_common(16))

if __name__ == '__main__':
    main()
