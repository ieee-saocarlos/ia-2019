unidades = ("zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove")
dezavinte = ("dez", "onze", "doze", "treze", "quatorze",
             "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

dezenas = ("dez", "vinte", "trinta", "quarenta", "cinquenta",
           "sessenta", "setenta", "oitenta", "noventa")

centenas = ("cento", "duzentos", "trezentos", "quatrocento", "quinhentos",
            "seiscentos", "setecentos", "oitocentos", "novecentos")

valordigitado = str(input('Digite um número de 0 até 1000: ', ))
valordigitado.zfill(2)
centenadigitada = int(valordigitado[0])
dezenadigitada = int(valordigitado[1])
unidadedigitada = int(valordigitado[2])
if centenadigitada == 0:
    if dezenadigitada == 0:
        resultado = unidades[unidadedigitada]
        print(resultado)
    elif dezenadigitada == 1:
        if 0 <= unidadedigitada <= 9:
            resultado = dezavinte[unidadedigitada]
            print(resultado)
    elif 2 <= dezenadigitada <=9:
        if unidadedigitada == 0:
            resultado = dezenas[dezenadigitada - 1]
            print(resultado)
        elif 0 < unidadedigitada <= 9:
            resultado = dezenas[dezenadigitada - 1] + ' e' + unidades[unidadedigitada]
            print(resultado)
elif 1<= centenadigitada <= 9:
            resultado = centenas[centenadigitada - 1] + 'e' + dezenas[dezenadigitada -1] + 'e' +\
                        unidades[unidadedigitada]
            print(resultado)
