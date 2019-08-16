import pyglet


class Ball(pyglet.sprite.Sprite):
    #definindo aceleracoes da bola
    GRAVITY_ACC = 0
    X_ACC = 0 #ainda n serve pra nd
    y_ACC = 0 #ainda n serve pra nd

    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

    #atualizando a posicao da bola
    def update(self, dt):
        self.y = self.position[1] + (self.GRAVITY_ACC + self.y_ACC) * dt
