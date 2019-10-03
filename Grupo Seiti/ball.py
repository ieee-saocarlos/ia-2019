import pyglet
import pymunk
import numpy
from pymunk import pyglet_util
import math

#class Ball(pyglet.sprite.Sprite):
class Bola(pyglet.sprite.Sprite):
    def __init__(self, mass, radius, xB, yB, *args, **kwargs):
        super(Bola, self).__init__(*args, **kwargs)
        self.circle_moment = pymunk.moment_for_circle(mass, 0, radius)
        self.circle_body = pymunk.Body(mass, self.circle_moment)
        self.circle_body.position = xB, yB
        self.circle_shape = pymunk.Circle(self.circle_body, radius)
        self.circle_shape.elasticity = 0.9
        self.circle_shape.friction = 0.9



    #atualizando a posicao da bola
    def update(self, dt):
        self.y = self.circle_body.position[1]
        self.x = self.circle_body.position[0]
        self.rotation = numpy.rad2deg(self.circle_body.angle)




