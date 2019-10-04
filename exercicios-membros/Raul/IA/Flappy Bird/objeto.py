import pyglet

class Objeto:
    def __init__(self, image, xc, yc, gene = None):
        self.sprite = pyglet.sprite.Sprite(image, x=xc, y=yc)
        self.vel = 0

        self.morto = False
        self.pontuacao = 0
        self.pontuado = False
        self.vel_tubo = 120

        self.gene = []
        if gene != None:
            self.gene = gene

    def draw(self):
        self.sprite.draw()

