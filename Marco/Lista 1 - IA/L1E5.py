# Exercicio 5 - Lista 1 : soma dos termos pares da sequencia de fibonacci

som=0
n0=0
n1=1
n2=0
while (n2<4000000):
    n2=n0+n1
    if (n2%2==0):
        som=som+n2
    n0=n1
    n1=n2
print("Soma dos termos pares na sequencia de fibonacci:",som)

