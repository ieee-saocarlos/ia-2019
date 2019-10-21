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


def instruction_loop():
    # inicializa o pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen_size = w, h = 1000, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('NPC Breakout')

    while 1:
        image(screen, 'background/instructions.png', 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'main_menu'

        clock.tick(30)
        pygame.display.update()
