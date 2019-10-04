file= open('nomes.txt','r')
nn=[]
mnn=[]
c=0
T=0
for line in file:
    nn.append(line)
    mnn.append(nn[c].split(' '))
    mnn[c][1] = mnn[c][1].split("\n")
    T+=float(mnn[c][1][0])
    c+=1

file.close()
file = open('nomes2.txt','w')
file.write('Nr. Usuários Espaço utilizado %do uso\n\n')

for c in range (len(mnn)):
    file.write(str(c))
    file.write('    ')
    file.write(str(mnn[c][0]))
    file.write('      ')
    file.write(str(round(float(mnn[c][1][0])/(2**20),2)))
    file.write('Mb     ')
    file.write(str(round(100*(float(mnn[c][1][0]))/T,2)))
    file.write('%\n')

file.write('\n')
file.write('Espaço total ocupado: ')
file.write(str(round(T/(2**20),2)))
file.write(' Mb\n')

file.write('Espaço médio ocupado:')
file.write(str(round(T/((c+1)*(2**20)),2)))
file.write(' Mb')
file.close()