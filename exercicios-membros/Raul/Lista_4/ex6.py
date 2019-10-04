from math import factorial

minimo = 3
maximo = 1000000
sum = 0

for num in range(minimo, maximo):
    numeros = []
    soma = 0
    potencia = 0
    count = 0
    valor = num
    while 10 ** potencia < valor:
        potencia += 1
        count += 1
    for i in range(count):
        numeros.append(valor // (10 ** (potencia - 1)))
        valor = valor - (numeros[i] * (10 ** (potencia - 1)))
        potencia -= 1
    for j in numeros:
        soma += factorial(j)
    if soma == num:
        sum += num

print (sum) # 40730