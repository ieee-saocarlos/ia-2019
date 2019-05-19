x=input("Digite uma palavra")
y=input("Digite outra palavra")
lx=len(x)
ly=len(y)
print(x,lx," letras")
print(y,ly," letras")
if lx==ly:
    print("tem a mesma quantidade de letras")
    if x==y:
        print("e são a mesma palavra")
elif lx!=ly:
    print ("tem quantidades de letras diferentes")
