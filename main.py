import os.path

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Rush")
clock = pygame.time.Clock()

sky_Surface = pygame.image.load('graphics/Sky.png')
ground_Surface = pygame.image.load('graphics/ground.png')

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_Surface, (0,0))
    screen.blit(sky_Surface, (0,0))
    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)