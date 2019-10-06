import pygame
import sys
import pymunk
import pymunk.pygame_util
import random


def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label


def image(window, imageName, x, y):
    image = pygame.image.load(imageName).convert_alpha()
    window.blit(image, (x, y))


def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    x = random.randint(120, 380)
    body.position = x, 550
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    return shape


def add_static_wall(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-300, 300), (300, 300), 5)
    l2 = pymunk.Segment(body, (300, 300), (300, -300), 5)
    l3 = pymunk.Segment(body, (-300, -300), (300, -300), 5)
    l4 = pymunk.Segment(body, (-300, 300), (-300, -300), 5)

    space.add(l1, l2, l3, l4)
    return l1, l2, l3, l4

def main():
    # Start
    pygame.init()
    clock = pygame.time.Clock()

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Set pygame
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('NPC Breakout')

    # Set pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    walls = add_static_wall(space)

    '''
    ball_size = [10, 10]
    ball_pos = [320, 180]
    ball_vel = [5, -5]
    '''

    # Game loop
    while True:
        '''ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    
        if ball_pos[0] == 0 or ball_pos[0] == size[0] - ball_size[0]:
            ball_vel[0] = ball_vel[0] * -1
        if ball_pos[1] == 0 or ball_pos[1] == size[1] - ball_size[1]:
            ball_vel[1] = ball_vel[1] * -1
    
        pygame.draw.rect(screen, white, [ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]])'''

        ball_shape = add_ball(space)
        balls.append(ball_shape)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        space.step(1/30.0)

        space.debug_draw(draw_options)
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
