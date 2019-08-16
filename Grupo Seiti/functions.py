#Arquivo para definir funcoes uteis


class Functions:

    #alterando a ancoragem das imagens
    @staticmethod
    def ancorar(image, pos):
        if pos == 'dir':
            image.anchor_y = image.height//2
            image.anchor_x = image.width

        elif pos == 'esq':
            image.anchor_y = image.height//2

        elif pos == 'center':
            image.anchor_y = image.height // 2
            image.anchor_x = image.width // 2

        return image
