#Exercicio 4 - Lista 1 : Faça um programa que encontre o maior fator primo do número 600851475143

a = 600851475143
for numero in range (2,600851475143):
    while (a%numero==0):
        a=a/numero
    if (a==1):
        break
print ("Maior fator primo do número 600851475143:",numero)
