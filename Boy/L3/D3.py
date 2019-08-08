"""Sudoku é um jogo de lógica de números com o intuito de preencher todos as posições com números de 1 a 9,
não podendo repetir o mesmo número na mesma linha, na mesma coluna e no mesmo quadrado (dos 9 presentes no sudoku).
A partir do sudoku abaixo, faça um programa que resolva o mesmo,
preenchendo os espaços vazios, e imprima a multiplicação dos 5 últimos números da primeira linha.
"""

def analise(l,c,mapa,quadrados):
    if(mapa[l][c]==0):
        q=qualQuadrado(l,c)
        setAnalise={0}
        for i in range (9):
            if(mapa[l][i]!=0):
                set1={mapa[l][i]}
                setAnalise = setAnalise.union(set1)
            if (mapa[i][c] != 0):
                set1 = {mapa[i][c]}
                setAnalise = setAnalise.union(set1)
            if(quadrados[q][i]!=0):
                set1 = {quadrados[q][i]}
                setAnalise = setAnalise.union(set1)
        lista=list(setAnalise)
        if(len(lista)<9):
            return 0
        if(len(lista)==9):
            for k in range(9):

                set1={k+1}
                if(setAnalise.union(set1)!=setAnalise):
                    mapa[l][c] = k+1
                    constroiQuadrado(quadrados, mapa)
                    return 1





def qualQuadrado(l,c):

    if (c >= 0 and c <= 2):
        if (l >= 0 and l <= 2):
            return 0
        if (l >= 3 and l <= 5):
            return 1
        if (l >= 6 and l <= 8):
            return 2
    if (c >= 3 and c <= 5):
        if (l >= 0 and l <= 2):
            return 3
        if (l >= 3 and l <= 5):
            return 4
        if (l >= 6 and l <= 8):
            return 5

    if (c >= 6 and c <= 8):
        if (l >= 0 and l <= 2):
            return 6
        if (l >= 3 and l <= 5):
            return 7
        if (l >= 6 and l <= 8):
            return 8





def entradaMapa(mapa):
   for c in range(9):
       print("Coloque 0 para indeterminado.")
       for d in range (9):
            mapa[c].append(int(input(f'Insira o valor da casa {d+1} da linha {c+1}:')))
            if(mapa[c][d]<0 or mapa[c][d]>9):
                print("Número inválido!!!")
                (f'Insira o valor da casa {d+1} da linha {c+1} novamente:')
                mapa[c][d]=int(input(f'Insira o valor da casa {d+1} da linha {c+1} novamente:'))


def constroiQuadrado(quadrados,mapa,i=0,k=0):
    if (i+1<=3):
        q=0
    if (i + 1 <= 6 and i+1>3):
        q=3
    if (i+1<=9 and i+1>6):
        q=6

    for c in range (9):
        quadrados[i][c]=mapa[k][(c%3)+q]
        if((c+1)%3==0):
            k+=1
    if(i<8):
        if(k<9):
            constroiQuadrado(quadrados, mapa, i+1, k)
        else:
            constroiQuadrado(quadrados, mapa, i+1)

def printMapa(mapa):
    for c in range (9):
        print()
        if (c % 3 == 0 and c!= 9 and c!=0):
            print("----------------------")
        for d in range(9):
            print(mapa[c][d],end=" ")
            if((d+1)%3==0 and d+1!=9):
                print('|', end=" ")


#mapa=[[],[],[],[],[],[],[],[],[]]
#entradaMapa(mapa)
mapa=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
quadrados=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
constroiQuadrado(quadrados, mapa)
printMapa(mapa)
print()
print()
k=1
while (k>0):
    k=0
    for l in range (9):
        for c in range (9):
            analise(l,c,mapa,quadrados)
            if(mapa[l][c]==0):
                k+=1

printMapa(mapa)
