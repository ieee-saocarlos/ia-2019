import pygame
import math

######################################################_Classes_#########################################################

#Pensado para um player no formato de um círculo
class player(object):
    def __init__(self, x, y, cor):
        """ ATRIBUTOS DA CLASSE """
        self.x = x
        self.y = y
        self.tamanho=23
        self.mx1=round(x/24)
        self.my1=round(y/24)
        self.mx2 = round((x + self.tamanho-1) / 24)
        self.my2 = round((y + self.tamanho-1) / 24)
        self.cor = cor
        self.velx = 0
        self.vely = 0
        self.up=0
        self.down=0
        self.left=0
        self.right=0

    """MÉTODO - MOVIMENTAÇÂO """ 
    #Eu deixei de usar dicionários pq eu tava encontrando dificuldades, mas podemos voltar a usar
    def move(self,esquerda,direita,cima,baixo):
        if (esquerda ==1 and self.left == 1 and self.my1==self.my2):
                self.velx = -2
                self.vely = 0
        else:
            if (direita ==1 and self.right == 1 and self.my1==self.my2):
                self.velx = 2
                self.vely = 0
            else:
                self.velx = 0
        if (cima ==1 and self.up == 1 and self.mx1==self.mx2):
                self.vely = -2
                self.velx = 0
        else:
            if (baixo==1 and self.down == 1 and self.mx1==self.mx2):
                self.vely = 2
                self.velx = 0
            else:
                self.vely = 0
        self.x += self.velx
        self.y += self.vely
        self.mx1 = math.floor(self.x / 24)
        self.my1 = math.floor(self.y / 24)
        self.mx2 = math.floor((self.x+self.tamanho) / 24)
        self.my2 = math.floor((self.y+self.tamanho) / 24)

    def analiseParede(self, mapa):
        if(mapa[self.my1 + 1][self.mx1]==1 and mapa[self.my2+1][self.mx2]==1):
            self.down = 0
            self.vely=0
        else:
            self.down = 1
        if (mapa[self.my1 - 1][self.mx1]==1 and mapa[self.my2-1][self.mx2]==1):
            self.up = 0
            self.vely=0
        else:
            self.up = 1
        if (mapa[self.my1 ][self.mx1+1]==1 and mapa[self.my2][self.mx2+1]==1):
            self.right = 0
            self.velx=0
        else:
            self.right = 1
        if (mapa[self.my1 ][self.mx1-1]==1 and mapa[self.my2][self.mx2-1]==1):
            self.left = 0
            self.velx = 0
        else:
            self.left = 1


    """MÉTODO - DESENHANDO O PLAYER """
    def draw(self, display, cor):
        pygame.draw.rect(display, self.cor, [self.x, self.y, self.tamanho, self.tamanho], 0)




######################################################_Funções_#########################################################

def texto(nomeFont,display,tamanho=100,msg='olá!',ant=True,cor=(100,100,100),pos=[100,100]):
    font = pygame.font.SysFont(nomeFont,tamanho)
    text= font.render(msg,ant,cor)
    display.blit(text,pos)



def print_display(): 
    #PRINTANDO NO DISPLAY
    #count+=1
    # --- #TESTE DE TEXTO:texto(None,display,50,f'{count}',True,(255,0,0),[largura/2+100,altura/2])
    display.fill((0,0,10))
    printMapa(mapa)
    pac.draw(display, amarelo)
    pygame.display.update();
    timer.tick(60)

def geraMapa():
    #0-nada
    #1-paredes
    #2-bolinhas
    #3-bolonas
    #4-portinha dos fantasmas

    mapa = [     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                 [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],#meio
                 [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                 [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                 [1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
                 [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
                 [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
                 [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                 [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                 [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                 [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return mapa

def printMapa(mapa):
    for c in range(36):
        for d in range(28):
            if (mapa[c][d] == 1):
                pygame.draw.rect(display, (0, 0, 100), [d * 24, c * 24, 24, 24], 0)


    


#################################################Programa principal#####################################################

"""VARIAVEIS"""
#GERAIS
mapa=geraMapa()
largura= 224*3
altura= 288*3
sair = True
amarelo =(150,150,0)
fps =60
count=0
esquerda=0
direita=0
cima=0
baixo=0
#------

""""-------------------"""

#INICIALIZAÇÂO DO PYGAME E O DISPLAY
pygame.init()
display = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pac-Man')
timer = pygame.time.Clock()
font = pygame.font.SysFont(None,25)
#-----------------------------------

"""LOOPING DE EVENTOS"""

# Instance da classe player - Pacman
pac = player(int(224*3/2), int(288*3/2)-40, amarelo)

while (sair):
    #ANALISE DAS ENTRADAS DE EVENTOS
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sair = False
        if event.type==pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                esquerda=1
            if (event.key == pygame.K_RIGHT):
                direita = 1
            if (event.key == pygame.K_UP):
                cima = 1
            if (event.key == pygame.K_DOWN):
                baixo = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                esquerda = 0
            if event.key == pygame.K_RIGHT:
                direita = 0
            if event.key == pygame.K_UP:
                cima=0
            if event.key == pygame.K_DOWN:
                baixo=0

    # -------------------------------


    #MOVIMENTAÇÕES
    pac.move(esquerda,direita,cima,baixo)
    pac.analiseParede(mapa)

    # -------------------------------

    #PRINTANDO NO DISPLAY
    count+=1
    print_display()

""""-------------------"""

pygame.quit()

########################################################################################################################