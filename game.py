### Libraries/Packages ###
import pygame
import time
import settings

### Classes/Functions/Methods ###
class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Tank Vector")
        screen = pygame.display.set_mode((400, 400))
        
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
        pygame.quit()