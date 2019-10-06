Lista1=['um','dois','três','quatro','cinco','seis','sete','oito','nove']
D= 'dez'
Lista2=['onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
Lista3=['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
Lista4=['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
M='mil'
E='E'
s=0
for c in range(0,9):
    s= s+ len(Lista1[c])
s= s + len(D)
for c in range (0,9):
    s = s + len(Lista2[c])
for c in range (0,8):
    s = s +  len(Lista3[c])
    for d in range (0,9):
        s = s + len(Lista3[c])+ len(E) + len(Lista1[d])
for c in range(0,9):
    s = s + len(Lista4[c])
    s = s + len(Lista4[c]) + len(E)+ len(D)
    for d in range (0,9):
        s = s + len(Lista4[c]) + len(E) + len(Lista1[d])
        s = s + len(Lista4[c]) + len(E) + len(Lista2[d])
    for d in range (0,8):
        s = s + len(Lista4[c]) + len(E) + len(Lista3[d])
        for e in range(0,9):
            s = s + len(Lista4[c]) + len(E) + len(Lista3[d])+ len(E) + len(Lista1[e])

s=s+len(Lista1[0]) + len(M)
s = s - 2 #Uma vez é cem e não cento
print(s)