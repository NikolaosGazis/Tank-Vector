### Libraries/Packages ###
import pygame
import time
import settings
from src.world import World
from player import Player
from camera import Camera

### Classes/Functions/Methods ###
class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Tank Vector")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        
        self.world = World()
        screen_w, screen_h = self.screen.get_size() # Fetch screen's actual resolution.
        self.player = Player(screen_w // 2, screen_h // 2) # Center.
        self.camera = Camera(screen_w, screen_h)
        
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Movement Update #
            self.player.update()
            self.camera.update(self.player.x, self.player.y)
        
            # Draw #
            self.world.draw(self.screen, self.camera.offset)
            self.player.draw(self.screen, self.camera.offset)
            pygame.display.flip()

            self.clock.tick(settings.FPS)
        
        pygame.quit()