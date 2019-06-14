arquivo = open('projeto.txt', 'r')
conteudo = arquivo.readlines()
len(conteudo)
arquivo.close()
conteudonome = []
conteudotamanho = []
linhas = []
tabela = ['Nr.', 'Nome', 'Tamanho', '% de uso']
resultado =[]
for linha in conteudo:
    cont = linha.split()
    conteudonome.append(cont[0])
    conteudotamanho.append(cont[1])
    '''resultado.i ='''
for i in range(len(conteudonome)):
    linhas.append(i)
    print(linhas[i], conteudonome[i], conteudotamanho[i])

arquivo = open('projeto.txt', 'w')
arquivo.write("'Nr.', 'Nome', 'Tamanho', '% de uso'")
arquivo.writelines(conteudo)
arquivo.close()






