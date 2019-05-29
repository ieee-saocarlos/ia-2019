def funcao(x):#Função que pega o argumento dado e aplica na f(x) dada pelo exercício
    x = float(x)#Necessário para que a funcção entenda que não é uma string(não é necessário desde que fique claro que o valor dado na função principal é realmente um valor e não uma string).
    return 5*(x**2 + x - 1)#retornando a f(x) dada.    (O simbolo "**" é elevado).


def derivada(p):#Função que deriva(de forma aproximada) a f(x) dada no ponto p.       ***(A derivada da f(x), neste caso, é: f'(x)=10*x +5)***
    x = float(p)
    return ((funcao(p+(1/100000))-funcao(p))/(1/100000))# Delta x deve ser um valor muito pequeno para ter uma aproximação mais exata.    ***(Se possível usar delta x na forma fracionária)***


#retorno pedido pelo enunciado:
w= input("Digite o valor de x:")
print("f(",w,")=",funcao(w))
print("f'(9) = %.2f" %derivada(9))#  =  95
print("f'(3) = %.2f" %derivada(3))#  =  35

# ("%.gf" %k) arredondando o número k em g casas.