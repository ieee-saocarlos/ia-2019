import pygame
import sys
import tijolos
import plataforma

pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
laranja = (255, 126, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
roxo = (255, 0, 255)

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('NPC Breakout')

ball_size = [10, 10]
ball_pos = [320, 180]
ball_vel = [5, -5]

def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label

def image(window, imageName, x, y):
    image = pygame.image.load(imageName).convert_alpha()
    window.blit(image, (x, y))

while True:
    screen.fill(black)

    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

    if ball_pos[0] == 0 or ball_pos[0] == size[0] - ball_size[0]:
        ball_vel[0] = ball_vel[0] * -1
    if ball_pos[1] == 0 or ball_pos[1] == size[1] - ball_size[1]:
        ball_vel[1] = ball_vel[1] * -1

    tijolos.desenhar(ball_pos[0], ball_pos[1], vermelho, screen)


    # desenha a bola
    pygame.draw.rect(screen, white, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plataforma.movement = -1 * plataforma.speed
            if event.key == pygame.K_RIGHT:
                plataforma.movement = plataforma.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plataforma.movement = 0

    plataforma.desenhar(roxo, screen)

    clock.tick(30)
    pygame.display.update()

