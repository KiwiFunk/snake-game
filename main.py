import pygame
import sys
from game.game import MAIN
from menus.menu import Menu
from pygame.math import Vector2

pygame.init()

cell_size = 60
grid_size = 17
screen = pygame.display.set_mode((cell_size * grid_size, cell_size * grid_size))
clock = pygame.time.Clock()

# Initialize game states and objects
game_state = "menu"
menu = Menu(screen, grid_size, cell_size)
main_game = MAIN(cell_size, grid_size)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    if game_state == "menu":
        # Handle menu state
        menu.draw()
        game_state = menu.handle_events()
        
    elif game_state == "start":
        # Handle game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == SCREEN_UPDATE:
                main_game.update()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = "menu"
                else:
                    main_game.handle_input(event)

        screen.fill((160, 100, 140))
        main_game.draw_elements(screen)
        pygame.display.update()
    
    clock.tick(60)