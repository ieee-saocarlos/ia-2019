from math import log10

soma = 0

for i in range(1, 1001):
    soma = soma + (i ** i)

log_da_soma = log10(soma)
parte_inteira_do_log = int(log_da_soma)

print (soma)
print (parte_inteira_do_log) #3000