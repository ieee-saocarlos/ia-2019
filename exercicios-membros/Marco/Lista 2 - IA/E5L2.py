#Faça um programa que pegue a lista [ 4 , 178 , 24 , 9 , 53 , 9 , 75 , 31 , 1 , 43 , 6 , 2 , 120 , 51 , 7 , 28 , 190 , 3 , 5 , 89 , 13 ] e encontre o maior valor de multiplicação de quatro números sequências.


list = [ 4 , 178 , 24 , 9 , 53 , 9 , 75 , 31 , 1 , 43 , 6 , 2 , 120 , 51 , 7 , 28 , 190 , 3 , 5 , 89 , 13 ]
b=0
for i in range(len(list)-3):
	a=list[i]*list[i+1]*list[i+2]*list[i+3]
	if a>b:
		b=a
print("O maior valor de multiplicacao de 4 numeros em sequencia:\n",b)
	