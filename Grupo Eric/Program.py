import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

size = width, height = 600, 600
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

    pygame.draw.rect(screen, white, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(30)
    pygame.display.update()

