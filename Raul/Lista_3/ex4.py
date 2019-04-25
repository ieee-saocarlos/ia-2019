def imprimir_1 (n):
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print ('\t {}'.format(y), end = '')
        print (end = '\n')

    return

def imprimir_2 (n):
    for x in range(1, n + 1):
        print ('\t {}'.format(x) * x)

    return

def imprimir_quad (n):
    for linha in range(1, n + 1):
        for coluna in range(1, n + 1):
            if linha >= coluna:
                print ('\t {}'.format(linha - coluna + 1), end = '')
            else:
                print ('\t {}'.format(coluna - linha + 1), end = '')
        print (end = '\n')


n = int(input('Digite o valor de n:\t'))

print ('\n')
imprimir_1(n)
print ('\n')
imprimir_2(n)
print ('\n')
imprimir_quad(n)
