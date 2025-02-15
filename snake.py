import pygame
import sys

#init pygame modules
pygame.init()

#Create a display surface/Game window
screen = pygame.display.set_mode((500, 500))

#Create clock object
clock = pygame.time.Clock()

#GAME LOOP START
while True:

    #Listen for events
    for event in pygame.event.get():
        #If window is closed, ensure game and code execution is ended
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Update game display
    pygame.display.update()

    #Limit to 60 loops per second
    clock.tick(60)