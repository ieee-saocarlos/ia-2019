import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)


def text(string, size):
    font = pygame.font.SysFont("comicsansMS", size)
    label = font.render(string, True, white)
    return label

def text_shadow(string, size):
    font = pygame.font.SysFont("comicsansMS", size)
    label = font.render(string, True, (8, 2, 19))
    return label


def image(window, image_name, x, y):
    image_v = pygame.image.load(image_name).convert_alpha()
    window.blit(image_v, (x, y))


def over_loop(points):
    pygame.init()
    clock = pygame.time.Clock()
    screen_size = w, h = 1000, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('NPC Breakout')

    while 1:
        image(screen, 'background/game-over.png', 0, 0)
        screen.blit(text_shadow(points, 50), [w / 2 + 45, h / 2 - 55])
        screen.blit(text(points, 50), [w/2 + 40, h/2 - 65])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    sys.exit()
                if event.key == pygame.K_r:
                    return 'game'
                if event.key == pygame.K_m:
                    return 'main_menu'

        clock.tick(60)
        pygame.display.update()
