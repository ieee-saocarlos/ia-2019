import pygame


def draw(purple, screen, pos, ball_pos):
    pygame.draw.rect(screen, purple, [pos[0], pos[1], 100, 15])


