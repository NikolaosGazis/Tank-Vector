### Libraries/Packages ###
from settings import *

### Classes/Functions/Methods ###
class Camera:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.x = 0
        self.y = 0
    
    def update(self, target_x, target_y):
        # Follow the Player #
        self.x = target_x - self.screen_w // 2
        self.y = target_y - self.screen_h // 2
    
        # Avoid showing the outside of the world #
        self.x = max(0, min(self.x, WORLD_WIDTH - self.screen_w))
        self.y = max(0, min(self.y, WORLD_HEIGHT - self.screen_h))
    
    @property
    def offset(self):
        return (self.x, self.y)