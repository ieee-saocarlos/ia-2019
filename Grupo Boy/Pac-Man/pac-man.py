import pygame

#VARIAVEIS
largura= 640
altura= 480
sair = True

#-------------------

#INICIALIZAÇÂO DO PYGAME E O DISPLAY
pygame.init()
pygame.display.set_mode((640,480))
pygame.display.set_caption('Pac-Man')

#=-----------------------------------

#LOOPING DE EVENTOD

while (sair):
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sair = False

    pygame.display.update();

pygame.quit()