# menu.py
import pygame
import sys


class Menu:
    def __init__(self, screen, grid_size, cell_size):
        self.screen = screen
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.font = pygame.font.Font('assets/fonts/sprint-2.ttf', 30)
        self.titlefont = pygame.font.Font('assets/fonts/sprint-2.ttf', 100)

    def draw_grass(self, screen):
        grass_color = (170, 215, 81)
        grass_dark = (160, 208, 72)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                color = grass_color if (row + col) % 2 == 0 else grass_dark
                pygame.draw.rect(screen, color, grass_rect)

    def draw(self):
        #self.screen.fill((0, 0, 0))  # black background

        self.draw_grass(self.screen)

        title_text = self.titlefont.render("Snake", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 4))
        self.screen.blit(title_text, title_rect)

        start_text = self.font.render("Press Enter to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 2))
        self.screen.blit(start_text, start_rect)

        quit_text = self.font.render("Press Esc to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 1.5))
        self.screen.blit(quit_text, quit_rect)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "start"  # Start the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return "menu"

