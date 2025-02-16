import pygame, sys
from random import randrange
from pygame.math import Vector2

#CLASSES
class Snake:
    def __init__(self, cell_size):
        self.width = cell_size
        self.height = cell_size
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3,10)]
        self.direction = Vector2(-1, 0)
        self.game_started = False

        #Init sprites
        self.head_up = pygame.image.load('assets/snake/Head.png').convert_alpha()
        self.head_up = pygame.transform.smoothscale(self.head_up, (self.width, self.height))
        self.head_down = pygame.transform.rotate(self.head_up, 180)
        self.head_right = pygame.transform.rotate(self.head_up, -90)
        self.head_left = pygame.transform.rotate(self.head_up, 90)

        self.body_vertical = pygame.image.load('assets/snake/Body.png').convert_alpha()
        self.body_vertical = pygame.transform.smoothscale(self.body_vertical, (self.width, self.height))
        self.body_horizontal = pygame.transform.rotate(self.body_vertical, 90)

        self.tail_up = pygame.image.load('assets/snake/Tail.png').convert_alpha()
        self.tail_up = pygame.transform.smoothscale(self.tail_up, (self.width, self.height))
        self.tail_down = pygame.transform.rotate(self.tail_up, 180)
        self.tail_right = pygame.transform.rotate(self.tail_up, -90)
        self.tail_left = pygame.transform.rotate(self.tail_up, 90)

        self.body_bl = pygame.image.load('assets/snake/BendLeft.png').convert_alpha()
        self.body_bl = pygame.transform.smoothscale(self.body_bl, (self.width, self.height))
        self.body_br = pygame.image.load('assets/snake/BendRight.png').convert_alpha()
        self.body_br = pygame.transform.smoothscale(self.body_br, (self.width, self.height))

        self.body_ul = pygame.transform.rotate(self.body_bl, 180)
        self.body_ur = pygame.transform.rotate(self.body_br, 180)

        #Sounds
        self.leftkey_sound = pygame.mixer.Sound('assets/sounds/key1.wav')
        self.rightkey_sound = pygame.mixer.Sound('assets/sounds/key2.wav')
        self.upkey_sound = pygame.mixer.Sound('assets/sounds/key3.wav')
        self.downkey_sound = pygame.mixer.Sound('assets/sounds/key4.wav')
        self.eat_sound = pygame.mixer.Sound('assets/sounds/Eat.wav')

    def draw_snake(self):
        """
        """
        self.update_head_sprite()
        self.update_tail_sprite()

        #i = index e = element
        for i, e in enumerate(self.body):
            #Create a rect object for positioning
            e_rect = pygame.Rect(e.x * self.width, e.y * self.height, self.width, self.height)
            #pygame.draw.rect(screen, (100, 100, 100), e_rect)

            #Calculate direction snake is heading
            if i == 0:
                screen.blit(self.head, e_rect)

            elif i == len(self.body)-1:
                screen.blit(self.tail, e_rect)

            else:
                prev_element = self.body[i + 1] - e
                next_element = self.body[i - 1] - e

                if prev_element.x == next_element.x:
                    screen.blit(self.body_vertical, e_rect)
                elif prev_element.y == next_element.y:
                    screen.blit(self.body_horizontal, e_rect)
                else:
                    if (prev_element.x == -1 and next_element.y == -1) or (prev_element.y == -1 and next_element.x == -1):
                        screen.blit(self.body_ur, e_rect)
                    elif (prev_element.x == 1 and next_element.y == -1) or (prev_element.y == -1 and next_element.x == 1):
                        screen.blit(self.body_ul, e_rect)
                    elif (prev_element.x == -1 and next_element.y == 1) or (prev_element.y == 1 and next_element.x == -1):
                        screen.blit(self.body_bl, e_rect)
                    elif (prev_element.x == 1 and next_element.y == 1) or (prev_element.y == 1 and next_element.x == 1):
                        screen.blit(self.body_br, e_rect)

    def update_head_sprite(self):
        """
        Create a new vector based on the relationship between the head, and the first element after.
        Use to calculate direction and assign approriate sprite
        """
        head_rel = self.body[1] - self.body[0]
        if head_rel == Vector2(1, 0): self.head = self.head_left
        elif head_rel == Vector2(-1, 0): self.head = self.head_right
        elif head_rel == Vector2(0, 1): self.head = self.head_up
        elif head_rel == Vector2(0, -1): self.head = self.head_down

    def update_tail_sprite(self):
        """
        Create a new vector based on the relationship between the tail, and the first element before.
        Use to calculate direction and assign approriate sprite
        """
        tail_rel = self.body[-2] - self.body[-1]
        if tail_rel == Vector2(-1, 0): self.tail = self.tail_left
        elif tail_rel == Vector2(1, 0): self.tail = self.tail_right
        elif tail_rel == Vector2(0, -1): self.tail = self.tail_up
        elif tail_rel == Vector2(0, 1): self.tail = self.tail_down

    def change_direction(self, new_direction, audio_file):
        """
        Perform logic checks to make sure inputs of the same axis are ignored before setting new direction

        Parameters:
        new_direction: Takes an input of Vector2(x, y)
        audio_file: Takes a string of the correct audio to play
        """
        #if the opposite of the new input does not equal the old one, set direction as new input
        if self.game_started:
            if new_direction.x != self.direction.x and new_direction.y != self.direction.y:
                self.direction = new_direction
                #play the specified audio
                getattr(self, audio_file).play()
        else:
            if new_direction.x != self.direction.x:
                self.direction = new_direction
                getattr(self, audio_file).play()
                self.game_started = True
            
    def move_snake(self):
        if self.game_started:
            #Create copy of body list, using slice : to make sure we have unique lists
            body_new = self.body[:]
            #Add new head at position 0
            body_new.insert(0, body_new[0] + self.direction)
            #Remove the last segment and copy new list to body list
            body_new.pop()
            self.body = body_new

    def grow(self):
        self.body.append(self.body[-1])

    def eat_fruit_audio(self):
        self.eat_sound.set_volume(0.2)
        self.eat_sound.play()

class Fruit:
    def __init__(self, cell_size):
        #Vector2(x, y)
        self.pos = Vector2(15, 10)
        self.width = cell_size
        self.height = cell_size
        self.sprite = pygame.image.load('assets/fruits/watermelon.png').convert_alpha()
        self.sprite_scaled = pygame.transform.smoothscale(self.sprite, (self.width, self.height))
    
    def draw_fruit(self):
        """
        Create a rectangle object and draw it on the display surface
        """
        fruit_rect = pygame.Rect(self.pos.x * self.width, self.pos.y * self.height, self.width, self.height)
        screen.blit(self.sprite_scaled, fruit_rect)
        #pygame.draw.rect(screen, (150, 150, 100), fruit_rect)

    def new_fruit(self, grid_size):
        """
        Move the fruit to a new randomized location within the grid
        """
        self.pos = Vector2(randrange(grid_size), randrange(grid_size))

class MAIN:
    def __init__(self, cell_size, grid_size):
        self.snake = Snake(cell_size)
        self.fruit = Fruit(cell_size)
        self.grid = grid_size
        self.cell = cell_size
        self.heading_font = pygame.font.Font('assets/fonts/sprint-2.ttf', 30)

    def update(self):
        """
        Update the game loop
        """
        self.snake.move_snake()
        self.check_positions()
        self.game_end_check()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_positions(self):
        if self.fruit.pos == self.snake.body[0]:
            print("NOMF")
            self.snake.eat_fruit_audio()
            self.fruit.new_fruit(self.grid)
            self.snake.grow()

    def game_end_check(self):
        """
        Checks to see if snake is outside display surface, or has hit itself
        """
        #If snake has collided with itself
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()
        #Check if snake.body[0] falls in a range between 0 and the grid size for both axis
        if not (0 <= self.snake.body[0].x < self.grid) or not (0 <= self.snake.body[0].y < self.grid):
            self.game_over()

    def game_over(self):
        print("Game Over")
        pygame.quit()
        sys.exit()
    
    def draw_grass(self):
        grass_color = (170, 215, 81)
        grass_dark = (160, 208, 72)

        for row in range(self.grid):
            for col in range(self.grid):
                grass_rect = pygame.Rect(col * self.cell, row * self.cell, self.cell, self.cell)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, grass_color, grass_rect)
                else:
                    pygame.draw.rect(screen, grass_dark, grass_rect)

    def draw_score(self):
        score_text = str((len(self.snake.body) - 3) * 10)
        score_surface = self.heading_font.render(score_text, True, (255,255,255))
        score_xy = ((self.grid * self.cell / 2), self.grid)

        # Create a black outline
        outline_surface = self.heading_font.render(score_text, True, (0, 0, 0))
        outline_rect = outline_surface.get_rect(center = score_xy)

        # Blit the outline first
        for offset in [(2, 2), (2, -2), (-2, 2), (-2, -2)]:
            screen.blit(outline_surface, outline_rect.move(offset))

        # Blit the main score text
        score_rect = score_surface.get_rect(center = score_xy)
        screen.blit(score_surface, score_rect)


#init pygame modules
pygame.mixer.pre_init(44100, -16, 2, 512)
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
                main_game.snake.change_direction(Vector2(0, -1), 'upkey_sound')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main_game.snake.change_direction(Vector2(0, 1), 'downkey_sound')
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_game.snake.change_direction(Vector2(-1, 0), 'leftkey_sound')
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_game.snake.change_direction(Vector2(1, 0), 'rightkey_sound')

    #Takes RGB value as a tuple. OLD FILL, DEPRECIATED
    screen.fill((160, 100, 140))
    
    main_game.draw_elements()

    #Update game display
    pygame.display.update()

    #Limit to 60 loops per second
    clock.tick(60)