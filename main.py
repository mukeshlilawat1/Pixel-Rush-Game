import os.path

import pygame
from sys import exit

from pygame.examples.moveit import GameObject

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Rush")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_Surface = pygame.image.load('graphics/Sky.png').convert()
ground_Surface = pygame.image.load('graphics/ground.png').convert()
score_surface = test_font.render('Pixel Rush', False, (64,64,64))
score_rectangle = score_surface.get_rect(center = (400, 50))

#snail setup
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle =  snail_surface.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_rectangle = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
               if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                   print('collision')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800


    if game_active:
        screen.blit(sky_Surface, (0, 0))
        screen.blit(ground_Surface, (0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        pygame.draw.rect(screen, '#c0e8ec', score_rectangle,10)
        screen.blit(score_surface, score_rectangle)

        snail_rectangle.x -= 4

        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        #player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surf, player_rectangle)

        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill('Yellow')

    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)