import pyglet


class Objeto:
    def __init__(self, image, xc, yc, gene=None):
        self.sprite = pyglet.sprite.Sprite(image, x=xc, y=yc)

        self.cor = ''

        self.velx = 0
        self.vely = 0
        self.parada = False
        self.tocando = []

        # self.gene = []
        # if gene != None:
        #    self.gene = gene

    def draw(self):
        self.sprite.draw()

