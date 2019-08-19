import pyglet
import matplotlib.pyplot as plt
from pyglet.window import key
from pyglet.text import Label
from objeto import Objeto
from random import randint, random, choice
from time import time

class Jogo(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(55, 80)

        self.inicio = time()
        self.frame_rate = 1 / 60
        self.populacao = 250
        self.geracao = 0
        self.vel_fundo = -150
        self.grav = -300
        self.geracao = 0
        self.maior_pont = 0
        self.na_ger = 0
        self.pontuacao = 0
        self.programado = False
        self.time = False
        self.fator_aprendizado = 0.1
        self.birds = []

        self.data_graf = [[], []]

        self.resetar()

    def resetar(self):
        if self.geracao != 0:
            print('Gerações:', self.geracao)
            print('Pontuação:', self.pontuacao)
            print()
        self.fundos = []
        self.chaos = []
        self.tubos = []
        self.tubos_inv = []

        self.tubo_rate = 0
        self.geracao += 1

        self.imagem_fundo = pyglet.image.load(r'D:\programação\Python\IA\flapy_bird\ceu.png')
        self.fundos.append(Objeto(self.imagem_fundo, 0, 0))
        self.fundos.append(Objeto(self.imagem_fundo, 3084, 0))

        self.imagem_chao = pyglet.image.load(r'D:\programação\Python\IA\flappy_bird_ult_tent\chao.png')
        self.chaos.append(Objeto(self.imagem_chao, 0, -75))
        self.chaos.append(Objeto(self.imagem_chao, 2045, -75))

        self.imagem_tubo = pyglet.image.load(r'D:\programação\Python\IA\flapy_bird\tubo.png')
        self.imagem_tubo.anchor_x = self.imagem_tubo.width // 2

        self.imagem_tubo_invertido = pyglet.image.load(r'D:\programação\Python\IA\flapy_bird\tubo_invertido.png')
        self.imagem_tubo_invertido.anchor_x = self.imagem_tubo_invertido.width // 2

        self.imagem_bird = pyglet.image.load(r'D:\programação\Python\IA\flapy_bird\bird.png')

        self.texto = Label('Vivos : ' + str(self.populacao), font_size=15,
                           bold=True, color=(0, 0, 0, 255), x=700, y=840)

        self.texto1 = Label('Pontuação : ' + str(0), font_size=15,
                           bold=True, color=(0, 0, 0, 255), x=700, y=810)

        self.texto2 = Label('Geração : ' + str(self.geracao), font_size=15,
                            bold=True, color=(0, 0, 0, 255), x=700, y=870)

        self.texto3 = Label('Máximo ' + str(self.maior_pont) + ' na ger. ' + str(self.na_ger), font_size=15,
                            bold=True, color=(0, 0, 0, 255), x=700, y=780)

        if self.pontuacao > 100 and self.time == False:
            print(time() - self.inicio)
            if self.pontuacao > 1000:
                print(time() - self.inicio)
                for bird in self.birds:
                    if bird.pontuacao > 1000:
                        print(bird.gene)
                self.time = True

        if self.pontuacao == 0:
            self.birds = []
            for a in range(self.populacao):
                self.birds.append(Objeto(self.imagem_bird, 150, 500))
                self.birds[-1].gene = [[[(6 * random()) - 3 for _ in range(2)] for _ in range(5)],
                                        [[(6 * random()) - 3 for _ in range(5)] for _ in range(5)],
                                        [[(6 * random()) - 3 for _ in range(5)] for _ in range(1)]]
        else:
            self.selecionar()
            self.birds = []
            for gene1 in self.genes_def:
                self.birds.append(Objeto(self.imagem_bird, 150, 500, gene = gene1))

        self.data_graf[0].append(self.geracao)
        self.data_graf[1].append(0)


    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.pulo(self.birds[0])
        if symbol == key.ESCAPE:
            self.resetar()

    def on_draw(self):
        for fundo in self.fundos:
            fundo.draw()
        for tubo, tubo_inv in zip(self.tubos, self.tubos_inv):
            tubo.draw()
            tubo_inv.draw()
        self.texto.draw()
        self.texto1.draw()
        self.texto2.draw()
        self.texto3.draw()
        for chao in self.chaos:
            chao.draw()
        for bird in self.birds:
            bird.draw()

    def selecionar(self):
        maiores = []
        self.genes = []
        self.genes_def = []
        maior = 0
        for bird in self.birds:
            if bird.pontuacao > maior:
                maior = bird.pontuacao
        for bird in self.birds:
            if bird.pontuacao == maior:
                maiores.append(bird)
        while self.populacao % len(maiores) != 0:
            maiores.remove(maiores[-1])
        parte = self.populacao // len(maiores)
        for bird in maiores:
            for _ in range(parte - 1):
                self.genes.append(bird.gene)
            self.genes_def.append(bird.gene)
        #for k in self.genes_def[:len(maiores)]:
        #    print(k)
        #print()
        self.mutacao(len(maiores)) #printar o antes e depois pra ver se muda os que permaneceriam
        for _ in range(self.populacao - len(self.genes_def)):
            self.genes_def.append([[[(6 * random()) - 3 for _ in range(2)] for _ in range(5)],
                                    [[(6 * random()) - 3 for _ in range(5)] for _ in range(5)],
                                    [[(6 * random()) - 3 for _ in range(5)] for _ in range(1)]])
        #for k in self.genes_def[:len(maiores) + 10]:
        #    print(k)

    def mutacao(self, n):
        for x in range(int((2/5) * len(self.genes))):
            g = [[[0 for _ in range(2)] for _ in range(5)],
                 [[0 for _ in range(5)] for _ in range(5)],
                 [[0 for _ in range(5)] for _ in range(1)]]
            for i in range(len(g)):
                for j in range(len(g[i])):
                    for k in range(len(g[i][j])):
                        if random() > 0.5:
                            g[i][j][k] = self.genes[x][i][j][k] + (random() * self.fator_aprendizado) #trocar o x+1 por x
                        else:
                            g[i][j][k] = self.genes[x][i][j][k] - (random() * self.fator_aprendizado)
            self.genes_def.append(g)
        for x in range(int((2/5) * len(self.genes))):
            g = [[[0 for _ in range(2)] for _ in range(5)],
                 [[0 for _ in range(5)] for _ in range(5)],
                 [[0 for _ in range(5)] for _ in range(1)]]
            for i in range(len(g)):
                for j in range(len(g[i])):
                    for k in range(len(g[i][j])):
                        if random() > 0.5:
                            g[i][j][k] = self.genes[x][i][j][k] + (random() * 2 * self.fator_aprendizado) #trocar o x+1 por x
                        else:
                            g[i][j][k] = self.genes[x][i][j][k] - (random() * 2 * self.fator_aprendizado)
            self.genes_def.append(g)


    def tocar(self, bird):
        for tubo, tubo_inv in zip(self.tubos, self.tubos_inv):
            if bird.sprite.x + 74 > tubo.sprite.x - 75 and bird.sprite.x < tubo.sprite.x + 75:
                if (bird.sprite.y < tubo.sprite.y + 700 and bird.sprite.y + 52 > tubo.sprite.y + 643) or (bird.sprite.y + 52 > tubo.sprite.y + 870 and bird.sprite.y < tubo.sprite.y + 927):
                    bird.morto = True
                    return
                if bird.sprite.x + 74 > tubo.sprite.x - 56 and bird.sprite.x < tubo.sprite.x + 56:
                    if bird.sprite.y + 52 < tubo.sprite.y + 643 or bird.sprite.y > tubo_inv.sprite.y + 57:
                        bird.morto = True
                        return

        if bird.sprite.y <= 120:
            bird.morto = True

    def pulo(self, bird):
        bird.vel = 220

    def update_chao_fundo(self, dt):
        for chao in self.chaos:
            chao.sprite.x += self.vel_fundo * dt
        if self.chaos[-1].sprite.x < 0:
            self.chaos.remove(self.chaos[0])
            self.chaos.append(Objeto(self.imagem_chao, self.chaos[-1].sprite.x + 2045, -75))

        for fundo in self.fundos:
            fundo.sprite.x += self.vel_fundo * dt
        if self.fundos[-1].sprite.x < 0:
            self.fundos.remove(self.fundos[0])
            self.fundos.append(Objeto(self.imagem_fundo, self.fundos[-1].sprite.x + 3084, 0))

    def update_tubo(self, dt):
        x = 1100
        y = randint(-450, -100)
        self.tubo_rate -= dt
        if self.tubo_rate <= 0:
            if self.programado == True:
                y = -275
                self.programado = False
            self.tubos.append(Objeto(self.imagem_tubo, x, y))
            self.tubos_inv.append(Objeto(self.imagem_tubo_invertido, x, y + 870))
            if y < -400 or y > -150:
                self.programado = True
            self.tubo_rate += 3

        if self.tubos[0].sprite.x <= -100:
            self.tubos.remove(self.tubos[0])
            self.tubos_inv.remove(self.tubos_inv[0])

        for tubo, tubo_inv in zip(self.tubos, self.tubos_inv):
            tubo.sprite.x += self.vel_fundo * dt
            tubo_inv.sprite.x += self.vel_fundo * dt

        for tubo, tubo_inv in zip(self.tubos, self.tubos_inv):
            if tubo.sprite.y < -500:
                tubo.vel_tubo = choice([30, 60, 90, 120, 150])
            elif tubo.sprite.y > -50:
                tubo.vel_tubo = -choice([30, 60, 90, 120, 150])
            #tubo.sprite.y += tubo.vel_tubo * dt
            #tubo_inv.sprite.y += tubo.vel_tubo * dt


    def update_bird(self, dt):
        self.mortos = 0
        for bird in self.birds:
            if bird.morto == True:
                self.mortos += 1
            self.tocar(bird)
            if bird.morto == False:
                bird.vel += self.grav * dt
                if bird.sprite.y < 840:
                    bird.sprite.y += bird.vel * dt
                elif bird.vel < 0:
                    bird.sprite.y += bird.vel * dt
            else:
                bird.sprite.x += self.vel_fundo * dt
        self.texto = Label('Vivos : ' + str(self.populacao - self.mortos), font_size=15,
                           bold=True, color=(0, 0, 0, 255), x=700, y=840)
        if self.mortos == self.populacao:
            self.resetar()

    def pontuar(self):
        for bird in self.birds:
            if bird.sprite.x > self.tubos[0].sprite.x + 75 and bird.pontuado == False:
                bird.pontuacao += 1
                bird.pontuado = True
            if bird.sprite.x < self.tubos[0].sprite.x:
                bird.pontuado = False
        pontuacao = 0
        for bird in self.birds:
            if bird.pontuacao > pontuacao:
                pontuacao = bird.pontuacao
        self.pontuacao = pontuacao
        self.texto1 = Label('Pontuação : ' + str(pontuacao), font_size=15,
                            bold=True, color=(0, 0, 0, 255), x=700, y=810)
        self.data_graf[1][-1] = pontuacao
        if pontuacao > self.maior_pont:
            self.maior_pont = pontuacao
            self.na_ger = self.geracao

    def jogada(self):
        for bird in self.birds:
            if bird.morto == False:
                for tubo in self.tubos:
                    if tubo.sprite.x + 75 > bird.sprite.x:
                        self.entradas = [tubo.sprite.x - bird.sprite.x,
                                         tubo.sprite.y + 700 - bird.sprite.y]
                        break
                self.rna(self.entradas, bird.gene, bird)

    def rna(self, entradas, gene, bird):
        self.out1 = []
        self.out2 = []
        for i in range(5):
            self.out1.append(self.neuronio(entradas, gene[0][i]))
        for i in range(5):
            self.out2.append(self.neuronio(self.out1, gene[1][i]))
        self.output = self.neuronio(self.out2, gene[2][0])

        if self.output > 0:
            self.pulo(bird)

    def neuronio(self, inputs, pesos):
        bias = pesos[-1]
        soma = 0
        for i in range(len(inputs)):
            soma += inputs[i] * pesos[i]

        return self.funcao(soma + bias)

    def funcao(self, x):
        if x >= 0:
            return x
        else:
            return 0

    def update(self, dt):
        self.update_chao_fundo(dt)
        self.update_tubo(dt)
        self.jogada()
        self.pontuar()
        self.update_bird(dt)


if __name__ == "__main__":
    win = Jogo(960, 900, "Flappy Bird", resizable=False, vsync=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)
    pyglet.app.run()
