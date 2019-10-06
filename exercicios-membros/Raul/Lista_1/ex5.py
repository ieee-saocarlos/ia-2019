fib = [0, 1]
soma = 0

while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0 and fib[-1] < 4000000:
        soma = soma + fib[-1]

print (soma) #4613732