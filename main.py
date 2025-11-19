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
score_surface = test_font.render('Pixel Rush', False, (64,64,64))
score_rectangle = score_surface.get_rect(center = (400, 50))

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

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #    if player_rectangle.collidepoint(event.pos):
        #        print('collision')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_Surface, (0, 0))
    screen.blit(ground_Surface, (0,300))
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle,10)
    screen.blit(score_surface, score_rectangle)

    snail_rectangle.x -= 4

    if snail_rectangle.right <= 0:

        snail_rectangle.left = 800

    screen.blit(player_surf, player_rectangle)
    screen.blit(snail_surface, snail_rectangle)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')


     #collision detection
    # if player_rectangle.colliderect(snail_rectangle):
    #     print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rectangle.collidepoint(mouse_pos):
        # print('collision')
       print(pygame.mouse.get_pressed())



    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)