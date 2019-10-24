import math
import pygame
# Pensado para um player no formato de um círculo
class Player(object):
    def __init__(self, x, y, cor):
        """ ATRIBUTOS DA CLASSE """
        self.x = x
        self.y = y
        self.tamanho = 23
        self.mx1 = round(x / 24)
        self.my1 = round(y / 24)
        self.mx2 = round((x + self.tamanho - 1) / 24)
        self.my2 = round((y + self.tamanho - 1) / 24)
        self.cor = cor
        self.velx = 0
        self.vely = 0
        self.velTest = 2  # TEM QUE SER DIVISOR DE 24
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.comedor = False

    # MÉTODO - MOVIMENTAÇÂO

    # Eu deixei de usar dicionários pq eu tava encontrando dificuldades, mas podemos voltar a usar
    def move(self, esquerda, direita, cima, baixo):
        if self.vely == 0:
            if esquerda == 1 and self.left == 1 and self.my1 == self.my2:
                self.velx = -self.velTest
                self.vely = 0
            else:
                if direita == 1 and self.right == 1 and self.my1 == self.my2:
                    self.velx = self.velTest
                    self.vely = 0
                else:
                    self.velx = 0
            if cima == 1 and self.up == 1 and self.mx1 == self.mx2:
                self.vely = -self.velTest
                self.velx = 0
            else:
                if baixo == 1 and self.down == 1 and self.mx1 == self.mx2:
                    self.vely = self.velTest
                    self.velx = 0
                else:
                    self.vely = 0
        else:
            if cima == 1 and self.up == 1 and self.mx1 == self.mx2:
                self.vely = -self.velTest
                self.velx = 0
            else:
                if baixo == 1 and self.down == 1 and self.mx1 == self.mx2:
                    self.vely = self.velTest
                    self.velx = 0
                else:
                    self.vely = 0
            if esquerda == 1 and self.left == 1 and self.my1 == self.my2:
                self.velx = -self.velTest
                self.vely = 0
            else:
                if direita == 1 and self.right == 1 and self.my1 == self.my2:
                    self.velx = self.velTest
                    self.vely = 0
                else:
                    self.velx = 0

        self.x += self.velx
        self.y += self.vely
        self.mx1 = math.floor(self.x / 24)
        self.my1 = math.floor(self.y / 24)
        self.mx2 = math.floor((self.x + self.tamanho) / 24)
        self.my2 = math.floor((self.y + self.tamanho) / 24)

    def analise_parede(self, mapa):
        if (self.mx1 < 27 and self.mx2 < 27) and (self.mx1 > 0 and self.mx2 > 0):
            if mapa[self.my1][self.mx1] == 2 and mapa[self.my2][self.mx2] == 2:
                mapa[self.my1][self.mx1] = 0
            if mapa[self.my1][self.mx1] == 3 and mapa[self.my2][self.mx2] == 3:
                mapa[self.my1][self.mx1] = 0
                self.comedor = True
            if mapa[self.my1 + 1][self.mx1] % 3 == 1 and mapa[self.my2 + 1][self.mx2] % 3 == 1:
                self.down = 0
                self.vely = 0
            else:
                self.down = 1
            if mapa[self.my1 - 1][self.mx1] % 3 == 1 and mapa[self.my2 - 1][self.mx2] % 3 == 1:
                self.up = 0
                self.vely = 0
            else:
                self.up = 1
            if mapa[self.my1][self.mx1 + 1] % 3 == 1 and mapa[self.my2][self.mx2 + 1] % 3 == 1:
                self.right = 0
                self.velx = 0
            else:
                self.right = 1
            if mapa[self.my1][self.mx1 - 1] % 3 == 1 and mapa[self.my2][self.mx2 - 1] % 3 == 1:
                self.left = 0
                self.velx = 0
            else:
                self.left = 1
        else:
            if self.x > 224 * 3 and self.velx > 0:
                self.x = -24
            else:
                if self.x <= -24 and self.velx < 0:
                    self.x = 224 * 3

    # MÉTODO - DESENHANDO O PLAYER

    def draw(self, display, cor):
        pygame.draw.rect(display, self.cor, [self.x, self.y, self.tamanho, self.tamanho], 0)
