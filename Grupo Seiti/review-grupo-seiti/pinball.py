import pyglet
from pyglet.window import key
from pyglet.gl import *
import pymunk
import pymunk.pyglet_util
import game

# Instanciando a classe game e janela
game = game.Game()

window = pyglet.window.Window(game.windowWidth, game.windowHeight, vsync=False)

# iniciando o clock para atualizar a tela
pyglet.clock.schedule_interval(game.update, game.TIME_INTERVAL)


# funcão para escrever na tela
@window.event
def on_draw():
    window.clear()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    game.draw()

    # exibindo na tela os elementos da fisica (pymunk)
    game.space.debug_draw(pymunk.pyglet_util.DrawOptions())


# funcao para detectar teclas pressionadas
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        game.batE.status = "PRESS"

    elif symbol == key.RIGHT:
        game.batD.status = "PRESS"

    elif symbol == key.SPACE:
        game.molaS = 'PRESS'

    if game.status == "GAME OVER":
        if symbol == key.ENTER:
            game.reset()


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        game.batE.status = "NORMAL"

    elif symbol == key.RIGHT:
        game.batD.status = "NORMAL"

    elif symbol == key.SPACE:
        game.molaS = 'GO'


# iniciando a aplicacão
pyglet.app.run()
