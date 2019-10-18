import pygame

def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, white)
    return label

class PowerUp:
    def __init__(self, pos):
        self.size = [10, 10]
        self.speed = 3
        self.pos = pos
        self.power_usp = power_ups = []

    def drop(self, screen, w, h):
        screen.blit(text('INSTRUÇÕES', 50), [w / 2 - 150, h / 2 - 50])
