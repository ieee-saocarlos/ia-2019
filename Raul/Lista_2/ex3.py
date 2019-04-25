lista = [15, 9, -3, 7, 99, -3, 0, -5, 8, 15, -6, -3, 99, 15, 0, 15]
lista_copia = [15, 9, -3, 7, 99, -3, 0, -5, 8, 15, -6, -3, 99, 15, 0, 15]
lista_cres = []
lista_decres = []
lista_par = []
lista_impar = []
lista_num_rep = []

tamanho = len(lista)

while len(lista_cres) < tamanho:
    for n in lista_copia:
        a = 0
        for k in lista_copia:
            if n > k:
                a = 1
                break
        if a == 0:
            lista_cres.append(n)
            lista_copia.remove(n)


for k in lista_cres[::-1]:
    if k not in lista_decres:
        lista_decres.append(k)

for num in lista_decres[::-1]:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

for n in lista_cres:
    if [n, lista_cres.count(n)] not in lista_num_rep:
        lista_num_rep.append([n, lista_cres.count(n)])

print (lista_cres) # [-6, -5, -3, -3, -3, 0, 0, 7, 8, 9, 15, 15, 15, 15, 99, 99]
print (lista_decres) # [99, 15, 9, 8, 7, 0, -3, -5, -6]
print (lista_par, lista_impar) #[-6, 0, 8] [-5, -3, 7, 9, 15, 99]
for j in lista_num_rep:
    print ("O número {} repete {} vezes".format(j[0], j[1]))

