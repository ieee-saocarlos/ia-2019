soma_quadrados = 0
quadrados_soma = 0

for i in range(1,101):
    quadrados_soma += i

quadrados_soma = quadrados_soma ** 2

for i in range(1,101):
    soma_quadrados += i ** 2

print (quadrados_soma) # 25502500
print (soma_quadrados) # 338350
print (quadrados_soma - soma_quadrados) # 25164150
