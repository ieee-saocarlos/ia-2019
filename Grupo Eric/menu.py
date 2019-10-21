import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)


def text(string, size):
    font = pygame.font.SysFont("arial", size)
    label = font.render(string, True, black)
    return label


def image(window, image_name, x, y):
    image_v = pygame.image.load(image_name).convert_alpha()
    window.blit(image_v, (x, y))


def menu_loop():
    # inicializa o pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen_size = w, h = 1000, 600
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('NPC Breakout')
    select = 0

    while 1:
        image(screen, 'background/main-menu.png', 0, 0)
        if select == 0:
            pygame.draw.rect(screen, white, [w / 2 - 250, h / 2 + 50, 30, 15])
        else:
            pygame.draw.rect(screen, white, [w / 2 - 250, h / 2 + 170, 30, 15])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    select -= 1
                    select = select % 2
                if event.key == pygame.K_DOWN:
                    select += 1
                    select = select % 2
                if event.key == pygame.K_SPACE:
                    if select == 0:
                        return 'game'
                    else:
                        return 'instruction'

        clock.tick(30)
        pygame.display.update()
