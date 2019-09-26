import pyglet
import pymunk
import math
import numpy
import functions
from pymunk import Vec2d


fc = functions.Functions()


class Bat(pyglet.sprite.Sprite):
    #definindo formato (triangular) e massa dos bastoes
    forma = [(5, -5), (-50, -33), (0, 12)]
    massa = 80

    def __init__(self, ori, *args, **kwargs):
        super(Bat, self).__init__(*args, **kwargs)
        self.orientation = ori

        #criando o bastão se acordo com o lado que será posicionado
        moment = pymunk.moment_for_poly(self.massa, self.forma)
        self.body = pymunk.Body(self.massa, moment)
        self.body.position = self.x, self.y
        self.shape = pymunk.Poly(self.body, [(ori*x, y) for x, y in self.forma]) #o valor de ori torna o x positivo ou negativo

        #criando o ponto em que o bastão é fixado
        self.jointBody = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.jointBody.position = self.body.position
        self.j = pymunk.PivotJoint(self.body, self.jointBody, (0, 0), (0, 0))
        self.s = pymunk.DampedRotarySpring(self.body, self.jointBody, 0.15*ori, 20000000, 900000)

        #atribuindo algumas caracteristcas ao bastão
        self.shape.group = 1
        self.shape.elasticity = 0.9
        self.status = "NORMAL"

    def update(self, dt):
        #atualiza o angulo da sprit
        self.rotation = -30 * self.orientation - (numpy.rad2deg(self.body.angle) * 0.9)

        #aplica o impulso no bastão
        if self.status == "PRESS":
            self.body.apply_impulse_at_local_point(Vec2d.unit() * -4000, (self.width * self.orientation, 0))


    '''def listaPixels(self):
        self.bordas = []
        rot = self.rotation
        sentido = fc.sinal(rot)
        for i in range(self.x, (self.x + self.width * sentido + 1), sentido):
            self.bordas.append((i, self.y+(i - self.x)*math.cos(rot)))'''


