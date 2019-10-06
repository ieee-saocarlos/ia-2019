def potencia(a, b):
    return a ** b

numeros = []

for a in range(2, 101):
    for b in range(2, 101):
        numeros.append(potencia(a, b))

numeros = sorted(numeros)
print (len(list(set(numeros)))) # 9183