class Ball:
    def __init__(self, size, speed, pos):
        self.size = size
        self.speed = speed
        self.pos = pos
        self.vel = [0, speed]

    def mov(self, screen_size):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]

        if self.pos[0] < 0 or self.pos[0] > screen_size[0] - self.size[0]:
            self.vel[0] = self.vel[0] * -1
        elif self.pos[1] < 0:
            self.vel[1] = self.vel[1] * -1
        elif self.pos[1] > screen_size[1] - self.size[1]:
            self.vel = [0, 0]
