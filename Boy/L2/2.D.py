ingr=[['Arroz',100,5.00],['Carne',100,16.00],['Batata Inglesa',250,3.50],['Cenoura',100,3.00],['Macarrão',200,13.75],['Queijo Minas',150,12.00]]
pratos=[['Muito escondidinho',[['Batata Inglesa',3],['Queijo Minas',1],['Cenoura',1]]],['Pastelão de Vento',[['Batata Inglesa',4],['Carne',1]]],['Misturadão',[['Arroz',4],['Carne',2],['Cenoura',3],['Queijo Minas',2],['Macarrão',3]]],['Marmitex',[['Arroz',3],['Macarrão',2],['Carne',4],['Queijo Minas',1]]]]
sem=[['Muito Escondidinho',13],['Pastelão de Vento',21],['Misturadão',19],['Marmitex',25]]
preco=[]
qs=pratos[:]
ins=[]
insv=[]
for c in range(len(pratos)):
    P=0
    for d in range(len(pratos[c][1])):
        for e in range(len(ingr)):
            if(pratos[c][1][d][0]==ingr[e][0]):
               P+= pratos[c][1][d][1]*ingr[e][1]*ingr[e][2]*0.001
    preco.append([pratos[c][0],float('%.3f'%P)])
print(preco)

for c in range(len(qs)):
    for d in range(len(qs[c][1])):
        qs[c][1][d][1]=qs[c][1][d][1]*sem[c][1]
print(qs)

for c in range(len(qs)):
    for d in range(len(qs[c][1])):
        ins.append(qs[c][1][d])

for c in range(len(ingr)):
    insv.append([ingr[c][0],0])
    for d in range(len(ins)):
        if(ingr[c][0] == ins[d][0]):
            insv[c][1]+=ins[d][1]
print(insv)
D=0
for c in range(len(preco)):
    if(preco[c][1]>D):
        g=preco[c][0]
        D=preco[c][1]
print('o prato mais caro é o',g,'e custa',D)
