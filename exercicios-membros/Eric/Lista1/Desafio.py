"""Se todos os números de 1 a 1000 (um mil) forem escritos por extenso, quantas letras serão utilizadas?"""

import time


def n_letters():
    u = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

    t = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

    d = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

    c = ('cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos'
         , 'novecentos')

    m = 'um mil'

    yield len(m.replace(" ", ""))
    yield len(c[0])

    for i in range(1000):
        i = "%04d" % i
        i = str(i)

        if int(i) > 100:
            yield len(c[int(i[1])])
            if i[2:] != '00':
                yield len('e')

        if i[2] != '1':
            yield len(d[int(i[2])] + u[int(i[3])])
            if int(i[2:]) > 20 and i[3] != '0':
                yield len('e')

        if i[2] == '1':
            yield len(t[int(i[3])])


def main():
    start = time.perf_counter()
    print(sum(n_letters()))
    end = time.perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()

#19674