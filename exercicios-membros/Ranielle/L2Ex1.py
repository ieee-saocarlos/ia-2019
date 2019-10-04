# -*- coding: utf-8 -*-
numeros = []
contador = 1
while contador <= 10:
   numerodigitado = input('Digite um numero :', )
   numeros.append(numerodigitado)
   contador = contador + 1

print('Os numeros digitados são, nesta ordem: ')
contadorexibenum = 1
while contadorexibenum <=10:
    print numeros[contadorexibenum -1 ]
    contadorexibenum = contadorexibenum +1
