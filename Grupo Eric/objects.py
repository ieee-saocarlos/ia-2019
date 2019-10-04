import pygame


def colision(i, vertexes, brick, ball_vel):
    past_vert = [0, 0]
    for vert in vertexes:
        if brick[0] < vert[0] < brick[0] + 55 and brick[1] < vert[1] < brick[1] + 15:
            past_vert[0] = vert[0] - ball_vel[0]
            past_vert[1] = vert[1] - ball_vel[1]
            tan = (vert[1] - past_vert[1]) / (vert[0] - past_vert[1])
            if brick[0] < (vert[0] and past_vert[0]) < brick[0] + 55:
                return i, 'y'
            elif brick[1] < (vert[1] and past_vert[1]) < brick[1] + 55:
                return i, 'x'
            else:
                if -1 < tan < 1:
                    return i, 'x'
                else:
                    return i, 'y'


def bricks(x, y, red, screen, wall, ball_size, ball_vel):
    i = 0
    vertexes = [[x, y], [x + ball_size[0], y], [x, y + ball_size[1]], [x + ball_size[0], y + ball_size[1]]]

    for brick in wall:
        pygame.draw.rect(screen, red, [brick[0], brick[1], 50, 15])
        r = colision(i, vertexes, brick, ball_vel)
        if r is not None:
            return r
        i += 1

def plat(purple, screen, pos, ball_pos):
    pygame.draw.rect(screen, purple, [pos[0], pos[1], 100, 15])