import pyglet
import pymunk
from pyglet.gl import *
import functions
import ball
import bat
import obstaculos
from pymunk import pyglet_util

func = functions.Functions()
# posições iniciais

# Bola
x_b = 250  # 505
y_b = 500  # 55

# Bastoes
x_e = 220
y_e = 50
x_d = 375
y_d = 50


class Game:
    # definindo variaveis do pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -500)  # -500 é toop

    # definindo a taxa de atualizacão
    TIME_INTERVAL = 0.01
    time = 0

    # definindo o fundo e caracteristicas da janela
    fundo = pyglet.resource.image('resources/images/Arte fundo - baixo.png')

    windowWidth = fundo.width
    windowHeight = fundo.height

    # definindo a imagem de gameover
    go = pyglet.image.load('resources/images/gameOver.gif')
    go = func.ancorar(go, 'center')
    gameOver = pyglet.sprite.Sprite(go, windowWidth // 2, windowHeight // 2)

    # definindo array para objetos que podem colidir
    physicalObjects = []

    # Bordas
    borders = [pymunk.Segment(space.static_body, (495, 45), (515, 45), 1.0),  # tubo/direita
               pymunk.Segment(space.static_body, (515, 45), (515, 400), 1.0),

               pymunk.Segment(space.static_body, (515, 400), (510, 500), 1.0),  # circulo/topo
               pymunk.Segment(space.static_body, (510, 500), (505, 545), 1.0),
               pymunk.Segment(space.static_body, (505, 545), (495, 570), 1.0),
               pymunk.Segment(space.static_body, (495, 570), (480, 600), 1.0),
               pymunk.Segment(space.static_body, (480, 600), (420, 660), 1.0),
               pymunk.Segment(space.static_body, (420, 660), (350, 693), 1.0),
               pymunk.Segment(space.static_body, (350, 693), (300, 697), 1.0),  # metade do
               pymunk.Segment(space.static_body, (300, 697), (250, 693), 1.0),  # semi circulo
               pymunk.Segment(space.static_body, (250, 693), (180, 660), 1.0),
               pymunk.Segment(space.static_body, (180, 660), (120, 600), 1.0),
               pymunk.Segment(space.static_body, (120, 600), (105, 570), 1.0),
               pymunk.Segment(space.static_body, (105, 570), (95, 545), 1.0),
               pymunk.Segment(space.static_body, (95, 545), (90, 500), 1.0),

               pymunk.Segment(space.static_body, (90, 500), (100, 400), 1.0),  # lado esquerdo
               pymunk.Segment(space.static_body, (100, 400), (130, 200), 1.0),
               pymunk.Segment(space.static_body, (130, 200), (212, 60), 1.0),

               pymunk.Segment(space.static_body, (380, 60), (460, 200), 1.0),  # lado direito
               pymunk.Segment(space.static_body, (460, 200), (495, 400), 1.0),

               # pymunk.Segment(space.static_body, (500, 400), (490, 450), 1.0), # tubo lado esquerdo
               pymunk.Segment(space.static_body, (495, 400), (495, 45), 1.0),
               pymunk.Segment(space.static_body, (495, 400), (490, 500), 1.0),
               pymunk.Segment(space.static_body, (490, 500), (485, 540), 1.0),
               pymunk.Segment(space.static_body, (485, 540), (475, 565), 1.0),
               pymunk.Segment(space.static_body, (475, 565), (460, 590), 1.0)
               ]

    removiveis = []

    # iniciando os elementos do jogo
    def __init__(self):
        # adicionando as formas(obstaculos)
        self.Circulo_0 = obstaculos.Circulo(385, 583, 39)
        self.Circulo_1 = obstaculos.Circulo(257, 302, 39)
        self.space.add(self.Circulo_0.circulo, self.Circulo_1.circulo)

        self.Triangulo1_0 = obstaculos.Triangulo1(270, 444, 42)
        self.Triangulo1_1 = obstaculos.Triangulo1(181, 560, 42)
        self.Triangulo1_2 = obstaculos.Triangulo1(413, 385, 42)
        self.space.add(self.Triangulo1_0.triangulo1, self.Triangulo1_1.triangulo1, self.Triangulo1_2.triangulo1)

        self.Triangulo2_0 = obstaculos.Triangulo2(210, 121, 40, 90, -40)
        self.Triangulo2_1 = obstaculos.Triangulo2(385, 121, -40, 90, 40)
        self.space.add(self.Triangulo2_0.triangulo2, self.Triangulo2_1.triangulo2)

        self.criaremov()

        # Criando os bastoes
        aux = func.ancorar(pyglet.image.load('resources/images/bastao1.png'), 'esq')
        self.batE = bat.Bat(-1, aux, x_e, y_e)
        self.space.add(self.batE.body, self.batE.shape)  # adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batE.j, self.batE.s)
        self.physicalObjects.append(self.batE)

        aux = func.ancorar(pyglet.image.load('resources/images/bastao-1.png'), 'dir')
        self.batD = bat.Bat(1, aux, x_d, y_d)
        self.space.add(self.batD.body, self.batD.shape)  # adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batD.j, self.batD.s)
        self.physicalObjects.append(self.batD)

        for line in self.borders:
            line.elasticity = 0.7
            line.group = 1
        self.space.add(self.borders)

        self.status = 'BEGINING'
        self.molaS = 'GO'
        self.molaX = 0

    def criaremov(self):
        self.Trigira_0 = obstaculos.Trigira(150, 300, 30)
        self.Trigira_1 = obstaculos.Trigira(190, 360, 30)
        self.Trigira_2 = obstaculos.Trigira(160, 400, 30)
        self.Trigira_3 = obstaculos.Trigira(140, 450, 30)
        self.space.add(self.Trigira_0.trigira, self.Trigira_0.trigira_body,
                       self.Trigira_1.trigira, self.Trigira_1.trigira_body,
                       self.Trigira_2.trigira, self.Trigira_2.trigira_body,
                       self.Trigira_3.trigira, self.Trigira_3.trigira_body)

        self.space.add(self.Trigira_0.j, self.Trigira_1.j, self.Trigira_2.j, self.Trigira_3.j)

        # Criando a bola
        self.mass = 1
        self.radius = 10
        aux = func.ancorar(pyglet.image.load('resources/images/bola.png'), 'center')
        self.ball = ball.Bola(self.mass, self.radius, x_b, y_b, aux)
        self.space.add(self.ball.circle_body, self.ball.circle_shape)
        self.removiveis = [self.Trigira_0.trigira, self.Trigira_0.trigira_body,
                           self.Trigira_1.trigira, self.Trigira_1.trigira_body,
                           self.Trigira_2.trigira, self.Trigira_2.trigira_body,
                           self.Trigira_3.trigira, self.Trigira_3.trigira_body,
                           self.Trigira_0.j, self.Trigira_1.j, self.Trigira_2.j, self.Trigira_3.j,
                           self.ball.circle_body, self.ball.circle_shape]

    def reset(self):

        self.space.remove(self.removiveis)
        self.criaremov()

        self.status = "PLAYING"

    # desenhando na tela os elementos do jogo
    def draw(self):
        self.fundo.blit(0, 0)
        if self.status == 'GAME OVER':
            self.gameOver.draw()

        elif self.status == 'PLAYING' or self.status == 'BEGINING':
            self.ball.draw()
            for obj in self.physicalObjects:
                obj.draw()

    # verificando status do jogo e mudando pos da bola
    def update(self, dt):
        dt = Game.TIME_INTERVAL

        self.space.step(dt)
        if self.status == "PLAYING":
            if self.ball.y < 0:
                self.status = 'GAME OVER'
            else:
                self.time += dt

                self.ball.update(dt)

                self.batE.update(dt)
                self.batD.update(dt)

        elif self.status == "BEGINING":
            self.at_mola(self.molaS)
            self.batE.update(dt)
            self.batD.update(dt)

    def at_mola(self, status):
        if status == 'PRESS':
            self.molaX += 40

        elif status == 'GO':
            if self.molaX != 0:
                impulso_bola = self.molaX
                # chamar função para aplicar impulso na bolinha se ela estiver na posição inicial

            self.molaX = 0
            self.status = "PLAYING"
