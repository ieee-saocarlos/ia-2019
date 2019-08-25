import pyglet
from objeto import Objeto
from random import choice
from math import atan, pi, sin, cos

class Tela(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(70, 80)

        self.cores = ['vermelha', 'verde', 'roxa', 'rosa', 'laranja',
                      'azul', 'azulado', 'amarela']

        self.frame_rate = 1/60
        self.vel_bolas = 360

        self.imagem_seta = pyglet.image.load(r'imagens\seta.png')
        self.imagem_seta.anchor_y = self.imagem_seta.height // 2

        self.seta = Objeto(self.imagem_seta, 480, 10)

    def on_mouse_motion(self, x, y, dx, dy):
        if x - self.seta.sprite.x == 0:
            self.seta.sprite.rotation = -90
        else:
            tan = (y - self.seta.sprite.y) / (x - self.seta.sprite.x)
            if x - self.seta.sprite.x > 0:
                self.seta.sprite.rotation = -(atan(tan) * 180 / pi)
            else:
                self.seta.sprite.rotation = (-atan(tan) * 180 / pi) - 180

    def on_draw(self):
        self.clear()
        self.seta.draw()

    def update(self, dt):
        pass

    def dist(self, x1, x2, y1, y2):
        a1 = (x1 - x2) ** 2
        a2 = (y1 - y2) ** 2
        return (a1 + a2) ** 0.5

if __name__ == "__main__":
    win = Tela(900, 900, "Jogo das bolinhas", resizable=False, vsync=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)
    pyglet.app.run()
