import pygame
import sys
from game.snake import Snake
from game.fruit import Fruit
from pygame.math import Vector2

class MAIN:
    def __init__(self, cell_size, grid_size):
        self.snake = Snake(cell_size)
        self.fruit = Fruit(cell_size)
        self.grid = grid_size
        self.cell = cell_size
        self.heading_font = pygame.font.Font('assets/fonts/sprint-2.ttf', 30)

    def update(self):
        self.snake.move_snake()
        self.check_positions()
        self.game_end_check()

    def draw_elements(self, screen):
        self.draw_grass(screen)
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen)
        self.draw_score(screen)
        self.fruit.scale_anim()

    def check_positions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.eat_fruit_audio()
            self.fruit.new_fruit(self.grid)
            self.snake.grow()

        for e in self.snake.body[1:]:
            if e == self.fruit.pos:
                self.fruit.new_fruit(self.grid)

    def game_end_check(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()
        if not (0 <= self.snake.body[0].x < self.grid) or not (0 <= self.snake.body[0].y < self.grid):
            self.game_over()

    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self, screen):
        grass_color = (170, 215, 81)
        grass_dark = (160, 208, 72)
        for row in range(self.grid):
            for col in range(self.grid):
                grass_rect = pygame.Rect(col * self.cell, row * self.cell, self.cell, self.cell)
                color = grass_color if (row + col) % 2 == 0 else grass_dark
                pygame.draw.rect(screen, color, grass_rect)

    def draw_score(self, screen):
        score_text = str((len(self.snake.body) - 3) * 10)
        score_surface = self.heading_font.render(score_text, True, (255, 255, 255))
        score_xy = ((self.grid * self.cell / 2), 30)
        outline_surface = self.heading_font.render(score_text, True, (0, 0, 0))
        outline_rect = outline_surface.get_rect(center = score_xy)
        for offset in [(2, 2), (2, -2), (-2, 2), (-2, -2)]:
            screen.blit(outline_surface, outline_rect.move(offset))
        score_rect = score_surface.get_rect(center = score_xy)
        screen.blit(score_surface, score_rect)

    def handle_input(self, event):
        """Handle keyboard input events"""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.snake.change_direction(Vector2(0, -1), 'upkey_sound')
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.snake.change_direction(Vector2(0, 1), 'downkey_sound')
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self.snake.change_direction(Vector2(-1, 0), 'leftkey_sound')
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.snake.change_direction(Vector2(1, 0), 'rightkey_sound')
