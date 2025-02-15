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
        self.cell_size = cell_size
        self.width = cell_size
        self.height = cell_size
    
    def spawn_fruit(self):
        """
        Create a rectangle object and draw it on the display surface
        """
        fruit_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.width, self.height)
        pygame.draw.rect(screen, (150, 150, 100), fruit_rect)


def get_random_position(max_grid):
    """
    Returns a tuple for (x, y) containing randomly genereated int values within the specified parameters

    Parameters:
    max_grid (int): Size of the game grid, function will not return a value OOB.
    """
    x = random.randrange(max_grid +1)
    y = random.randrange(max_grid +1)
    return x, y



#init pygame modules
pygame.init()

cell_size = 40
grid_size = 20

#Create a display surface/Game window
screen = pygame.display.set_mode((cell_size * grid_size, cell_size * grid_size))

#Create clock object
clock = pygame.time.Clock()

#Create a fruit object
fx, fy = get_random_position(grid_size)
test_fruit = Fruit(fx, fy, cell_size)

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