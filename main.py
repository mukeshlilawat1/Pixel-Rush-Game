import os.path

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Rush")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_Surface = pygame.image.load('graphics/Sky.png').convert()
ground_Surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Pixel Rush', False, 'Black')

#snail setup
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle =  snail_surface.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surf.get_rect(midbottom = (80, 300))

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_Surface, (0, 0))
    screen.blit(ground_Surface, (0,300))
    screen.blit(text_surface, (300, 50))

    snail_rectangle.x -= 4

    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800

    screen.blit(player_surf, player_rectangle)
    screen.blit(snail_surface, snail_rectangle)




    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)