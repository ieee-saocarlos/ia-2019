a= input('Digite um texto:')
n= int(input('Digite um número:'))
while (n>len(a) - a.count(' ')):
    n=int(input('Por favor, digitar um outro valor para nome:'))

n= n + a.count(' ')
print(a[:n].upper(), end='')
print(a[n:].lower())


# Esse programa foi feito apenas para trabalhar com letras e espaços. Se quiser trabalhar com todos
# os caracteres especiais deve-se adicionar +ou- a.count('caracter_especial_especifico') seguindo o exemplo do espaço(' ').