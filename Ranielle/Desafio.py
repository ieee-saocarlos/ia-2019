# -*- coding: utf-8 -*-
unidades = ("zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove")
dezavinte = ("dez", "onze", "doze", "treze", "quatorze",
             "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

dezenas = ("dez", "vinte", "trinta", "quarenta", "cinquenta",
           "sessenta", "setenta", "oitenta", "noventa")

centenas = ("cento", "duzentos", "trezentos", "quatrocento", "quinhentos",
            "seiscentos", "setecentos", "oitocentos", "novecentos")

valordigitadozfill = input('Digite um numero de zero ate 1000: ', )
while valordigitadozfill > 1000 :
    valordigitadozfill = input('Você digitou um numero maior do que 1000, Digite novamente um numero de um ate 1000: ', )
valordigitadoint = int(valordigitadozfill)
valordigitadozfill=str(valordigitadozfill)
valordigitado = valordigitadozfill.zfill(3)
centenadigitada = int(valordigitado[0])
dezenadigitada = int(valordigitado[1])
unidadedigitada = int(valordigitado[2])
contagemdeletras =[]

for contador in range(valordigitadoint + 1):
    contagem = str(contador)
    valordigitado = contagem.zfill(4)
    milhardigitado = int(valordigitado[0])
    centenadigitada = int(valordigitado[1])
    dezenadigitada = int(valordigitado[2])
    unidadedigitada = int(valordigitado[3])
    if centenadigitada == 0 and milhardigitado != 1:
        if dezenadigitada == 0:
            resultado = unidades[unidadedigitada]
            print(resultado)
        elif dezenadigitada == 1:
            if 0 <= unidadedigitada <= 9:
                resultado = dezavinte[unidadedigitada]
                print(resultado)
        elif 2 <= dezenadigitada <= 9:
            if unidadedigitada == 0:
                resultado = dezenas[dezenadigitada - 1]
                print(resultado)
            elif 1 <= unidadedigitada <= 9:
                resultado = dezenas[dezenadigitada - 1] + ' e ' + unidades[unidadedigitada]
                print(resultado)
                resultado = resultado.replace(' ','')

    elif 1 <= centenadigitada <= 9:
        if dezenadigitada == 0:
            if unidadedigitada == 0:
                resultado = 'cem'
                print (resultado)
            elif 1 <= unidadedigitada <= 9:
                resultado = centenas[centenadigitada - 1] + ' e ' + unidades[unidadedigitada]
                print(resultado)
                resultado = resultado.replace(' ', '')
        elif dezenadigitada == 1:
            resultado = centenas[centenadigitada - 1] + ' e ' + dezavinte[unidadedigitada]
            print(resultado)
            resultado = resultado.replace(' ', '')
        elif 2 <= dezenadigitada <= 9:
            if unidadedigitada == 0:
                resultado = centenas[centenadigitada - 1] + ' e ' + dezenas[dezenadigitada -1]
                print(resultado)
                resultado = resultado.replace(' ', '')
            elif 1 <= unidadedigitada <= 9:
                resultado = centenas[centenadigitada - 1] + ' e ' + dezenas[dezenadigitada -1] + ' e ' +\
                            unidades[unidadedigitada]
                print(resultado)
                resultado = resultado.replace(' ', '')
    elif milhardigitado == 1:
        resultado = 'mil'
        print (resultado)
    contagemdeletras.append(len(resultado))
    print (contagemdeletras)
somadacontagem = sum(contagemdeletras)
print ('A soma das letras de 1 ao numero digitado e: ', somadacontagem - 4)
