numero = 600851475143
num = numero
maior_primo = 0

while numero % 2 == 0:
    maior_primo = 2
    numero = numero / 2

for div in range(3, num + 1, 2):
    flag = 0
    if numero % div == 0:
        for k in range(3, div, 2):
            if div % k == 0:
                flag = 1
                break
        if flag == 0:
            maior_primo = div
            while numero % div == 0:
                numero = numero / div
    if numero == 1:
        break


print (maior_primo) #6857
