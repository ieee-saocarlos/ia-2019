import pygame


def colision(vertexes, brick, ball_vel):
    past_vert = [0, 0]
    for vert in vertexes:
        if brick[0] < vert[0] < brick[0] + 55 and brick[1] < vert[1] < brick[1] + 15:
            past_vert[0] = vert[0] - ball_vel[0]
            past_vert[1] = vert[1] - ball_vel[1]
            tan = (vert[1] - past_vert[1]) / (vert[0] - past_vert[1])
            if brick[0] < (vert[0] and past_vert[0]) < brick[0] + 55:
                return 'y'
            elif brick[1] < (vert[1] and past_vert[1]) < brick[1] + 55:
                return 'x'
            else:
                if -1 < tan < 1:
                    return 'x'
                else:
                    return 'y'


def bricks(x, y, red, screen, wall, ball_size, ball_vel):
    i = 0
    vertexes = [[x, y], [x + ball_size[0], y], [x, y + ball_size[1]], [x + ball_size[0], y + ball_size[1]]]

    for brick in wall:
        pygame.draw.rect(screen, red, [brick[0], brick[1], 50, 15])
        r = colision(vertexes, brick, ball_vel)
        if r is not None:
            return i, r
        i += 1


def plat(x, y, purple, screen, plat_pos, ball_size, ball_vel):
    i = 0
    vertexes = [[x, y], [x + ball_size[0], y], [x, y + ball_size[1]], [x + ball_size[0], y + ball_size[1]]]
    pygame.draw.rect(screen, purple, [plat_pos[0], plat_pos[1], 100, 15])
    past_vert = [0, 0]

    for vert in vertexes:
        if plat_pos[0] < vert[0] < plat_pos[0] + 100 and plat_pos[1] < vert[1] < plat_pos[1] + 15:
            past_vert[0] = vert[0] - ball_vel[0]
            past_vert[1] = vert[1] - ball_vel[1]
            tan = (vert[1] - past_vert[1]) / (vert[0] - past_vert[1])
            if plat_pos[0] < (vert[0] and past_vert[0]) < plat_pos[0] + 55:
                return 'y'
            elif plat_pos[1] < (vert[1] and past_vert[1]) < plat_pos[1] + 55:
                return 'x'
            else:
                if -1 < tan < 1:
                    return 'x'
                else:
                    return 'y'
    i += 1
