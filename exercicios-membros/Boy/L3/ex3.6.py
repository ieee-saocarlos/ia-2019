"""oito rainhas"""

def analisePosição(nc,nl,pr):#nc = número da coluna =número de rainhas postas. nl=número da linha a ser analisada . pr= vetor da main.
    for c in range (nc):
        if(pr[c]==nl):#analisando se está na mesma linha.
            return -1
        if(nc - c == pr[c]-nl or nc - c == -(pr[c]-nl)):#analisando se está na mesma diagonal.
            return -1
    return 1


def colocaRainha(nc,pr,i=0):
    for d in range(pr[nc]+i,8):
        if(analisePosição(nc, d, pr) == 1):
            pr[nc] = d
            return 1
    tiraRainha(nc - 1, pr)
    colocaRainha(nc, pr)


def tiraRainha(nc,pr):
    colocaRainha(nc,pr,1)
    pr[nc+1]=0



def funcaoAuxiliar(x=0):
    for c in range(x,8):
        if (colocaRainha(c, pr) == -1):
            tiraRainha(c-1, pr)
            funcaoAuxiliar(c)
            return 1


pr=[0,0,0,0,0,0,0,0]#Número da linha de cada rainha(de 0 a 7). A coluna é representada pela posição na lista já que são apenas 8 colunas.
funcaoAuxiliar(0)

print(pr)
