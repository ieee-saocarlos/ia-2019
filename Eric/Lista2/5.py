"""
Faça um programa que pegue a lista
[ 4 , 178 , 24 , 9 , 53 , 9 , 75 , 31 , 1 , 43 , 6 , 2 , 120 , 51 , 7 , 28 , 190 , 3 , 5 , 89 , 13 ]
e encontre o maior valor de multiplicação de quatro números sequências.
"""


def main():
    my_list = [4, 178, 24, 9, 53, 9, 75, 31, 1, 43, 6, 2, 120, 51, 7, 28, 190, 3, 5, 89, 13]

    m = len(my_list) - 4
    s = 0

    for i in range(m):
        p = (my_list[i] * my_list[i+1] * my_list[i+2] * my_list[i+3])
        if p > s:
            s = p

    print(s)

if __name__ == '__main__':
    main()