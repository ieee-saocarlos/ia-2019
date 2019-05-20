"""Faça um programa que encontre o maior fator primo do número 600851475143"""

import math


def main():
    number = 600851475143
    # biggest divisor of the number
    max_d = int(math.sqrt(600851475143)+1)
    flag = 0
    # loops to find the divisors
    for i in range(3, max_d, 2):
        while flag != 1:
            if number % i == 0 and number != i:
                # when a divisor is found the next number analysed is the quotient
                number = number/i
            else:
                # jumps to the next possible divisor
                flag = 1
        flag = 0
    print(number)


if __name__ == "__main__":
    main()
