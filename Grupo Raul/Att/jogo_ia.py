import pyglet
import random
from objeto import Objeto
from random import choice
from math import atan, pi, sin, cos , fabs


class Tela(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(70, 80)

        self.dicionario_cores = {r'imagens\bola_vermelha.png':'vermelha',
                                 r'imagens\bola_rosa.png':'rosa',
                                 r'imagens\bola_amarela.png':'amarela',
                                 r'imagens\bola_verde.png':'verde',
                                 r'imagens\bola_azul.png':'azul'}

        self.cores = [r'imagens\bola_vermelha.png',
                      r'imagens\bola_rosa.png',
                      r'imagens\bola_amarela.png',
                      r'imagens\bola_verde.png',
                      r'imagens\bola_azul.png']
       # if self.pont >=5000:
          #  self.cores.append(r'imagens\bola_Raul.png')
     #   if self.pont >=10000:
        #    self.cores.append(r'imagens\bola_Raul.png')

        self.iniciar()

    def iniciar(self):

        self.pos_previa = [865, 35]
        self.pos_seta = [450, 30]
        self.bola_previa = None
        self.prev = True
        self.raio = 29
        self.jogada = 0
        self.bola_voando = False
        self.explodiu = False
        self.erros = 0
        self.vez = 0
        self.pont = 0

        self.perdeu = False

        self.frame_rate = 1 / 120
        self.vel_bolas = 800

        self.imagem_seta = pyglet.image.load(r'imagens\seta.png')
        self.imagem_seta.anchor_y = self.imagem_seta.height // 2

        cor = choice(self.cores)
        cor_1 = self.dicionario_cores[cor]

        self.imagem_bola = pyglet.image.load(cor)
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bola_previa = Objeto(self.imagem_bola, self.pos_previa[0], self.pos_previa[1])
        self.bola_previa.cor = cor_1

        self.label_pontuacao = pyglet.text.Label('Pontuação : ' + str(self.pont),
                                                 x = 20, y = 20, font_size = 15,
                                                 color = (255, 255, 255, 255),
                                                 bold = True)

        self.bolas = []

        self.seta = Objeto(self.imagem_seta, self.pos_seta[0], self.pos_seta[1])

        self.imagem_Gameover = pyglet.image.load(r'imagens\Gameover.png')

        self.Gameover = Objeto(self.imagem_Gameover, 0, 0)

        self.colocar_bolas()

###########################################################################

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.iniciar()

        if symbol == pyglet.window.key.ESCAPE:
            quit()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.bola_voando == False:
            if button == pyglet.window.mouse.LEFT:
                if y>= 15:
                    self.jogar_bola(x, y)
                else:
                    self.jogar_bola(x,15)

        if button == pyglet.window.mouse.RIGHT:
            #for bola in self.bolas:
            #    print(bola.cor)
            self.adicionar_linha()

    def on_mouse_motion(self, x, y, dx, dy):
        if x - self.seta.sprite.x == 0:
            self.seta.sprite.rotation = -90
        else:
            tan = (y - self.seta.sprite.y) / (x - self.seta.sprite.x)
            if x - self.seta.sprite.x > 0:
                self.seta.sprite.rotation = -(atan(tan) * 180 / pi)
            else:
                self.seta.sprite.rotation = (-atan(tan) * 180 / pi) - 180

###########################################################################

    def colocar_bolas(self):
        for y in range(8):
            for x in range(15):
                if (y + 1) % 2 == 0:
                    if x == 0:
                        continue

                cor = choice(self.cores)
                cor_1 = self.dicionario_cores[cor]

                self.im_bola = pyglet.image.load(cor)
                self.im_bola.anchor_x = self.imagem_bola.width // 2
                self.im_bola.anchor_y = self.imagem_bola.height // 2

                if y % 2 == 0:
                    xi = 30 + (x * 60)
                else:
                    xi = 30 + (x * 60) - (60 * cos((60 * pi) / 180))
                yi = 870 - (y * 60 * sin((60 * pi) / 180))

                self.bolas.append(Objeto(self.im_bola, xi, yi))
                self.bolas[-1].parada = True
                self.bolas[-1].cor = cor_1
                self.bolas[-1].inicial = True

        for bola in self.bolas:
            self.ver_conectados(bola)

    def jogar_bola(self, x, y):
        if x != 450:
            tan = (y - 10) / (x - 450)

            self.bolas.append(self.nova_bola)
            if x - 450 > 0:
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

    def ver_conectados(self, bola):
        raio = 65 ** 2
        for bola_2 in self.bolas:
            if bola_2 == bola:
                continue
            raio_2 = self.dist(bola.sprite.x, bola.sprite.y,
                               bola_2.sprite.x, bola_2.sprite.y)

            if raio_2 <= raio:
                bola.tocando.append(bola_2)

            if len(bola.tocando) >= 6:
                break

    def testar_colisao(self, bola):
        for bola_2 in self.bolas:
            if bola_2 == bola:
                continue

            raio = self.dist(bola.sprite.x, bola.sprite.y,
                             bola_2.sprite.x, bola_2.sprite.y)

            if raio <= ((2 * self.raio) ** 2):
                self.mapeamento(bola, bola_2)
                return True

    def update_bolas(self, dt):
        if len(self.bolas) > 0:
            if self.bolas[-1].parada:
                self.bola_voando = False
        for bola in self.bolas:
            if bola.parada == False:
                if self.testar_colisao(bola):
                    self.ver_conectados(bola)
                    bola.parada = True
                    self.numero = 1
                    self.verificados = [bola]
                    self.verificar_iguais(bola)
                    if self.numero >= 3:
                        for bolinha in self.verificados:
                            self.bolas.remove(bolinha)
                            self.pont = self.pont + 10 * self.numero
                        self.explodiu = True
                    if not self.explodiu:
                        self.erros += 1
                    self.explodiu = False
                    continue
                if bola.sprite.x >=871:
                    bola.velx = - fabs(bola.velx)
                if bola.sprite.x <= 29:
                    bola.velx = fabs(bola.velx)
                if bola.sprite.y > 871:
                    bola.parada=True

                bola.sprite.x += bola.velx * dt
                bola.sprite.y += bola.vely * dt
            else:
                if bola.sprite.y <= 60:
                    self.pontuacao_final = pyglet.text.Label(str(self.pont),
                                                             x = 270, y = 75,
                                                             font_size = 35,
                                                             color = (0, 0, 0, 255),
                                                             bold = True, italic = True,
                                                             font_name = 'arial')
                    self.perdeu = True

    def previa(self):
        self.nova_bola = self.bola_previa
        self.nova_bola.sprite.x = self.pos_seta[0]
        self.nova_bola.sprite.y = self.pos_seta[1]

        cor = choice(self.cores)
        cor_1 = self.dicionario_cores[cor]

        self.imagem_bola = pyglet.image.load(cor)
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bola_previa = Objeto(self.imagem_bola, self.pos_previa[0], self.pos_previa[1])
        self.bola_previa.cor = cor_1

        self.prev = False

    def adicionar_linha(self):

        for bola in self.bolas:
            bola.sprite.y -= 60 * sin((60 * pi) / 180)

        for x in range(15):
            if self.vez == 0:
                if x == 0:
                    continue

            cor = choice(self.cores)
            cor_1 = self.dicionario_cores[cor]

            self.im_bola = pyglet.image.load(cor)
            self.im_bola.anchor_x = self.imagem_bola.width // 2
            self.im_bola.anchor_y = self.imagem_bola.height // 2

            if self.vez == 1:
                xi = 30 + (x * 60)
            else:
                xi = 30 + (x * 60) - (60 * cos((60 * pi) / 180))
            yi = 870

            self.bolas.append(Objeto(self.im_bola, xi, yi))
            self.bolas[-1].parada = True
            self.bolas[-1].cor = cor_1
            self.bolas[-1].inicial = True

        if self.vez == 0:
            self.vez = 1
        else:
            self.vez = 0

        for bola in self.bolas:
            bola.tocando = []
            self.ver_conectados(bola)

    def dist(self, x1, y1, x2, y2):
        a1 = (x1 - x2) ** 2
        a2 = (y1 - y2) ** 2
        return (a1 + a2)

    def p_ang(self, xi, yi, xf, yf):
        if xf == xi:
            ang = 90
        else:
            ang = atan((yf - yi) / (xf - xi))
            ang = (180 * ang / pi)
        if xf > xi:
            if ang < 0:
                ang += 360
            return ang
        elif xf < xi:
            return ang + 180
        else:
            if yf > yi:
                return ang
            else:
                return ang + 180

    def mapeamento(self, bola1, bola2):

        angulo = self.p_ang(bola2.sprite.x, bola2.sprite.y,
                            bola1.sprite.x, bola1.sprite.y)

        if angulo <= 30:
            ang = 0
        elif angulo <= 90:
            ang = (60 * pi) / 180
        elif angulo <= 150:
            ang = (120 * pi) / 180
        elif angulo <= 210:
            ang = pi
        elif angulo <= 270:
            ang = (240 * pi) / 180
        elif angulo <= 330:
            ang = (300 * pi) / 180
        else:
            ang = 0

        bola1.sprite.x = bola2.sprite.x + (60 * cos(ang))
        bola1.sprite.y = bola2.sprite.y + (60 * sin(ang))

        for bola in self.bolas:
            if bola == bola1:
                bola.parada = True

    def verificar_iguais(self, bola):
        cor = bola.cor
        for bola1 in bola.tocando:
            if bola1.cor == cor and bola1 not in self.verificados:
                self.numero += 1
                self.verificados.append(bola1)
                self.verificar_iguais(bola1)
   # def novos_niveis(self):
      #  if self.pont >= 5000:
        #    self.cores.append(r'imagens\bola_Raul.png')
       # if self.pont >= 10000:
        #    self.cores.append(r'imagens\bola_Aleixo.png')
############################################################################

    def on_draw(self):
        self.clear()
        if self.perdeu:
            self.Gameover.draw()
            self.pontuacao_final.draw()
        else:
            self.seta.draw()
            self.nova_bola.draw()
            self.bola_previa.draw()
            for bola in self.bolas:
                bola.draw()
            self.label_pontuacao.draw()

    def update(self, dt):
        if self.prev and self.bola_voando == False:
            self.previa()
        if not self.bola_voando and self.erros >= 5:
            self.adicionar_linha()
            self.erros = 0
        self.update_bolas(dt)
        self.label_pontuacao = pyglet.text.Label('Pontuação : ' + str(self.pont),
                                                 x=20, y=20, font_size=15,
                                                 color=(255, 255, 255, 255),
                                                 bold=True)

      #  self.novos_niveis()


if __name__ == "__main__":
    win = Tela(900, 900, "Bubble Shooter", resizable=False, vsync=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)
    pyglet.app.run()