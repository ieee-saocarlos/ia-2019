lista_ingredientes = [['Arroz', 100, 5.0],
                      ['Carne', 100, 16.0],
                      ['Batata Inglesa', 250, 3.5],
                      ['Cenoura', 100, 3.0],
                      ['Queijo Minas', 150, 12.0],
                      ['Macarrão', 200, 13.75]]

lista_pratos = [['Muito Escondidinho', ['Batata Inglesa', 3], ['Queijo Minas', 1], ['Cenoura', 1]],
                ['Pastelão de Vento', ['Batata Inglesa', 4], ['Carne', 1]],
                ['Misturadão', ['Arroz', 4], ['Carne', 2], ['Cenoura', 3],
                    ['Queijo Minas', 2], ['Macarrão', 3]],
                ['Marmitex', ['Arroz', 3], ['Macarrão', 2], ['Carne', 4], ['Queijo Minas', 1]]]

lista_consumo = [['Muito Escondidinho', 13],
                 ['Pastelão de Vento', 21],
                 ['Misturadão', 19],
                 ['Marmitex', 25]]

compra_total = [0, 0, 0, 0, 0, 0]
valor_pratos = []
prato_mais_caro = [0]

for prato in lista_pratos:
    compras = []
    custo = 0
    for ingrediente in range(1, len(prato)):
        for opcao in lista_ingredientes:
            if prato[ingrediente][0] == opcao[0]:
                custo += prato[ingrediente][1] * opcao[2]

        for consumo in lista_consumo:
            if prato[0] == consumo[0]:
                compra = prato[ingrediente][1] * consumo[1]
        compras.append(compra)

    print ('O prato {} custa {}'.format(prato[0], custo))
    for n in range(len(compras)):
        print ('Vai ser necessário {} {} do prato {}'.format(compras[n], prato[n + 1][0], prato[0]))
        for k in range(len(lista_ingredientes)):
            if lista_ingredientes[k][0] == prato[n + 1][0]:
                compra_total[k] += compras[n]

    valor_pratos.append(custo)
    print ('\n')


for i in range(len(compra_total)):
    print ('Deve-se comprar {} {}'.format(compra_total[i], lista_ingredientes[i][0]))

print ('\n')

for valor in range(len(valor_pratos)):
    if valor_pratos[valor] > prato_mais_caro[0]:
        prato_mais_caro[0] = valor_pratos[valor]
        prato_mais_caro.append(valor)

print ('O prato {} é o mais caro, com o valor de {}'.format(lista_pratos[prato_mais_caro[1]][0], prato_mais_caro[0])) # O prato Muito Escondidinho é o mais caro, com o valor de 126.25

