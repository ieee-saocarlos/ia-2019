"""Encontre o valor da parte inteira do log10 da soma: 1^1+2^2+3^3+...+998^998+999^999+1000^1000."""
import math


def main():
    # gerador de potências
    mygen = (i**i for i in range(1, 1001))
    # parte inteira do log10 da soma
    print(int(math.log(sum(mygen), 10)))


if __name__ == main():
    main()

