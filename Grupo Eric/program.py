import pygame
import sys
import objects
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

while 1:
    ball_dir = [random.randint(-1, 2), random.randint(-1, 2)]
    if ball_dir is not [0, 0]:
        break

ball_size = [10, 10]
ball_speed = 3
ball_pos = [w/2, h/2 + 100]
ball_vel = [0, ball_speed]

plat_pos = [w/2 - 50, h - 25]
plat_mov = 0
speed = 5

wall = []

points = 0
level = 0


def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, white)
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
    elif ball_pos[1] < 0:
        ball_vel[1] = ball_vel[1] * -1
    elif ball_pos[1] > size[1] - ball_size[1]:
        ball_vel = [0, 0]

    if not wall:
        level += 1
        # Coordenadas dos tijolos
        wall = []
        for column in range(14):
            for row in range(9):
                if row is not 0:
                    wall.append([w / 2 - 25 + row * 55, h / 2 - column * 20])
                wall.append([w / 2 - 25 - row * 55, h / 2 - column * 20])

    if not (plat_pos[0] < 0 and plat_mov < 0) and not (plat_pos[0] > w - 100 and plat_mov > 0):
        plat_pos[0] += plat_mov

    ric = objects.plat(ball_pos[0], ball_pos[1], purple, screen, plat_pos, ball_size, ball_vel)
    if ric is not None:
        ball_vel[0] = ric[1]
        if ric == 'x':
            ball_vel[0] *= -1
        else:
            ball_vel[1] *= -1

    col = objects.bricks(ball_pos[0], ball_pos[1], red, screen, wall, ball_size, ball_vel)
    if col is not None:
        points += 1
        # Apaga o tijolo em que a bola colidiu
        wall.pop(col[0])
        if col[1] == 'x':
            ball_vel[0] *= -1
        else:
            ball_vel[1] *= -1
    objects.bricks(ball_pos[0], ball_pos[1], red, screen, wall, ball_size, ball_vel)

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

    screen.blit(text('score: ' + str(points)), [10, 10])
    screen.blit(text('level: ' + str(level)), [w - 80, 10])

    clock.tick(60)
    pygame.display.update()