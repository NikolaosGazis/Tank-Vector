### Libraries/Packages ###
import pygame
from settings import *

### Classes/Functions/Methods ###
class HUD:
    def __init__(self):
        pygame.font.init()

        self.font = pygame.font.SysFont("Arial", 28, bold=True)
    
    def draw(self, screen, score):
        # Score #
        text_score = self.font.render(f"Score: {score}", True, (255, 255, 255))
        x = screen.get_width() // 2 - text_score.get_width() // 2 # Center.
        screen.blit(text_score, (x, 10))