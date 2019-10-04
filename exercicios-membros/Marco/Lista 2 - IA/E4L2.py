#Faça um programa que pegue a lista  [ 15 , 9 , -3 , 7 , 99 , -3 , 0 , -5 , 8 , 15 , -6 , -3 , 99 , 15 , 0 , 15 ] e imprima: a) numeros em ordem crescente. b) decrescente sem repeticao. c) pares e impares, crescente e sem repeticao. d) quantas vezes cada numero se repete. 

m = [ 15 , 9 , -3 , 7 , 99 , -3 , 0 , -5 , 8 , 15 , -6 , -3 , 99 , 15 , 0 , 15 ]

print("Lista original:\n",m)

cres=[]
decres=[]
pares=[]
impares=[]

# a) crescente
copia = [ 15 , 9 , -3 , 7 , 99 , -3 , 0 , -5 , 8 , 15 , -6 , -3 , 99 , 15 , 0 , 15 ]
for i in m:
	a=copia[0]
	for j in copia:
		if j<a:
			prim=j
			a=prim
	cres.append(a)
	copia.remove(a)
print("a) Numeros em ordem crescente:\n",cres)

# b) decrescente
n=(len(cres)-1)
while n!=-1:
	decres.append(cres[n])
	n=n-1
#nao repetidos
n_rep=[]
for i in decres:
	if i not in n_rep:
		n_rep.append(i)
print("b) Numeros em ordem decrescente sem repeticao:\n",n_rep)


# c) pares e impares 
for i in m:
	if i%2==0:
		pares.append(i)
	else:
		impares.append(i)
		
par_n=[]
impar_n=[]

#pares crescente
tam=len(pares)
for i in range (tam):
	a=pares[0]
	for j in pares:
		if j<a:
			prim=j
			a=prim
	par_n.append(a)
	pares.remove(a)

#pares sem repeticao
par=[]
for i in par_n:
	if i not in par:
		par.append(i)


print("c) Numeros pares em ordem crescente e sem repeticao:\n",par)

#impares crescente
tam=len(impares)
for i in range (tam):
	a=impares[0]
	for j in impares:
		if j<a:
			prim=j
			a=prim
	impar_n.append(a)
	impares.remove(a)

#impares sem repeticao
impar=[]
for i in impar_n:
	if i not in impar:
		impar.append(i)

bao = [ 15 , 9 , -3 , 7 , 99 , -3 , 0 , -5 , 8 , 15 , -6 , -3 , 99 , 15 , 0 , 15 ]

#print("c) Impares crescente e sem repeticao:\n",impar)

print("d) Quantas vezes cada numero se repete:")
for i in m:
	a=0
	for j in bao:
		if j==i:
			a=a+1
	if i in bao:
		print("Numero",i, "se repete",a, "vezes")
	while i in bao:
		if i in bao:
			bao.remove(i)

	

		