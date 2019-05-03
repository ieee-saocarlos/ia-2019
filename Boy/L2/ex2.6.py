lista=[['Mateus', 82, 174],['João', 74, 169],['Laura', 59, 158],['Marcos', 112, 190],['Gisele', 47, 159],['Ana Clara', 70, 165]]
lista.append(["Juliana", 83 ,172])
lista.sort()
print(lista)
P=0
H=0
for c in range(len(lista)):
    P+=lista[c][1]
    H+=lista[c][2]
print('A média do peso é de',P,"Kg")
print('A média da altura é de',H,"cm")
