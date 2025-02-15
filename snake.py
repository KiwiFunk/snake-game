import pygame
import sys
import random
from pygame.math import Vector2

#CLASSES
class Fruit:
    def __init__(self, x_pos, y_pos, cell_size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pos = Vector2(self.x_pos, self.y_pos)
        self.width = cell_size
        self.height = cell_size
    
    def spawn_fruit(self):
        """
        Create a rectangle object and draw it on the display surface
        """
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        pygame.draw.rect(screen, (150, 150, 100), fruit_rect)


def get_random_position(cell_size, max_grid):
    """
    Returns a random int within the specified parameters

    Parameters:
    cell_size (int): Size of the grid cells for calculating X/Y pos.
    max_grid (int): Size of the game grid, function will not return a value OOB.
    """
    return random.randrange(max_grid +1) * cell_size



#init pygame modules
pygame.init()

cell_size = 40
grid_size = 20

#Create a display surface/Game window
screen = pygame.display.set_mode((cell_size * grid_size, cell_size * grid_size))

#Create clock object
clock = pygame.time.Clock()

#Create a fruit object
test_fruit = Fruit(get_random_position(cell_size, grid_size), get_random_position(cell_size, grid_size), cell_size)

#GAME LOOP START
while True:

    #Listen for events
    for event in pygame.event.get():

        #If window is closed, ensure game and code execution is ended
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Takes RGB value as a tuple
    screen.fill((160, 200, 40))
    

    test_fruit.spawn_fruit()



    #Update game display
    pygame.display.update()

    #Limit to 60 loops per second
    clock.tick(60)