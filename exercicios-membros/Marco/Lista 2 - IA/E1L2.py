#Exercicio 1 - Lista 2: Faça um programa que peça 10 números e imprima uma lista com esses valores.

vet=[]
for i in range (10):
	vet.append(int(input("Digite um numero para a lista\n")))
print("A lista formada sera:",vet)