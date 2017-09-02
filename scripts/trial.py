import pygame
from pygame.locals import *

pygame.init
screen = pygame.display.set_mode( (1200,600))
fireball= pygame.image.load("../resources/images/fireball1.png")
while True:
    screen.blit( fireball , (0,0))
    pygame.display.update()

