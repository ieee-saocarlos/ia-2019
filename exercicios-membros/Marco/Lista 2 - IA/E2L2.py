import math
# Exercicio 2 - Lista 2 :A soma 1^1+2^2+3^3+4^4+5^5 resulta em 3413, sendo a parte inteira de seu log10 igual a 3. Encontre o valor da parte inteira do log10 da soma: 1^1+...+1000^1000.

som=-1
for i in range (1000):
	som=som+(i**i)
l=math.log10(som)
l=int(l)
print("A parte inteira do log10 da somatoria, sera:",l)