lista = [4,178,24,9,53,9,75,31,1,43,6,2,120,51,7,28,190,3,5,89,13]
M=0
for c in range(len(lista)-3):
    if(M<lista[c]*lista[c+1]*lista[c+2]*lista[c+3]):
        M=lista[c]*lista[c+1]*lista[c+2]*lista[c+3]
        n=c
print('O maior produto é',M, 'formado pela sequencia',lista[n],'*',lista[n+1],'*',lista[n+2],'*',lista[n+3])