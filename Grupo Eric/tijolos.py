import pygame


def draw(x, y, red, screen, wall, ball_size):
    i = 0
    vertexes = [[x, y], [x + ball_size[0], y], [x, y + ball_size[1]], [x + ball_size[0], y + ball_size[1]]]

    for brick in wall:
        for vertex in vertexes:
            pygame.draw.rect(screen, red, [brick[0], brick[1], 50, 15])
            if brick[0] < vertex[0] < brick[0] + 55 and brick[1] < vertex[1] < brick[1] + 15:
                if abs(vertex[0] - brick[0] < vertex[1] - brick[1]):
                    return i, 'x'
                else:
                    return i, 'y'
        i += 1
