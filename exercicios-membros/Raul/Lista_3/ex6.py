from math import fabs

def colocar_rainhas(rainhas, k):
    global a
    if a == 1:
        return
    if k == len(rainhas):
        print (rainhas)
        mostrar_tabuleiro(rainhas)
        a = 1
        return

    else:
        for i in range(1, len(rainhas) + 1):
            rainhas[k] = i
            if verificar(rainhas) == 1:
                colocar_rainhas(rainhas, k + 1)
            rainhas[k] = 0


def verificar(u):
    for pos in range(len(u)):
        for n in range(len(u)):
            if u[pos] == u[n] and u[pos] != 0 and pos != n:
                return 0

    for pos in range(len(u)):
        for n in range(len(u)):
            if fabs(u[pos] - u[n]) == fabs(pos - n) and u[pos] != 0 and u[n] != 0 and pos != n:
                return 0

    return 1

def mostrar_tabuleiro(rainhas):
    for linhas in range(len(rainhas)):
        for colunas_1 in range(rainhas[linhas] - 1):
            print ('| ', end = '')
        print ('|♠', end = '')
        for colunas_1 in range(rainhas[linhas] - 1, 8):
            print ('| ', end = '')
        print (end = '\n')

rainhas = [0, 0, 0, 0, 0, 0, 0, 0]
a = 0

colocar_rainhas(rainhas, 0) # [1, 5, 8, 6, 3, 7, 2, 4]