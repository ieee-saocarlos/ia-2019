import pygame
import math
from pacMan import player

class Ghost(object):
    def __init__(self, x, y, cor, pac):
        self.coord = {          # dicionário indicando coordenadas
            "x": x,
            "y": y,
        }
        self.velocXY = {        # armazenar velocidade
            "x": 0,
            "y": 0,
        }
        self.veloc = 2          # velocidade
        self.tamanho = 23       # tamanho em pixels
        self.cor = cor
        self.estado = {        # identificar cada estado do fantasma
            "chase": False,
            "scatter": False,
            "eaten": False,
            "frightened": False,
        }
        #self.estadoAtual = []   # lista vazia na inicialização
        self.jogador = {         # posição do jogador como entrada
            "x": pac.x,
            "y": pac.y,
            "up": pac.up,
            "down": pac.down,
            "left": pac.left,
            "right": pac.right,
        }
        self.direcao = {      # dicionário indicando a direção
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }
        self.proximaDirecao = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

    def move(self):
        if self.direcao.get("up"):
            self.velocXY["y"] = -self.veloc
            self.proximaDirecao["down"] = False
        elif self.direcao.get("down"):
            self.velocXY["y"] = self.veloc
            self.proximaDirecao["up"] = False
        elif self.directao.get("left"):
            self.velocXY["x"] = -self.veloc
            self.proximaDirecao["right"] = False
        elif self.direcao.get("right"):
            self.velocXY["x"] = self.veloc
            self.proximaDirecao["left"] = False

        self.coord["x"] += self.velocXY.get("x")
        self.coord["y"] += self.velocXY.get("y")


""" SUBCLASSES """
class Blinky(Ghost):        # vermelho
    def procurarAlvo(self):
        if self.estado["chase"]:
            self.alvo = {"x": self.jogador["x"], "y": self.jogador["y"]}

        elif self.estado["scatter"]:
            self.alvo = self.jogador
        elif self.estado["eaten"]:
            self.alvo = self.jogador            # direto pra casinha
        elif self.estado["frightened"]:
            self.alvo = self.jogador            # caminho aleatório (?)
        else:
            self.estado["scatter"] = True


class Pinky(Ghost):          # rosa
    def procurarAlvo(self):
        if self.estado["chase"]:
            if self.jogador["up"] == 1:
                self.alvo = {"x": self.jogador["x"], "y": self.jogador["y"]-4*self.tamanho}
            elif self.jogador["down"] == 1:
                self.alvo = {"x": self.jogador["x"], "y": self.jogador["y"]+4*self.tamanho}
            elif self.jogador["left"] == 1:
                self.alvo = {"x": self.jogador["x"]-4*self.tamanho, "y": self.jogador["y"]}
            elif self.jogador["right"] == 1:
                self.alvo = {"x": self.jogador["x"]+4*self.tamanho, "y": self.jogador["y"]}
        elif self.estado["scatter"]:
            self.alvo = self.jogador
        elif self.estado["eaten"]:
            self.alvo = self.jogador
        elif self.estado["frightened"]:
            self.alvo = self.jogador
        else:
            self.estado["scatter"] = True
#class Inky(Ghost):          # azul
#class Clyde(Ghost):         # laranja

