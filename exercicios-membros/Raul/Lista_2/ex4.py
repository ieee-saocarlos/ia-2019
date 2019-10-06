lista = [4, 178, 24, 9, 53, 9, 75, 31, 1, 43, 6, 2, 120, 51, 7, 28, 190, 3, 5, 89, 13]

maior_mult = 0

for n in range(len(lista) - 3):
    mult = lista[n] * lista[n + 1] * lista[n + 2] * lista[n + 3]
    if mult > maior_mult:
        maior_mult = mult

print (maior_mult) #2037744
