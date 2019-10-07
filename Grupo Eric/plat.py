import pygame


class Plat:
    def __init__(self, pos, speed, mov):
        self.speed = speed
        self.pos = pos
        self.mov = mov

    def collision(self, color, screen, b_p, b_s, b_v):
        i = 0
        vertexes = [[b_p[0], b_p[1]],
                    [b_p[0] + b_s[0], b_p[1]],
                    [b_p[1], b_p[1] + b_s[1]],
                    [b_p[0] + b_s[0], b_p[1] + b_s[1]]]
        pygame.draw.rect(screen, color, [self.pos[0], self.pos[1], 100, 15])
        past_vert = [0, 0]

        for vert in vertexes:
            if self.pos[0] < vert[0] < self.pos[0] + 100 and self.pos[1] < vert[1] < self.pos[1] + 15:
                past_vert[0] = vert[0] - b_v[0]
                past_vert[1] = vert[1] - b_v[1]
                acc = ((b_p[0] + b_s[0] / 2) - (self.pos[0] + 100 / 2)) / (50 / 3)
                if self.pos[0] < (vert[0] and past_vert[0]) < self.pos[0] + 100:
                    return 'y', acc
                elif self.pos[1] < (vert[1] and past_vert[1]) < self.pos[1] + 15:
                    return 'x', acc
                else:
                    try:
                        tan = (vert[1] - past_vert[1]) / (vert[0] - past_vert[0])
                    except:
                        tan = 0
                    if -1 < tan < 1:
                        return 'x', acc
                    else:
                        return 'y', acc
        i += 1

    def move(self, screen_size):
        if not (self.pos[0] < 0 and self.mov < 0) and not (self.pos[0] > screen_size[0] - 100 and self.mov > 0):
            self.pos[0] += self.mov
