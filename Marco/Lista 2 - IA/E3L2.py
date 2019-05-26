# Faça um programa que a partir da lista [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] imprima:
# a) Uma lista com somente números pares.
# b) Uma lista com somente números  ímpares.
# c) Uma lista inversa a lista inicial (sem uso de comandos prontos como reverse).
# d) Uma lista com somente números primos.

m=[1,2,3,4,5,6,7,8,9,10]
pares=[]
impares=[]
inversa=[]
primos=[]

#pares e impares
for i in m:
	if i%2==0:
		pares.append(i)
	else:
		impares.append(i)
		
#inversa
n=9
while n!=-1:
	inversa.append(m[n])
	n=n-1

#primos
for i in m:
	mult=0
	for count in range (2,i):
		if(i%count==0):
			mult=1
		
	if mult==0 and i!=1:
		primos.append(i)

print("Lista original:",m)	
print("As listas pares, impares, inversa e de primos formadas, foram, respectivamemte:\n",pares,impares,inversa,primos)

		
	
	