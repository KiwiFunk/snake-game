import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self, cell_size):
        self.width = cell_size
        self.height = cell_size
        self.body = [Vector2(4, 8), Vector2(3, 8), Vector2(2, 8)]
        self.direction = Vector2(-1, 0)
        self.game_started = False

        # Init sprites
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

        # Sounds
        self.leftkey_sound = pygame.mixer.Sound('assets/sounds/key1.wav')
        self.rightkey_sound = pygame.mixer.Sound('assets/sounds/key2.wav')
        self.upkey_sound = pygame.mixer.Sound('assets/sounds/key3.wav')
        self.downkey_sound = pygame.mixer.Sound('assets/sounds/key4.wav')
        self.eat_sound = pygame.mixer.Sound('assets/sounds/Eat.wav')

    def draw_snake(self, screen):
        self.update_head_sprite()
        self.update_tail_sprite()

        for i, e in enumerate(self.body):
            e_rect = pygame.Rect(e.x * self.width, e.y * self.height, self.width, self.height)

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
        head_rel = self.body[1] - self.body[0]
        if head_rel == Vector2(1, 0): self.head = self.head_left
        elif head_rel == Vector2(-1, 0): self.head = self.head_right
        elif head_rel == Vector2(0, 1): self.head = self.head_up
        elif head_rel == Vector2(0, -1): self.head = self.head_down

    def update_tail_sprite(self):
        tail_rel = self.body[-2] - self.body[-1]
        if tail_rel == Vector2(-1, 0): self.tail = self.tail_left
        elif tail_rel == Vector2(1, 0): self.tail = self.tail_right
        elif tail_rel == Vector2(0, -1): self.tail = self.tail_up
        elif tail_rel == Vector2(0, 1): self.tail = self.tail_down

    def change_direction(self, new_direction, audio_file):
        if self.game_started:
            if new_direction.x != self.direction.x and new_direction.y != self.direction.y:
                self.direction = new_direction
                getattr(self, audio_file).play()
        else:
            if new_direction.x != self.direction.x:
                self.direction = new_direction
                getattr(self, audio_file).play()
                self.game_started = True

    def move_snake(self):
        if self.game_started:
            body_new = self.body[:]
            body_new.insert(0, body_new[0] + self.direction)
            body_new.pop()
            self.body = body_new

    def grow(self):
        tail = self.body[-1]
        direction = self.body[-1] - self.body[-2]
        new_segment = Vector2(tail.x + direction.x, tail.y + direction.y)
        self.body.append(new_segment)

    def eat_fruit_audio(self):
        self.eat_sound.set_volume(0.2)
        self.eat_sound.play()

    def reset(self):
        """
        Called on game end conditions
        """
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]

        #replace with calling the gameover.py contents
