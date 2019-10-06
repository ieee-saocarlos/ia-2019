def funcao(x):
    return 5 * (((x**2) + x - 1) ** 2)

def derivada(f, x):
    h = 0.000001
    if f(x) > f(x + h):
        return (f(x) - f(x + h)) / h
    else:
        return (f(x + h) - f(x)) / h

deri_3 = derivada(funcao, 3)
deri_9 = derivada(funcao, 9)

print (deri_3) # 770
print (deri_9) # 16910