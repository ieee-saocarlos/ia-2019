#EXERCICIO PARA COMPARAR O TAMANHO E O CONTEUDO DE DUAS STRINGS
msg1 = input('Digite uma mensagem:', )
msg2 = input('Digite outra mensagem:', )
tam1 = len(msg1)
tam2 = len(msg2)
if tam1 == tam2:
    if msg1 == msg2:
        print("AS MENSAGENS SÃO IGUAIS")
        print(" A mensagem1 é:", msg1, " \n O tamanho da mensagem1 é:", tam1)
        print(" A mensagem2 é:", msg2, " \n O tamanho da mensagem2 é:", tam2)

    else:
        print('AS MENSAGENS POSSUEM TAMANHOS IGUAIS, PORÉM CONTEUDO DIFERENTE')
        print(" A mensagem1 é:", msg1, " \n O tamanho da mensagem1 é:", tam1)
        print(" A mensagem2 é:", msg2, " \n O tamanho da mensagem2 é:", tam2)

else:
    print("AS MENSAGENS POSSUEM TAMANHOS E CONTEUDOS DIFERENTES")
    print(" A mensagem1 é:", msg1, " \n O tamanho da mensagem1 é:", tam1)
    print(" A mensagem2 é:", msg2, " \n O tamanho da mensagem2 é:", tam2)


