"""Sabe-se o seguinte sobre os ingredientes que compõem os pratos de um restaurante:
Nome
Peso da porção (em gramas)
Preço do Kg.

a) Crie uma lista de ingredientes onde cada elemento armazena o nome do ingrediente, peso da porção (em g) e o preço do
Kg.

b) Crie uma lista de Pratos de um restaurante onde cada elemento armazena o nome do prato e listas de ingrediente com
nome dos ingredientes que o prato utiliza e quantidade de porções necessárias para prepará-lo.

c) Crie uma lista com a quantidade semanal vendida de cada prato.

d) Faça um programa que, utilizando as listas criadas nos itens a, b e c, mostre:

* O custo de cada prato e a quantidade que deverá ser comprada de cada ingrediente para sua produção semanal
* A quantidade que deverá ser comprada de cada ingrediente para produzir todos os pratos por uma semana
* O prato que renderá maior dinheiro na semana e quanto será esse valor
"""
def main():

    ingredientes = [
        ["Arroz",		   100, 5.00,  0],
        ["Carne",		   100, 16.00, 0],
        ["Batata Inglesa", 250, 3.50,  0],
        ["Cenoura",		   100, 3.00,  0],
        ["Macarrão",	   200, 13.75, 0],
        ["Queijo Minas",   150, 12.00, 0]
    ]

    pratos = [
        ["Muito Escondidinho", ["Batata Inglesa", 3], ["Queijo Minas", 1], ["Cenoura", 1]],
        ["Pastelão de Vento",  ["Batata Inglesa", 4], ["Carne", 1]],
        ["Misturadão",    ["Arroz", 4],      ["Carne", 2],        ["Cenoura", 3], ["Queijo Minas", 2], ["Macarrão", 3]],
        ["Marmitex",      ["Arroz", 3],      ["Macarrão", 2],     ["Carne", 4],   ["Queijo Minas", 1]]
    ]

    consumo = [
        ["Muito Escondidinho", 13],
        ["Pastelão de Vento",  21],
        ["Misturadão",         19],
        ["Marmitex",           25]
    ]

    # lista com o prato de maior lucro e o dinheiro recebido
    maior_lucro = [0, 0]

    for prato in pratos:
        custo = 0
        print(("Ingredientes do {}:".format(prato[0])).upper())
        # pega o indice de cada ingrediente
        for i in range(1, len(prato)):
            for ingrediente in ingredientes:
                # compara cada ingrediente disponível para ver se é igual
                if prato[i][0] == ingrediente[0]:
                    # calcula o custo de cada prato
                    custo += prato[i][1] * ingrediente[1] * ingrediente[2] * 0.001
                    # pega a quantidade consumida do prato semanalmente
                    for j in consumo:
                        if j[0] == prato[0]:
                            c = j[1]
                    # calcula e imprime a quantidade de ingredientes de cada prato
                    print('*' + ingrediente[0] + ": {} kg semanais".format(ingrediente[1] * prato[i][1] * 7/1000 * c))
                    # soma a quantidade do ingrediente
                    ingrediente[3] += 7 * ingrediente[1] * prato[i][1] * c

        print("\nO {} custa R${}".format(prato[0], "%.2f" % custo))

        # encontra o prato com maior lucro
        if custo * c > maior_lucro[1]:
            maior_lucro = [prato[0], custo * c]

        print("------------------------------------------------------")
    
    print("Quantidade semanal de cada ingrediente:\n")
    for ingrediente in ingredientes:
        print("{}: {} kg".format(ingrediente[0], ingrediente[3]/1000))

    print("---------------------------------------------------")
    print(maior_lucro)


if __name__ == '__main__':
    main()
