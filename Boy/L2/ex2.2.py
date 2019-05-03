#A soma 1^1+2^2+3^3+4^4+5^5 resulta em 3413, sendo a parte inteira de seu log10 igual a 3. Encontre o valor da parte inteira do log10 da soma:1^1+2^2+3^3+...+998^998+999^999+1000^1000
import math
s=0
for c in range (1,1001):
    s += c**c


print("%.0f" %math.log10(s))

