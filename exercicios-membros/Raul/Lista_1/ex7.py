letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string = input("Digite a string a ser modificada:\t")
string_copia = string

a = 0

letras_string = []
count = 0
for i in range(len(string)):
    if string[i] in letras:
        count += 1
        letras_string.append([string[i], i, count])

while a == 0:
    n = int(input("Digite o número de digitos a serem colocado em maiuscula:\t"))

    if n > count:
        print ("\tO número digitado é grande demais!\n")
    else:
        a = 1


for k in letras_string:
    if n == k[2]:
        posicao = k[1]

string_1 = string[:posicao + 1].upper()
string_2 = string[posicao + 1:].lower()

print (string_1 + string_2)