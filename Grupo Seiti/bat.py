import pyglet


class Bat(pyglet.sprite.Sprite):

    def __init__(self, rot, *args, **kwargs):
        super(Bat, self).__init__(*args, **kwargs)
        self.rotation = rot

    #Funcão para rodar os bastoes, algo q NAO ESTA FUNCIONANDO
    def click(self, rot):
        self.rotation = rot

