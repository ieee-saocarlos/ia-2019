sudoku = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9],
]


a = 0
soma = 0

possibilidades_numeros = [[],[],[],[],[],[],[],[],[]]
testar_colocar = [0,0,0,0,0,0,0,0,0]
testar_tirar = [0,0,0,0,0,0,0,0,0]

sudoku_posicoes = []

verificar_9 = []


def determinar_numeros(posicao):
    for i in range(0,9):
        if testar_colocar[i] == 9 and posicao not in possibilidades_numeros[i]:
            possibilidades_numeros[i].append(posicao)

        if testar_tirar[i] != 9 and posicao in possibilidades_numeros[i]:
            possibilidades_numeros[i].remove(posicao)

    for x in range(0,9):
        testar_tirar[x] = 0
        testar_colocar[x] = 0



def apresentar_posicoes(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                sudoku_posicoes.append((i*9) + j)

    for i in sudoku_posicoes:
        linha = (i - (i % 9))//9
        coluna = i % 9
        for p in range(0,9):
            for numero in range(0,9):
                if sudoku[linha][p] != numero + 1:
                    testar_colocar[numero] += 1

                if sudoku[p][coluna] != numero + 1:
                    testar_tirar[numero] += 1

        determinar_numeros(i)

        u = 3
        v = 3

        while u < 10:
            if (linha >= u - 3) and (linha < u) and (coluna >= v - 3) and (coluna < v):
                for x in range(u - 3, u):
                    for y in range(v - 3, v):
                        for numero in range(0,9):
                            if sudoku[x][y] != numero + 1:
                                testar_tirar[numero] += 1


                determinar_numeros(i)

            v += 3
            if v > 9:
                u += 3
                v = 3





def backtracking(k, sudoku):
    global a
    if k == len(sudoku_posicoes):
        printar_sudoku(sudoku)
        print (sudoku[0][-1] * sudoku[0][-2] * sudoku[0][-3] * sudoku[0][-4] * sudoku[0][-5])
        a = 1
        return 0
    else:
        for i in range(1,10):
            if a == 1:
                return 0
            sudoku[(sudoku_posicoes[k] - (sudoku_posicoes[k] % 9)) // 9][(sudoku_posicoes[k] % 9)] = i
            if sudoku_posicoes[k] in possibilidades_numeros[i-1]:
                if validar(k, sudoku) == 1:
                    if (i == 9) and (sudoku_posicoes[k] not in verificar_9):
                        verificar_9.append(sudoku_posicoes[k])

                    backtracking(k + 1, sudoku)

                else:
                    sudoku[(sudoku_posicoes[k] - (sudoku_posicoes[k] % 9)) // 9][(sudoku_posicoes[k] % 9)] = 0

            else:
                sudoku[(sudoku_posicoes[k] - (sudoku_posicoes[k] % 9)) // 9][(sudoku_posicoes[k] % 9)] = 0

        if sudoku_posicoes[k] in verificar_9:
            sudoku[(sudoku_posicoes[k] - (sudoku_posicoes[k] % 9)) // 9][(sudoku_posicoes[k] % 9)] = 0




def printar_sudoku(sudoku):
    print (sudoku[0][0], sudoku[0][1], sudoku[0][2],'',sudoku[0][3], sudoku[0][4], sudoku[0][5],'', sudoku[0][6], sudoku[0][7], sudoku[0][8])
    print (sudoku[1][0], sudoku[1][1], sudoku[1][2],'',sudoku[1][3], sudoku[1][4], sudoku[1][5],'', sudoku[1][6], sudoku[1][7], sudoku[1][8])
    print (sudoku[2][0], sudoku[2][1], sudoku[2][2],'',sudoku[2][3], sudoku[2][4], sudoku[2][5],'', sudoku[2][6], sudoku[2][7], sudoku[2][8])
    print ('')
    print (sudoku[3][0], sudoku[3][1], sudoku[3][2],'',sudoku[3][3], sudoku[3][4], sudoku[3][5],'', sudoku[3][6], sudoku[3][7], sudoku[3][8])
    print (sudoku[4][0], sudoku[4][1], sudoku[4][2],'',sudoku[4][3], sudoku[4][4], sudoku[4][5],'', sudoku[4][6], sudoku[4][7], sudoku[4][8])
    print (sudoku[5][0], sudoku[5][1], sudoku[5][2],'',sudoku[5][3], sudoku[5][4], sudoku[5][5],'', sudoku[5][6], sudoku[5][7], sudoku[5][8])
    print ('')
    print (sudoku[6][0], sudoku[6][1], sudoku[6][2],'',sudoku[6][3], sudoku[6][4], sudoku[6][5],'', sudoku[6][6], sudoku[6][7], sudoku[6][8])
    print (sudoku[7][0], sudoku[7][1], sudoku[7][2],'',sudoku[7][3], sudoku[7][4], sudoku[7][5],'', sudoku[7][6], sudoku[7][7], sudoku[7][8])
    print (sudoku[8][0], sudoku[8][1], sudoku[8][2],'',sudoku[8][3], sudoku[8][4], sudoku[8][5],'', sudoku[8][6], sudoku[8][7], sudoku[8][8])
    print ('\n'*2)






def validar(k, sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                continue
            for x in range(0,9):
                if (sudoku[i][j] == sudoku[i][x]) and (x != j):
                    return 0

                if (sudoku[i][j] == sudoku[x][j]) and (x != i):
                    return 0




    for i in range(0,3):
        for j in range(0,3):
            if sudoku[i][j] == 0:
                continue
            for x in range(0,3):
                for y in range(0,3):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(0,3):
        for j in range(3,6):
            if sudoku[i][j] == 0:
                continue
            for x in range(0,3):
                for y in range(3,6):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(0,3):
        for j in range(6,9):
            if sudoku[i][j] == 0:
                continue
            for x in range(0,3):
                for y in range(6,9):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0





    for i in range(3,6):
        for j in range(0,3):
            if sudoku[i][j] == 0:
                continue
            for x in range(3,6):
                for y in range(0,3):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(3,6):
        for j in range(3,6):
            if sudoku[i][j] == 0:
                continue
            for x in range(3,6):
                for y in range(3,6):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(3,6):
        for j in range(6,9):
            if sudoku[i][j] == 0:
                continue
            for x in range(3,6):
                for y in range(6,9):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0





    for i in range(6,9):
        for j in range(0,3):
            if sudoku[i][j] == 0:
                continue
            for x in range(6,9):
                for y in range(0,3):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(6,9):
        for j in range(3,6):
            if sudoku[i][j] == 0:
                continue
            for x in range(6,9):
                for y in range(3,6):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0

    for i in range(6,9):
        for j in range(6,9):
            if sudoku[i][j] == 0:
                continue
            for x in range(6,9):
                for y in range(6,9):
                    if (sudoku[i][j] == sudoku[x][y]) and ((i != x) or (j != y)) and (sudoku[i][j] != 0):
                        return 0


    return 1




printar_sudoku(sudoku)
apresentar_posicoes(sudoku)
backtracking(0, sudoku)  #1008
