# maior fator primo
import math
valorinicial = input("Digite um número e encontre seu maior fator primo:", )
def funcMaiorFatorPrimo(valorinicial):
    r = valorinicial
    i: int = 2
    for i in range(i, math.sqrt(r)):
        if r % i == 0:
            return funcMaiorFatorPrimo(r/i)
        i+=i;
    return r
print(funcMaiorFatorPrimo(valorinicial))