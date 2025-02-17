import pygame
import math
from random import randrange
from pygame.math import Vector2

class Fruit:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.pos = Vector2(14, 8)
        self.sprites = self._load_sprites()
        self.current_sprite = self.sprites[0]
        self.sprite = self.current_sprite
        self.time = 0
        self.animation_speed = 0.025
        self.max_scale_change = 10
        self.midpoint_size = self.cell_size
        self.rect = self.sprite.get_rect()
        self.rect.center = (
            self.pos.x * self.cell_size + self.cell_size // 2,
            self.pos.y * self.cell_size + self.cell_size // 2
        )

    def _load_sprites(self):
        sprite_files = [
            'assets/fruits/watermelon.png',
            'assets/fruits/orange.png', 
            'assets/fruits/strawb.png'
        ]
        return [
            pygame.transform.smoothscale(
                pygame.image.load(file).convert_alpha(),
                (self.cell_size, self.cell_size)
            )
            for file in sprite_files
        ]

    def scale_anim(self):
        self.time += 1
        new_size = self.max_scale_change * math.sin(self.animation_speed * self.time * math.pi) + self.midpoint_size
        self.sprite = pygame.transform.smoothscale(
            self.current_sprite,
            (int(new_size), int(new_size))
        )
        old_center = self.rect.center
        self.rect = self.sprite.get_rect()
        self.rect.center = old_center

    def draw_fruit(self, screen):
        screen.blit(self.sprite, self.rect)

    def new_fruit(self, grid_size):
        self.pos = Vector2(randrange(grid_size), randrange(grid_size))
        self.current_sprite = self.sprites[randrange(len(self.sprites))]
        self.sprite = self.current_sprite
        self.rect.center = (
            self.pos.x * self.cell_size + self.cell_size // 2,
            self.pos.y * self.cell_size + self.cell_size // 2
        )
