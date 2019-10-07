import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)


def text(string, size):
    font = pygame.font.SysFont("arial", size)
    label = font.render(string, True, white)
    return label


def image(window, image_name, x, y):
    image_v = pygame.image.load(image_name).convert_alpha()
    window.blit(image_v, (x, y))


def menu_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen_size = w, h = 1000, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('NPC Breakout')

    while 1:
        screen.fill(black)
        screen.blit(text('BREAKOUT', 50), [w/2 - 150, h/2 - 50])
        screen.blit(text("aperte 's' para começar", 20), [w/2 - 115, h/2 + 25])
        screen.blit(text("aperte 'r' para recomeçar o jogo", 20), [w/2 - 115, h / 2 + 45])
        screen.blit(text("aperte 'x' para sair", 20), [w/2 - 115, h / 2 + 65])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    sys.exit()
                if event.key == pygame.K_s:
                    return 'game'

        clock.tick(30)
        pygame.display.update()
