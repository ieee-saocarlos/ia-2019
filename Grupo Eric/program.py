import pygame
import sys
import tijolos
import plataforma
import random


pygame.init()
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 126, 0)
red = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
purple = (255, 0, 255)

size = w, h = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('NPC Breakout')

# Coordenadas dos tijolos
wall = []
for column in range(15):
    for row in range(9):
        if row is not 0:
            wall.append([w/2-25+row*55, h/2-column*20])
        wall.append([w/2-25-row*55, h/2-column*20])

while 1:
    ball_dir = [random.randint(-1, 2), random.randint(-1, 2)]
    if ball_dir is not [0, 0]:
        break

ball_size = [10, 10]
ball_speed = 2.5
ball_pos = [w/2, h/2 + 100]
ball_vel = [x * ball_speed for x in ball_dir]

plat_pos = [w/2, h-5]
plat_mov = 0
speed = 5


def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label


def image(window, image_name, x, y):
    image_v = pygame.image.load(image_name).convert_alpha()
    window.blit(image_v, (x, y))


while True:
    screen.fill(black)

    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

    if ball_pos[0] < 0 or ball_pos[0] > size[0] - ball_size[0]:
        ball_vel[0] = ball_vel[0] * -1
    if ball_pos[1] < 0 or ball_pos[1] > size[1] - ball_size[1] - 5:
        ball_vel[1] = ball_vel[1] * -1

    col = tijolos.draw(ball_pos[0], ball_pos[1], red, screen, wall, ball_size)
    if col is not None:
        # Apaga o tijolo em que a bola colidiu
        wall.pop(col[0])
        if col[1] == 'x':
            ball_vel[0] *= -1
        else:
            ball_vel[1] *= -1

    # draw the ball
    pygame.draw.rect(screen, white, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plat_mov = -speed
            if event.key == pygame.K_RIGHT:
                plat_mov = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plat_mov = 0

    plat_pos[0] += plat_mov
    plataforma.draw(purple, screen, plat_pos, ball_pos)

    clock.tick(60)
    pygame.display.update()

