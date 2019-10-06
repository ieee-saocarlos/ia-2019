#Programa que converte temperatura em graus celsius para fahrenheit
tempCelsius = input("Digite uma temperatura em ºC: ",)
print('A temperatura digitada foi,:', tempCelsius, 'Graus Celsius')
tempFaren = float(tempCelsius)
tempFaren = (9*tempFaren/5) + 32
print('A temperatura em Fahrenheit é:', tempFaren,'ºF')
