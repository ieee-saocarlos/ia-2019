"""Se todos os números de 1 a 1000 (um mil) forem escritos por extenso, quantas letras serão utilizadas?"""

import time


def n_letters():
    Lista1 = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    D = 'dez'
    Lista2 = ['onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    Lista3 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    Lista4 = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
              'novecentos']
    M = 'mil'
    E = 'E'

    for c in range(0, 9):
        yield len(Lista1[c])
    yield len(D)
    for c in range(0, 9):
        yield len(Lista2[c])
    for c in range(0, 8):
        yield len(Lista3[c])
        for d in range(0, 9):
            yield len(Lista3[c]) + len(E) + len(Lista1[d])
    for c in range(0, 9):
        yield len(Lista4[c])
        yield len(Lista4[c]) + len(E) + len(D)
        for d in range(0, 9):
            yield len(Lista4[c]) + len(E) + len(Lista1[d])
            yield len(Lista4[c]) + len(E) + len(Lista2[d])
        for d in range(0, 8):
            yield len(Lista4[c]) + len(E) + len(Lista3[d])
            for e in range(0, 9):
                yield len(Lista4[c]) + len(E) + len(Lista3[d]) + len(E) + len(Lista1[e])

    yield len(Lista1[0]) + len(M)
    yield -2  # Uma vez é cem e não cento


def main():
    start = time.perf_counter()
    print(sum(n_letters()))
    end = time.perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()

#19674