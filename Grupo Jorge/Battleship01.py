import sys
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
my = 0
mx = 0
dx = 50
dy = 50
Alvos = []

Eixo = ['Horizontal', 'Vertical']
a = []
for b in range(50, 451, 50):
    for c in range(50, 451, 50):
        a.append((c, b))

size = width, height = 680, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Battleship')

for i in range(10):
        pygame.draw.line(screen, white,(50,dy),(500,dy))  #horizontal jogador 1
        pygame.draw.line(screen, white,(dx,50),(dx,500))  #vertical jogador 1

        dy += 50
        dx += 50

#arrumar essa merda
class Barco():
    def barco (self, tamanho, quantidade):
        Pos = []
        if(quantidade != 0):
            for n in range(quantidade):
                rpos = random.choice(a)
                xpos = rpos[0]
                ypos = rpos[1]
                a.remove(rpos)
                dir = random.choice(Eixo)
                if (tamanho != 0):
                    if(dir == 'Horizontal'):
                        for p in range(tamanho):
                            if(xpos + 50*p <= 450):
                                Pos.extend([(xpos + 50*p, ypos)])
                            elif(xpos + 50*p > 450):
                                Pos.extend([(xpos - 50*p, ypos)])
                    elif(dir == 'Vertical'):
                        for q in range(tamanho):
                            if(ypos + 50*q <= 450):
                                Pos.extend([(xpos, ypos + 50*q)])
                            elif(ypos + 50*q > 450):
                                Pos.extend([(xpos, ypos - 50*q)])
                else:
                    continue
        else:
            pass
        return Pos


B = Barco()
b1 = B.barco(1, 1)
Alvos.extend(b1)
b2 = B.barco(2, 2)
Alvos.extend(b2)
b3 = B.barco(3, 2)
Alvos.extend(b3)
b4 = B.barco(4, 2)
Alvos.extend(b4)
b5 = B.barco(5, 1)
Alvos.extend(b5)
b6 = B.barco(6, 1)
Alvos.extend(b6)

print(Alvos)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            my = pygame.mouse.get_pos()[1]
            mx = pygame.mouse.get_pos()[0]
        for i in range(50, 351, 150):
            if (my >= i and my < i + 150):
                for j in range(i, i + 101, 50):
                    if (my >= j and my < j + 50):
                        my = j
                    else:
                        continue
            else:
                continue
        for k in range(50, 351, 150):
            if (mx >= k and mx < k + 150):
                for l in range(k, k + 101, 50):
                    if (mx >= l and mx < l + 50):
                        mx = l
                    else:
                        continue
            else:
                continue
        if ((mx, my) in Alvos):
            for y in range(len(Alvos)):
                if (mx == Alvos[y][0] and my == Alvos[y][1]):
                    screen.fill(red, rect=(mx, my, 50, 50))
                elif (mx == 0 and my == 0):
                    continue
                elif (mx > 500 or mx < 50 or my > 500 or my < 50):
                    continue
                else:
                    continue
        elif (mx == 0 and my == 0):
            continue
        elif (mx >= 500 or mx < 50 or my >= 500 or my < 50):
            continue
        else:
            screen.fill(blue, rect=(mx, my, 50, 50))
    clock.tick(60)
    pygame.display.update()