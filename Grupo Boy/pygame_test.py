import pygame 
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

# load the images of the char
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

# trocar o fps 
clock = pygame.time.Clock()

screenWidth = 500
x = 50
y = 400
#dimensoes da imagem do personagem
width = 64
height = 64
vel = 5

# variaveis p/ pular
# quando pulando, garantir que nao pode mover pra cima e pra baixo ou pular de novo enquanto esta pulando
isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindown():
	global walkCount
	#p/ nao ficar constantemente desenhando - cor preta
	#win.fill((0,0,0))
	#vamos dar fill com uma imagem
	win.blit(bg, (0,0))

	#drawing chracters - rectangle win - surface where it are going to be draw, color RGB, 
	#pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))
	#vamos desenhar uma imagem ao inves de um retangulo

	if walkCount + 1 >= 27: #tem a ver com frames per second, 3 frames per scrip, 9 scripts..sei la
		walkCount = 0

	if left:
		win.blit(walkLeft[walkCount//3], (x,y))
		walkCount += 1
	elif right:
		win.blit(walkRight[walkCount//3], (x,y))
		walkCount += 1
	else:
		win.blit(char, (x,y))

	pygame.display.update()


run = True
while run:

	# clock - time delay
	clock.tick(27)

	# events - anything that happens from the user
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	#obs: the cordinates are from the top left
	#fez desse jeito p/ enquanto apertar a tecla o bicho se mover
	#mas desse jeito, vai estar constantemente desenhando
	# x > vel garante que a posição de x não será negativa
	# mas o personagem vai parecer que ainda está fora da dela, porque sua posição é definida pelo topo esquerdo, então vc tira o tamanho do personagem tbm
	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
		x += vel
		left = False
		right = True
	else:
		left = False
		right = False
		walkCount = 0

	if not(isJump):
		'''
		p/ se mover somente na vertical se pular
		if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN] and y < screenWidth - height - vel:
			y += vel'''
		if keys[pygame.K_SPACE]:
			isJump = True
			right = False
			left = False
			walkCount = 0
	else: 
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -=1
		else:
			isJump = False
			jumpCount = 10 

	redrawGameWindown()
	
pygame.quit()
