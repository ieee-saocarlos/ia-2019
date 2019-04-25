lista =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []
lista_inversa = []
lista_primo = []

for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

    a = 0
    for k in range(2, n):
        if n % k == 0:
            a = 1
            break

    if a == 0 and n != 1:
        lista_primo.append(n)

lista_inversa = lista[::-1]

print(lista_par) # [2, 4, 6, 8, 10]
print(lista_impar) # [1, 3, 5, 7, 9]
print(lista_inversa) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lista_primo) # [2, 3, 5, 7]