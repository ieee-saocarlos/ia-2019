#Pular duas linhas entre uma função e outra, ou entre uma função e o programa principal do código(para ter uma melhor visualização).
def fline(a):#Função que multiplica todos os elementos de uma liststa pelo seu antecessor.
    temp =a[len(a)-1]
    for c in range(len(a)-1,0,-1):
        a[c]= a[c]*a[c-1]
    a[0]=a[0]*temp


def sline(b):#Função que retorna uma lista dos digitos dos elementos da matriz de argumento.
    nlista = []
    for c in range(0,len(b)):
        s=str(b[c])
        for d in range(0,len(s)):
            nlista.append(int(s[d]))
    return nlista


def matriz(*args):#1-Funcão que printa n listas como uma unica matriz. 2-Neste caso o "*args"(parametro indefinido) foi usado para que fosse feita uma função genérica, podendo variar o número de listas usadas como argumentos.
    for c in range (len(args)):
        for d in range (len(args[c])):
            print("[",args[c][d],"]",end='') #Os colchetes foram colocados para que a matriz fique mais visual.
        print()


lista = [13,7,43,76,9,45,1,54]
fline(lista)
nlista =sline(lista)
matriz(lista,nlista)
