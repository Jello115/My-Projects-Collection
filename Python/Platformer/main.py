import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if pygame.K_RIGHT:
                pass
            if pygame.K_LEFT:
                pass
            if pygame.K_SPACE:
                pass
   
    screen.fill(BG_COLOR)
    level.run()

    pygame.display.update()
    clock.tick(60)