def func(x):
    return 8*(x**2) - 3*(x**3) + x


'''def integral_a(li,ls,i=0):
    dx=1/470
    if(li+i*dx>ls/3):
        return 0
    else:
        return func(li+i*dx)*dx + integral_a(li,ls,i+1)

def integral_b(ls,i=0):
    dx=1/470
    li=ls/3
    if(li+i*dx>2*ls/3):
        return 0
    else:
        return func(li+i*dx)*dx + integral_b(ls,i+1)


def integral_c(ls,i=0):
    dx=1/470
    li=2*ls/3
    if(li+i*dx>ls):
        return 0
    else:
        return func(li+i*dx)*dx + integral_c(ls,i+1)

def i(li,ls):
    return integral_a(li, ls) + integral_b(ls) + integral_c(ls)'''#Tentativa funcional de aproximar o valor exato da integra, mas pouco prático.

def integralSimples(li,ls,i=0):
    dx=1/190#O menor numero possível para essa técnica é 1/199, alem desse o python não suporta o número de loops
    if(li+i*dx>ls):
        return 0
    else:
        return func(li+i*dx)*dx + integralSimples(li,ls,i+1)



print(integralSimples(1,6))

#Tentar melhorar o código criando uma classe que administra quantas vezes se chama uma classe para tentar aumentar a precisão