import pygame
import sys
from game.game import MAIN
from pygame.math import Vector2

pygame.init()

cell_size = 60
grid_size = 17
screen = pygame.display.set_mode((cell_size * grid_size, cell_size * grid_size))
clock = pygame.time.Clock()

main_game = MAIN(cell_size, grid_size)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            main_game.handle_input(event)

    screen.fill((160, 100, 140))
    main_game.draw_elements(screen)
    pygame.display.update()
    clock.tick(60)
