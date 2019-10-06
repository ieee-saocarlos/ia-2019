import pygame
import sys
from ball import Ball
from plat import Plat
from wall import Wall

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 126, 0)
red = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
purple = (255, 0, 255)

# initialize
pygame.init()
clock = pygame.time.Clock()

screen_size = w, h = 1000, 600
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('NPC Breakout')

# main ball initial state
main_ball = Ball(size=[10, 10], speed=3, pos=[w / 2, h / 2 + 100])

# main plat initial state
main_plat = Plat(pos=[w / 2 - 50, h - 25], speed=5, mov=0)

# initialize wall
wall = Wall(bricks=[])

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

    if not wall.bricks:
        level += 1
        for column in range(14):
            for row in range(9):
                if row is not 0:
                    wall.bricks.append([w / 2 - 25 + row * 55, h / 2 - column * 20])
                wall.bricks.append([w / 2 - 25 - row * 55, h / 2 - column * 20])

    main_ball.mov(screen_size)

    if not (main_plat.pos[0] < 0 and main_plat.mov < 0) and not (main_plat.pos[0] > w - 100 and main_plat.mov > 0):
        main_plat.pos[0] += main_plat.mov

    ric = main_plat.collision(purple, screen, main_ball.pos, main_ball.size, main_ball.vel)
    if ric is not None:
        main_ball.vel[0] = ric[1]
        if ric == 'x':
            main_ball.vel[0] *= -1
        else:
            main_ball.vel[1] *= -1

    col = wall.brick(red, screen, main_ball.pos, main_ball.size, main_ball.vel)
    if col is not None:
        points += 1
        # Apaga o tijolo em que a bola colidiu
        wall.bricks.pop(col[0])
        if col[1] == 'x':
            main_ball.vel[0] *= -1
        else:
            main_ball.vel[1] *= -1

    col = wall.brick(red, screen, main_ball.pos, main_ball.size, main_ball.vel)

    # draw the ball
    pygame.draw.rect(screen, white, [main_ball.pos[0], main_ball.pos[1], main_ball.size[0], main_ball.size[1]])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_plat.mov = -main_plat.speed
            if event.key == pygame.K_RIGHT:
                main_plat.mov = main_plat.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                main_plat.mov = 0

    screen.blit(text('score: ' + str(points)), [10, 10])
    screen.blit(text('level: ' + str(level)), [w - 80, 10])

    clock.tick(60)
    pygame.display.update()
