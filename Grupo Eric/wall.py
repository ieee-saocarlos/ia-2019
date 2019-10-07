import pygame


def collision(vertexes, brick, ball_vel):
    past_vert = [0, 0]
    for vert in vertexes:
        if brick[0] < vert[0] < brick[0] + 55 and brick[1] < vert[1] < brick[1] + 15:
            past_vert[0] = vert[0] - ball_vel[0]
            past_vert[1] = vert[1] - ball_vel[1]
            if brick[0] < (vert[0] and past_vert[0]) < brick[0] + 55:
                return 'y'
            elif brick[1] < (vert[1] and past_vert[1]) < brick[1] + 55:
                return 'x'
            else:
                tan = (vert[1] - past_vert[1]) / (vert[0] - past_vert[0])
                if -1 < tan < 1:
                    return 'x'
                else:
                    return 'y'


class Wall:
    def __init__(self, bricks):
        self.bricks = bricks

    def brick(self, color, screen, ball_pos, ball_size, ball_vel):
        i = 0
        vertexes = [[ball_pos[0], ball_pos[1]],
                    [ball_pos[0] + ball_size[0], ball_pos[1]],
                    [ball_pos[0], ball_pos[1] + ball_size[1]],
                    [ball_pos[0] + ball_size[0], ball_pos[1] + ball_size[1]]]

        for brick in self.bricks:
            pygame.draw.rect(screen, color, [brick[0], brick[1], 50, 15])
            r = collision(vertexes, brick, ball_vel)
            if r is not None:
                return i, r
            i += 1

    def gen_wall(self, screen_size, level):
        if int(level*(14/9)) < 14:
            col = int(level*(14/9))
            ro = level
        else:
            col = 14
            ro = 9
        for column in range(col):
            for row in range(ro):
                if row is not 0:
                    self.bricks.append([screen_size[0] / 2 - 25 + row * 55, screen_size[1] / 2 - column * 20])
                self.bricks.append([screen_size[0] / 2 - 25 - row * 55, screen_size[1] / 2 - column * 20])
