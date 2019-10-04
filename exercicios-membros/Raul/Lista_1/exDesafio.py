num_1_a_9 = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
num_10_a_19 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
cem = 'cem'
milhar = 'mil'

soma = 0

for n in range(1, 1001):
    if n < 10:
        soma += len(num_1_a_9[n - 1])
    elif n < 20:
        soma += len(num_10_a_19[n - 10])
    elif n < 100:
        if n % 10 == 0:
            soma += len(dezenas[(n // 10) - 2])
        else:
            soma += len(dezenas[(n // 10) - 2]) + len('e') + len(num_1_a_9[(n % 10) - 1])
    elif n < 1000:
        if n % 10 == 0:
            if n % 100 == 0:
                if n == 100:
                    soma += len(cem)
                else:
                    soma += len(centenas[(n // 100) - 1])
            else:
                soma += len(centenas[(n // 100) - 1]) + len('e') + len(dezenas[((n // 10) - ((n // 100) * 10)) - 2])
        else:
            soma += len(centenas[(n // 100) - 1]) + len('e') + len(dezenas[((n // 10) - ((n // 100) * 10)) - 2]) + len('e') + len(num_1_a_9[(n - ((n // 10) * 10)) - 1])
    else:
        soma += len(milhar)

print (soma) #20796