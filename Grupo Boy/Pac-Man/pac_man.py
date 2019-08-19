import pygame

######################################################_Classes_#########################################################

#Pensado para um player no formato de um círculo
class player(object):
    def __init__(self, x, y, cor):
        """ ATRIBUTOS DA CLASSE """
        self.x = x
        self.y = y
        self.cor = cor
        self.velx = 0
        self.vely = 0

    """MÉTODO - MOVIMENTAÇÂO """ 
    #Eu deixei de usar dicionários pq eu tava encontrando dificuldades, mas podemos voltar a usar
    def move(self, x, y, velx, vely):
        self.x += self.velx
        self.y += self.vely

    """MÉTODO - DESENHANDO O PLAYER """
    def draw(self, display, cor):
        pygame.draw.circle(display, self.cor, (self.x, self.y), 12,0)




######################################################_Funções_#########################################################

def texto(nomeFont,display,tamanho=100,msg='olá!',ant=True,cor=(100,100,100),pos=[100,100]):
    font = pygame.font.SysFont(nomeFont,tamanho)
    text= font.render(msg,ant,cor)
    display.blit(text,pos)

    # -----------------------

"""Eu pensei em criar a função pra printar no display e deixar o programa 
principal mais limpo, mas pro teste do texto funcionar precisa adaptar ou deixar de usar a função mesmo"""

def print_display(): 
    #PRINTANDO NO DISPLAY
    #count+=1
    # --- #TESTE DE TEXTO:texto(None,display,50,f'{count}',True,(255,0,0),[largura/2+100,altura/2])
    display.fill((0,0,10))
    pac.draw(display, amarelo)
    pygame.display.update();
    timer.tick(60)

    # -----------------------
    


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
pac = player(int(224*3/2), int(288*3/2), amarelo)

while (sair):

    #ANALISE DAS ENTRADAS DE EVENTOS
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sair = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pac.velx =-2
            if event.key == pygame.K_RIGHT:
                pac.velx =2
            if event.key == pygame.K_UP:
                pac.vely =-2
            if event.key == pygame.K_DOWN:
                pac.vely = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pac.velx =0
            if event.key == pygame.K_RIGHT:
                pac.velx =0
            if event.key == pygame.K_UP:
                pac.vely =0
            if event.key == pygame.K_DOWN:
                pac.vely =0

    # -------------------------------


    #MOVIMENTAÇÕES
    pac.move(pac.x,pac.y,pac.velx,pac.vely)

    # -------------------------------

    #PRINTANDO NO DISPLAY
    count+=1
    print_display()

""""-------------------"""

pygame.quit()

########################################################################################################################