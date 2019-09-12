import pyglet
from objeto import Objeto
from random import choice
from math import atan, pi, sin, cos , fabs

class Tela(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(70, 80)

        self.cores = ['vermelha', 'verde', 'roxa', 'rosa', 'laranja',
                      'azul', 'azulado', 'amarela']

        self.frame_rate = 1/120
        self.vel_bolas = 500

        self.imagem_seta = pyglet.image.load(r'imagens\seta.png')
        self.imagem_seta.anchor_y = self.imagem_seta.height // 2

        self.imagem_bola = pyglet.image.load(r'imagens\bola_rosa.png')
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bolas = []

        self.seta = Objeto(self.imagem_seta, 450, 10)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            if y>= 15:
                self.jogar_bola(x, y)
            else:
                self.jogar_bola(x,15)

    def on_mouse_motion(self, x, y, dx, dy):
        if x - self.seta.sprite.x == 0:
            self.seta.sprite.rotation = -90
        else:
            tan = (y - self.seta.sprite.y) / (x - self.seta.sprite.x)
            if x - self.seta.sprite.x > 0:
                self.seta.sprite.rotation = -(atan(tan) * 180 / pi)
            else:
                self.seta.sprite.rotation = (-atan(tan) * 180 / pi) - 180

    def jogar_bola(self, x, y):
        if x != 480:
            tan = (y - 10) / (x - 480)

            self.bolas.append(Objeto(self.imagem_bola, 480, 10))
            if x - 480 > 0:
                self.bolas[-1].vely = self.vel_bolas * sin(atan(tan))
                self.bolas[-1].velx = self.vel_bolas * cos(atan(tan))
            else:
                self.bolas[-1].vely = -self.vel_bolas * sin(atan(tan))
                self.bolas[-1].velx = -self.vel_bolas * cos(atan(tan))
        else:
            self.bolas.append(Objeto(self.imagem_bola, 480, 10))
            self.bolas[-1].vely = self.vel_bolas
            self.bolas[-1].velx = 0

        self.prox_cor = choice(self.cores)

        self.prox_bola = Objeto(self.dicionario[self.prox_cor], 775, 50)

    def update_bolas(self, dt):
        for bola in self.bolas:
            if bola.parada == False:
                bola.sprite.x += bola.velx * dt
                bola.sprite.y += bola.vely * dt
            if bola.sprite.x >=871:
                bola.velx = -fabs(bola.velx)
            if bola.sprite.x <= 29:
                bola.velx=fabs(bola.velx)
            if bola.sprite.y > 871:
                bola.parada=True

    def on_draw(self):
        self.clear()
        self.seta.draw()
        for bola in self.bolas:
            bola.draw()

    def update(self, dt):
        self.update_bolas(dt)

    def dist(self, x1, x2, y1, y2):
        a1 = (x1 - x2) ** 2
        a2 = (y1 - y2) ** 2
        return (a1 + a2) ** 0.5

if __name__ == "__main__":
    win = Tela(900, 900, "Jogo das bolinhas", resizable=False, vsync=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)
    pyglet.app.run()
