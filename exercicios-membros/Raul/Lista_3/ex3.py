def funcao(x):
    return (8 * (x ** 2)) - (3 * (x ** 3)) + x

def integral(a, b, f):
    x_i = a
    delta = 0.000001
    soma = 0
    while x_i < b:
        soma = soma + (f(x_i) * delta)
        x_i  = x_i + delta

    return soma

int_1_6 = integral(1, 6, funcao)

print (int_1_6) # -380,4
