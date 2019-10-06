import pymunk
import pyglet
import math

class Circulo:
    def __init__(self, x, y, r):
        self.circulo_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.circulo = pymunk.Circle(self.circulo_body, r)
        self.circulo.body.position = x,y
        self.circulo.color = (255, 0, 0, 255)
        self.circulo.elasticity = 0.98
        self.circulo.friction = 0.6

class Triangulo1:
    def __init__(self, x, y, a):
        self.triangulo1_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.triangulo1 = pymunk.Poly(self.triangulo1_body, ((-a,0),(a*math.sqrt(3)/2,-a),(a*math.sqrt(3)/2,a)))
        self.triangulo1.body.position = x, y
        self.triangulo1.color = (255, 0, 0, 255)
        self.triangulo1.elasticity = 0.98
        self.triangulo1.friction = 0.6

class Triangulo2:
    def __init__(self, x, y, b, h, rot):
        self.triangulo2_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.triangulo2 = pymunk.Poly(self.triangulo2_body, ((0, 10),(b,0),(rot,h)))
        self.triangulo2.body.position = x,y
        self.triangulo2.color = (255, 0, 0, 255)
        self.triangulo2.elasticity = 0.98
        self.triangulo2.friction = 0.6

class Trigira:
    def __init__(self, x, y, l):
        self.trigira = pymunk.Poly(None, ((-l*math.sqrt(3)/3, 0),(l*math.sqrt(3)/6,-l/2),(l*math.sqrt(3)/6,l/2)))
        self.trigira_moment = pymunk.moment_for_poly(10,self.trigira.get_vertices())
        self.trigira_body = pymunk.Body(10 ,self.trigira_moment, pymunk.Body.DYNAMIC)
        self.trigira.body = self.trigira_body
        self.trigira_body.position = x, y
        self.trigira.color = (255, 0, 0, 255)
        self.trigira.elasticity = 0.5
        self.trigira.friction = 0.6
        self.pino = pymunk.Body(body_type= pymunk.Body.STATIC)
        self.pino.position = self.trigira_body.position
        self.j = pymunk.PivotJoint(self.pino, self.trigira_body, (0,0), (0,0))
