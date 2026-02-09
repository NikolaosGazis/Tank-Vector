### Libraries/Pakcages ###
import pygame
import math
from settings import *

### Classes/Functions/Methods ###
class Player:
    def __init__(self, x, y): # Player will guide a circle.
        self.x = x
        self.y = y
        self.radius = 20
        self.color = PLAYER_COLOR
        self.speed = PLAYER_SPEED
        
        self.barrel_length = 30
        self.barrel_width = 8
        self.barrel_color = BARREL_COLOR

        # Stats #
        self.stat_levels = {name: 0 for name in STAT_NAMES}
        self.stat_points = STAT_STARTING_LEVEL
        self.level = 1
        self.xp = 0

        # Player's HP based on the Max Health stat #
        self.hp = self.get_stat("max_hp")

    def get_stat(self, name):
        cfg = STATS_CONFIG[name]
        return cfg["base"] + self.stat_levels[name] * cfg["per_level"]

    def allocate_stat(self, stat_name):
        pass

    def hp_regen_update(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: # Verically.
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen, camera_offset=(0, 0)):
        sx = self.x - camera_offset[0]
        sy = self.y - camera_offset[1]
        
        # Move the barrel based on the mouse cursor #
        mx, my = pygame.mouse.get_pos()
        angle = math.atan2(my - sy, mx - sx)
        
        # Barrel rotation #
        half_w = self.barrel_width / 2
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        perp_x = -sin_a * half_w
        perp_y = cos_a * half_w
        end_x = sx + cos_a * self.barrel_length
        end_y = sy + sin_a * self.barrel_length
        
        points = [
            (sx + perp_x, sy + perp_y),
            (sx - perp_x, sy - perp_y),
            (end_x - perp_x, end_y - perp_y),
            (end_x + perp_x, end_y + perp_y),
        ]

        pygame.draw.polygon(screen, self.barrel_color, points)
        pygame.draw.circle(screen, self.color, (int(sx), int(sy)), self.radius)

    def draw_hp_bar(self, screen, sx, sy):
        pass