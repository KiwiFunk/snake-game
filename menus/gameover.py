# gameover.py
import pygame
import sys

class GameOver:
    def __init__(self, screen, grid_size, cell_size, score):
        self.screen = screen
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.score = score
        self.font = pygame.font.Font('assets/fonts/LeoRoundedProMedium.ttf', 45)
        self.heading = pygame.font.Font('assets/fonts/LeoRoundedProMedium.ttf', 65)

    def draw(self):

        self.screen.fill((170, 215, 81))  # basic bg fill

        game_over_text = self.heading.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 4))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 2))
        self.screen.blit(score_text, score_rect)

        #Insert logic for highscore processing here

        restart_text = self.font.render("Press Enter to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 1.5))
        self.screen.blit(restart_text, restart_rect)

        quit_text = self.font.render("Press Esc to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.grid_size * self.cell_size // 2, self.grid_size * self.cell_size // 1.25))
        self.screen.blit(quit_text, quit_rect)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "restart"  # Restart the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return "gameover"
