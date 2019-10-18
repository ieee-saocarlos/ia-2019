import pygame
import sys
import random
from ball import Ball
from plat import Plat
from wall import Wall
from power_up import PowerUp

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 126, 0)
red = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
purple = (255, 0, 255)


def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, white)
    return label


def image(window, image_name, x, y):
    image_v = pygame.image.load(image_name).convert_alpha()
    window.blit(image_v, (x, y))


def game_loop():
    # initialize
    status = 'level_start'
    pygame.init()
    clock = pygame.time.Clock()
    screen_size = w, h = 1000, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('NPC Breakout')
    option = 'game'
    pause = 0

    # main ball initial state
    main_ball = Ball(size=[10, 10], speed=5, pos=[w / 2, h / 2 + 100])

    # main plat initial state
    main_plat = Plat(pos=[w / 2 - 50, h - 25], speed=5, mov=0)

    # initialize wall
    wall = Wall(bricks=[])

    # initialize power_ups
    #power_up = PowerUp()

    # initialize score
    points = 0
    level = 0

    while option is not 'game_over':
        screen.fill(black)

        if not wall.bricks:
            level += 1
            wall.gen_wall(screen_size, level)
            status = 'level_start'

        if pause == 0:
            option = main_ball.move(screen_size, screen, white, main_ball.pos, main_ball.size, status, main_plat.pos)
            main_plat.move(screen_size)

        # colisao com a plataforma
        ric = main_plat.collision(purple, screen, main_ball.pos, main_ball.size, main_ball.vel)
        if ric is not None:
            main_ball.vel[0] = ric[1]
            if ric == 'x':
                main_ball.vel[0] *= -1
            else:
                main_ball.vel[1] *= -1

        # colisao com o tijolo
        col = wall.brick(red, screen, main_ball.pos, main_ball.size, main_ball.vel)
        if col is not None:
            points += 1
            # Drops power up after brick os destroyed
            #if random.randint(0, 7) == 0:
            #    power_ups.append(wall.bricks(col[0]), 0)
            # Apaga o tijolo em que a bola colidiu
            wall.bricks.pop(col[0])

            # para redesenhar apos apagar o tijolo
            wall.brick(red, screen, main_ball.pos, main_ball.size, main_ball.vel)
            if col[1] == 'x':
                main_ball.vel[0] *= -1
            else:
                main_ball.vel[1] *= -1

        # Draws power up
        #for obj in power_ups:
        #    obj.drop(screen, w, h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    main_plat.mov = -main_plat.speed
                elif event.key == pygame.K_RIGHT:
                    main_plat.mov = main_plat.speed
                elif event.key == pygame.K_r:
                    return 'game'
                elif event.key == pygame.K_x:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    status = 0
                elif event.key == pygame.K_p:
                    pause = ~pause
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    main_plat.mov = 0

        if pause is not 0:
            screen.blit(text('Paused'), [w / 2, h / 2])
            pygame.draw.rect(screen, white, [main_ball.pos[0], main_ball.pos[1], main_ball.size[0], main_ball.size[1]])

        screen.blit(text('score: ' + str(points)), [10, 10])
        screen.blit(text('level: ' + str(level)), [w - 80, 10])

        clock.tick(60)
        pygame.display.update()
    return 'game_over'
