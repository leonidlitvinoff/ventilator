import pygame
import math


def turn(alpha, step, s):
    radius = 67
    centre = 100
    shag_v_rad = math.pi / 12
    pygame.draw.polygon(s, pygame.Color('white'),
                        [(centre, centre),
                         (int(centre + radius * math.sin(alpha + shag_v_rad * step)),
                          int(centre + radius * math.cos(alpha + shag_v_rad * step))),
                         (int(centre + radius * math.sin(alpha + shag_v_rad * (step + 2))),
                          int(centre + radius * math.cos(alpha + shag_v_rad * (step + 2))))])


pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
v = 0
alpha = 0
while running:
    tick = clock.tick(30)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, pygame.Color('white'), (101, 101), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                v += math.pi / 90
            elif event.button == 3:
                v -= math.pi / 90
    alpha += v
    if alpha > 6.3:
        alpha = 0
    turn(alpha, 3, screen)
    turn(alpha, 11, screen)
    turn(alpha, 19, screen)
    pygame.display.flip()