def fatorial(n_1, n_2):

    prod_1 = 1
    prod_2 = 1

    for x in range(1, n_1 + 1):
        prod_1 = prod_1 * x

    for x in range(1, n_2 + 1):
        prod_2 = prod_2 * x

    if n_1 > n_2:
        return prod_1 - prod_2

    else:
        return prod_2 - prod_1


def prod_int(u, v):

    prod = 0

    for (a, b) in zip(u, v):
        prod = prod + (a * b)

    return prod


def raiz(n):

    resp = 0
    x = 0.001

    while x < n:
        resp = resp + x
        tent = resp * resp
        if tent > n * 0.9999 and tent < n * 1.0001:
            break
        elif tent > n * 1.8:
            x = - 0.0015
        elif tent > n * 1.5 and tent < n * 1.8:
            x = - 0.0009
        elif tent > n * 1.2 and tent < n * 1.5:
            x = - 0.0005
        elif tent > n * 1.0001 and tent < n * 1.2:
            x = - 0.00005
        elif tent > n * 0.8 and tent < n * 0.9999:
            x = 0.00005
        elif tent > n * 0.5 and tent < n * 0.8:
            x = 0.0005
        elif tent > n * 0.2 and tent < n * 0.5:
            x = 0.0009
        else:
            x = 0.0015


    resp = int(resp * 1000) / 1000

    return resp


def log(n, b = 34):

    x = 0.001
    resp = 0

    while 1:
        resp = resp + x
        tent = b ** resp

        if tent > n * 0.9999 and tent < n * 1.0001:
            break
        elif tent > n * 1.8:
            x = - 0.0015
        elif tent > n * 1.5 and tent < n * 1.8:
            x = - 0.0009
        elif tent > n * 1.2 and tent < n * 1.5:
            x = - 0.0005
        elif tent > n * 1.0001 and tent < n * 1.2:
            x = - 0.00005
        elif tent > n * 0.8 and tent < n * 0.9999:
            x = 0.00005
        elif tent > n * 0.5 and tent < n * 0.8:
            x = 0.0005
        elif tent > n * 0.2 and tent < n * 0.5:
            x = 0.0009
        else:
            x = 0.0015


    resp = int(resp * 1000) / 1000

    return resp


lista_1 = [13, 52, 75, 12, 8]
lista_2 = [6, 87, 1, 54, -6]



print (fatorial(7,3)) # 5034

print ('\n')

print (prod_int(lista_1, lista_2)) # 5277

print ('\n')

print (raiz(43)) # 6.557
print (raiz(98)) # 9.898

print ('\n')

print (log(876)) # 1.921