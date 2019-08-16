import pygame
######################################################_Funções_#########################################################
"""MOVIMENTAÇÂO"""
#Pac-Man
def pacMov(pos,vel):
    pos['x']+=vel['x']
    pos['y']+=vel['y']
""""-------------------"""



#################################################Programa principal#####################################################

"""VARIAVEIS"""
#GERAIS
largura= 640
altura= 480
sair = True
amarelo =(150,150,0)
#------

#Pac-Man
pacPos={'x':int(largura/2),'y':int(altura/2 +20)}
pacVel={'x':0,'y':0}

""""-------------------"""

#INICIALIZAÇÂO DO PYGAME E O DISPLAY
pygame.init()
display = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pac-Man')

#-----------------------------------

"""LOOPING DE EVENTOS"""

while (sair):

    #ANALISE DAS ENTRADAS DE EVENTOS
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sair = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacVel['x']=-1
            if event.key == pygame.K_RIGHT:
                pacVel['x']=1
            if event.key == pygame.K_UP:
                pacVel['y']=-1
            if event.key == pygame.K_DOWN:
                pacVel['y']=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pacVel['x']=0
            if event.key == pygame.K_RIGHT:
                pacVel['x']=0
            if event.key == pygame.K_UP:
                pacVel['y']=0
            if event.key == pygame.K_DOWN:
                pacVel['y']=0

    # -------------------------------


    #MOVIMENTAÇÕES
    pacMov(pacPos,pacVel)

    # -------------------------------

    #PRINTANDO NO DISPLAY
    display.fill((0,0,10))
    pygame.draw.circle(display, amarelo, [pacPos['x'], pacPos['y']], 10,0)
    pygame.display.update();
    # -----------------------

""""-------------------"""

pygame.quit()

########################################################################################################################