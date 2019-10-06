string_1 = input("Digite a primeira string:\t")
string_2 = input("Digite a segunda string:\t")

print (string_1, len(string_1))
print (string_2, len(string_2))

if len(string_1) == len(string_2):
    print ("As duas strings tem o mesmo tamanho!")

    if string_1 == string_2:
        print ("As duas strings são iguais!")
else:
    print ("As strings são diferentes!")