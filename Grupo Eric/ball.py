import pygame


class Ball:
    def __init__(self, size, speed, pos):
        self.size = size
        self.speed = speed
        self.pos = pos
        self.vel = [0, speed]

    def move(self, screen_size, screen, color, ball_pos, ball_size):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]

        if self.pos[0] < 0 or self.pos[0] > screen_size[0] - self.size[0]:
            self.vel[0] = self.vel[0] * -1
        elif self.pos[1] < 0:
            self.vel[1] = self.vel[1] * -1
        elif self.pos[1] > screen_size[1] - self.size[1]:
            self.vel = [0, 0]
            pygame.draw.rect(screen, color, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])
            return 'game_over'

        pygame.draw.rect(screen, color, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])
