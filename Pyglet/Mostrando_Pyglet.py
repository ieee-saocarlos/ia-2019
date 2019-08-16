import pyglet #importar a biblioteca

class Janela(pyglet.window.Window): #criar a classe do pyglet
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #isso faz com que os argumentos iniciais da classe determinam a janela

        self.set_location(100, 100) #posição da tela inicial em relação ao canto superior esquerdo

        self.velx = 400 # seta uma velocidade em x
        self.vely = 300 # seta uma velocidade em y

        self.imagem_bola = pyglet.image.load(r'D:\programação\Python\Jogos\bola.png')
        # puxa uma imagem
        self.imagem_bola.anchor_x = self.imagem_bola.width // 2 # seta os pontos que fica relativo as posições x e y
        self.imagem_bola.anchor_y = self.imagem_bola.height // 2

        self.bola = pyglet.sprite.Sprite(self.imagem_bola, x=400, y=400)
        # cria o desenho com imagem da bola criada a cima, nas posições x 400 e y 400

        self.texto = pyglet.text.Label('Texto', x=350, y=800, font_size=15,
                                       bold=True, italic=True, color=(0,255,0,255))
        #cria um texto na tela escrito Texto com tamanho 15 negrito e itálico, nas posições x 350 e y 800, com a cor preta (RGB sendo o ultimo número o brilho, tudo de 0 a 255)

    def on_key_press(self, symbol, modifiers): # função que recebe as teclas clicadas
        if symbol == pyglet.window.key.SPACE: # se aperta a tecla espaço
            self.velx *= 0.8 # reduz as velocidades em x e em y
            self.vely *= 0.8
        if symbol == pyglet.window.key.ESCAPE: # se apertar ESC o programa fecha
            self.close() # fecha o programa

    def on_mouse_press(self, x, y, button, modifiers): # função que recebe onde o mouse clica
        if button == pyglet.window.mouse.LEFT: # ve se o botão esquerdo do mouse foi clicado
            self.bola = pyglet.sprite.Sprite(self.imagem_bola, x=x, y=y) # recria a imagem da bola inde o mouse foi clicado

    def on_draw(self): #função que faz com que desenha na janela, o quanto mais baixo na função, a imagem fica a frente das de cima
        self.clear() #limpa a tela
        self.bola.draw() #desenha a bola na tela
        self.texto.draw() #desenha o texto na tela

    def atualizar_bolinha(self, dt):
        if self.bola.x > 800: # se a bolinha chega no canto direito da tela, a velocidade em x fica negativa
            self.velx = -self.velx
        elif self.bola.x < 50: # se a bolinha chega no canto esquerdo da tela, a velocidade em x fica positiva
            self.velx = -self.velx
        if self.bola.y > 800: # se a bola chega no topo da tela, a velocidade em y fica negativa
            self.vely = -self.vely
        elif self.bola.y < 50: # se a bola chega na base da tela, a velocidade em y fica positiva
            self.vely = -self.vely
        self.bola.x += self.velx * dt # atualiza a posição x da bola com a velocidade velx
        self.bola.y += self.vely * dt # atualiza a posição y da bola com a velocidade vely

    def update(self, dt): #função que realiza a cada 1/60
        self.atualizar_bolinha(dt)

if __name__ == "__main__": #iniciar o programa
    win = Janela(850, 850, "Jogo das bolinhas", resizable=False, vsync=True)
    #win é a janela, com tamanho 960x900, nome da tela Jogo das bolinhas, sem poder reajustar a tela com vsync
    pyglet.clock.schedule_interval(win.update, 1 / 60)
    #faz com a cada 1/60 segundos faça a função update da janela
    pyglet.app.run() #inicia a tela