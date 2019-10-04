#Exercicio 6 - Lista 2: Faça um programa que peça informações da pessoa como nome “Juliana”, peso 83 Kg e 172 cm de altura, adicione na matriz abaixo, imprima as informações de cada pessoa em ordem alfabética e calcule as médias dos pesos e das alturas.

m = [["Mateus", 82, 174], ["João", 74, 169],
["Laura", 59, 158],
["Marcos", 112, 190],
["Gisele", 47, 159],
["Ana Clara", 70, 165]]


nome=input("Digite o nome da pessoa:\n")
peso=float(input("Digite o peso da pessoa(kg):\n"))
altura=float(input("Digite a altura da pessoa(cm):\n"))

m.append([nome,peso,altura])
m.sort()

print("INFORMACOES CADASTRADAS:")
print("NOME:  PESO(kg):  ALTURA(cm):")
#imprimir em ordem alfabetica
for i in m:
	print(i)
#media dos pesos e das alturas
m_p=0
m_a=0
for i in m:
	m_p+=i[1]
	m_a+=i[2]	
print("Media dos pesos(kg):\n",m_p/7)
print("Media das alturas(cm):\n",m_a/7)
		
		
			