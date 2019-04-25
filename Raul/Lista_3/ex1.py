def fazer_matriz(v):
    matriz = [[],[]]

    for i in range(len(v)):
        matriz[0].append(v[i] * v[i - 1])

    for num in v:
        n = num
        exp = 1
        while 1:
            if num < (10 ** exp):
                for ex in range(exp - 1, -1, -1):
                    matriz[1].append(n // (10 ** ex))
                    n = n % (10 ** ex)
                break

            else:
                exp += 1



    return matriz


lista = [13, 7, 43, 76, 9, 45, 1, 54]

print (fazer_matriz(lista)[0]) # [702, 91, 301, 3268, 684, 405, 45, 54]
print (fazer_matriz(lista)[1]) # [1, 3, 7, 4, 3, 7, 6, 9, 4, 5, 1, 5, 4]
