import pygame
######################################################_Funções_#########################################################
"""MOVIMENTAÇÂO"""
#Pac-Man
def pacMov(pos,vel):
    pos['x']+=vel['x']
    pos['y']+=vel['y']
""""-------------------"""

def texto(nomeFont,display,tamanho=100,msg='olá!',ant=True,cor=(100,100,100),pos=[100,100]):
    font = pygame.font.SysFont(nomeFont,tamanho)
    text= font.render(msg,ant,cor)
    display.blit(text,pos)


#################################################Programa principal#####################################################

"""VARIAVEIS"""
#GERAIS
largura= 224*3
altura= 288*3
sair = True
amarelo =(150,150,0)
fps =60
count=0
#------

#Pac-Man
pacPos={'x':int(largura/2),'y':int(altura/2 +20)}
pacVel={'x':0,'y':0}

""""-------------------"""

#INICIALIZAÇÂO DO PYGAME E O DISPLAY
pygame.init()
display = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pac-Man')
timer = pygame.time.Clock()
font = pygame.font.SysFont(None,25)
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
                pacVel['x']=-2
            if event.key == pygame.K_RIGHT:
                pacVel['x']=2
            if event.key == pygame.K_UP:
                pacVel['y']=-2
            if event.key == pygame.K_DOWN:
                pacVel['y']=2
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
    #TEXTE DE TEXTO:texto(None,display,50,f'{count}',True,(255,0,0),[largura/2+100,altura/2])
    pygame.draw.circle(display, amarelo, [pacPos['x'], pacPos['y']], 12,0)
    pygame.display.update();
    timer.tick(60)
    # -----------------------
    count+=1
""""-------------------"""

pygame.quit()

########################################################################################################################