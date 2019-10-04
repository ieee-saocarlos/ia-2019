matriz = [['Mateus', 82, 174],
['João', 74, 169],
['Laura', 59, 158],
['Marcos', 112, 190],
['Gisele', 47, 159],
['Ana Clara', 70, 165]]

matriz_copia = [['Mateus', 82, 174],
['João', 74, 169],
['Laura', 59, 158],
['Marcos', 112, 190],
['Gisele', 47, 159],
['Ana Clara', 70, 165]]

nome = input("Digite o nome da pessoa a ser adicionada:\t")
peso = int(input("Digite o peso da pessoa a ser adicionada:\t"))
altura = int(input("Digite a altura da pessoa a ser adicionada:\t"))

matriz.append([nome, peso, altura])
matriz_copia.append([nome, peso, altura])

count = 0

while count < len(matriz_copia):
    for n in matriz:
        a = 0
        for k in matriz:
            b = 0

            if len(n[0]) > len(k[0]):
                minimo = len(k[0])
            else:
                minimo = len(n[0])

            for i in range(minimo):
                if n[0][i] > k[0][i]:
                    a = 1
                    b = 1
                    break
                elif n[0][i] == k[0][i]:
                    continue
                else:
                    break

            if b == 1:
                break

        if a == 0:
            print (n)
            matriz.remove(n)
            count += 1

med_peso = 0
med_alt = 0

for pes in matriz_copia:
    med_peso += (pes[1] / len(matriz_copia))
    med_alt += (pes[2] / len(matriz_copia))

print ('\n')
print ("media de peso: {}".format(med_peso)) # 75.29
print ("media de altura: {}".format(med_alt)) # 169.57


