### Libraries/Packages ###
import pygame
from settings import *

### Classes/Functions/Methods ###
class World:
    def __init__(self):
        self.surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
        self.generate_tiles()
    
    def generate_tiles(self):
        rows = WORLD_HEIGHT // TILE_SIZE
        cols = WORLD_WIDTH // TILE_SIZE
        
        for row in range(rows):
            for col in range(cols):
                color = TILE_COLOR_1 if (row + col) % 2 == 0 else TILE_COLOR_2
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.surface, color, rect)
    
    def draw(self, screen, camera_offset=(0, 0)):
        screen.blit(self.surface, (-camera_offset[0], -camera_offset[1]))