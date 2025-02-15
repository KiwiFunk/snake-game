import pygame
import sys
from random import randrange
from pygame.math import Vector2

#CLASSES

class Snake:
    def __init__(self, cell_size):
        self.width = cell_size
        self.height = cell_size
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7,10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for e in self.body:
            e_rect = pygame.Rect(e.x * self.width, e.y * self.height, self.width, self.height)
            pygame.draw.rect(screen, (100, 100, 100), e_rect)

    def move_snake(self):
        #Create copy of body list, using slice : to make sure we have unique lists
        body_new = self.body[:]
        #Add new head at position 0
        body_new.insert(0, body_new[0] + self.direction)
        #Remove the last segment and copy new list to body list
        body_new.pop()
        self.body = body_new

class Fruit:
    def __init__(self, cell_size, grid_size):
        #Vector2(x, y)
        self.pos = Vector2(randrange(grid_size), randrange(grid_size))
        self.width = cell_size
        self.height = cell_size
    
    def spawn_fruit(self):
        """
        Create a rectangle object and draw it on the display surface
        """
        fruit_rect = pygame.Rect(self.pos.x * self.width, self.pos.y * self.height, self.width, self.height)
        pygame.draw.rect(screen, (150, 150, 100), fruit_rect)

class MAIN:
    def __init__(self, cell_size, grid_size):
        self.snake = Snake(cell_size)
        self.fruit = Fruit(cell_size, grid_size)

    def update(self):
        """
        Update the game loop
        """
        self.snake.move_snake()
        self.check_positions()

    def draw_elements(self):
        self.fruit.spawn_fruit()
        self.snake.draw_snake()

    def check_positions(self):
        if self.fruit.pos == self.snake.body[0]:
            print("NOMF")



#init pygame modules
pygame.init()

cell_size = 40
grid_size = 20

#Create a display surface/Game window
screen = pygame.display.set_mode((cell_size * grid_size, cell_size * grid_size))

#Create clock object
clock = pygame.time.Clock()

main_game = MAIN(cell_size, grid_size)

#Controls how often the screen is updated. Use to increase snake speed in later levels?
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

#GAME LOOP START
while True:

    #Listen for events
    for event in pygame.event.get():

        #If window is closed, ensure game and code execution is ended
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SCREEN_UPDATE:
            main_game.update()
        #Listen for WASD or arrows and set snake.direction accordingly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_game.snake.direction = Vector2(1, 0)

    #Takes RGB value as a tuple
    screen.fill((160, 200, 40))
    
    main_game.draw_elements()

    #Update game display
    pygame.display.update()

    #Limit to 60 loops per second
    clock.tick(60)