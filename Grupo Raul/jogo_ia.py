import pyglet
import random
from objeto import Objeto
from random import choice
from math import atan, pi, sin, cos , fabs

class Tela(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(70, 80)

        self.pos_previa = [865, 35]
        self.pos_seta = [450, 30]
        self.bola_previa = None
        self.prev = True
        self.raio = 29
        self.jogada = 0
        self.bola_voando = False

        self.cores = [r'imagens\bola_vermelha.png', r'imagens\bola_rosa.png',r'imagens\bola_amarela.png',r'imagens\bola_verde.png',r'imagens\bola_azul.png']

        self.frame_rate = 1/240
        self.vel_bolas = 600

        self.imagem_seta = pyglet.image.load(r'imagens\seta.png')
        self.imagem_seta.anchor_y = self.imagem_seta.height // 2

        self.imagem_bola = pyglet.image.load(choice(self.cores))
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bola_previa = Objeto(self.imagem_bola, self.pos_previa[0], self.pos_previa[1])

        self.bolas = []

        self.seta = Objeto(self.imagem_seta, self.pos_seta[0], self.pos_seta[1])

    def on_mouse_press(self, x, y, button, modifiers):
        if self.bola_voando == False:
            if button == pyglet.window.mouse.LEFT:
                if y>= 15:
                    self.jogar_bola(x, y)
                else:
                    self.jogar_bola(x,15)

        if button == pyglet.window.mouse.RIGHT:
            for bola in self.bolas:
                print(bola.parada)

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
        if x != 450:
            tan = (y - 10) / (x - 480)

            self.bolas.append(self.nova_bola)
            if x - 480 > 0:
                self.bolas[-1].vely = self.vel_bolas * sin(atan(tan))
                self.bolas[-1].velx = self.vel_bolas * cos(atan(tan))
            else:
                self.bolas[-1].vely = -self.vel_bolas * sin(atan(tan))
                self.bolas[-1].velx = -self.vel_bolas * cos(atan(tan))
        else:
            self.bolas.append(self.nova_bola)
            self.bolas[-1].vely = self.vel_bolas
            self.bolas[-1].velx = 0

        self.prev = True
        self.bola_voando = True


    def testar_colisao(self, bola):
        for bola_2 in self.bolas:
            if bola_2 == bola:
                continue

            raio = self.dist(bola.sprite.x, bola.sprite.y,
                             bola_2.sprite.x, bola_2.sprite.y)

            if raio <= ((2 * self.raio) ** 2):
                return True

    def update_bolas(self, dt):
        if len(self.bolas) > 0:
            if self.bolas[-1].parada:
                self.bola_voando = False
        for bola in self.bolas:
            if self.testar_colisao(bola):
                bola.parada = True
            if bola.parada == False:
                bola.sprite.x += bola.velx * dt
                bola.sprite.y += bola.vely * dt
            if bola.sprite.x >=871:
                bola.velx = -fabs(bola.velx)
            if bola.sprite.x <= 29:
                bola.velx=fabs(bola.velx)
            if bola.sprite.y > 871:
                bola.parada=True

    def previa(self):
        self.nova_bola = self.bola_previa
        self.nova_bola.sprite.x = self.pos_seta[0]
        self.nova_bola.sprite.y = self.pos_seta[1]

        self.imagem_bola = pyglet.image.load(choice(self.cores))
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bola_previa = Objeto(self.imagem_bola, self.pos_previa[0], self.pos_previa[1])

        self.prev = False

    def on_draw(self):
        self.clear()
        self.seta.draw()
        self.nova_bola.draw()
        self.bola_previa.draw()
        for bola in self.bolas:
            bola.draw()

    def update(self, dt):
        if self.prev and self.bola_voando == False:
            self.previa()
        self.update_bolas(dt)

    def dist(self, x1, y1, x2, y2):
        a1 = (x1 - x2) ** 2
        a2 = (y1 - y2) ** 2
        return (a1 + a2)

if __name__ == "__main__":
    win = Tela(900, 900, "Jogo das bolinhas", resizable=False, vsync=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)
    pyglet.app.run()