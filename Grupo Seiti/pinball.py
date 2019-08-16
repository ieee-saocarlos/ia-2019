import pyglet
from pyglet.window import key
from pyglet.gl import *
import game

#Instanciando a classe game e janela
game = game.Game()

window = pyglet.window.Window(game.windowWidth, game.windowHeight, vsync = False)

#iniciando o clock para atualizar a tela
pyglet.clock.schedule_interval(game.update, game.TIME_INTERVAL)


#funcão para escrever na tela
@window.event
def on_draw():
    window.clear()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    game.draw()

#funcao para detectar teclas pressionadas
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        game.esq()

    elif symbol == key.RIGHT:
        game.dir()

#iniciando a aplicacão
pyglet.app.run()