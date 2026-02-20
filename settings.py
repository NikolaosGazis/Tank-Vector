### Parameters/Fixed Variables ###

# Global #
FPS = 60

# World # 
TILE_SIZE = 64
WORLD_HEIGHT = 6400
WORLD_WIDTH = 6400
TILE_COLOR_1 = (45, 45, 45)
TILE_COLOR_2 = (50, 50, 50)

# Player #
PLAYER_COLOR = (0, 120, 255)
BARREL_COLOR = (80, 80, 80)
PLAYER_SPEED = 4

# Player Stats #
STAT_STARTING_LEVEL = 0
STAT_MAX_LEVEL = 7

STAT_NAMES = [
    "max_hp",
    "health_regen",
    "body damage", # When collided.
    "bullet_damage",
    "bullet_speed",
    "bullet_pen",
    "reload_speed",
    "move_speed",
]

STAT_DISPLAYED_NAMES = {
    "max_hp":           "Max Health",
    "health_regen":     "Health Regen",
    "body damage":      "Body Damage",
    "bullet_damage":    "Bullet Damage",
    "bullet_speed":     "Bullet Speed",
    "bullet_pen":       "Bullet Penetration",
    "reload_speed":     "Reload Speed",
    "move_speed":       "Movement Speed",
}

STATS_CONFIG = { # Upgradeable stats.
    "max_hp":        {"base": 50,  "per_level": 20},
    "health_regen":  {"base": 0,   "per_level": 0.5},
    "body damage":   {"base": 10,  "per_level": 5},
    "bullet_damage": {"base": 10,  "per_level": 5},
    "bullet_speed":  {"base": 5,   "per_level": 1},
    "bullet_pen":    {"base": 1,   "per_level": 1},
    "reload_speed":  {"base": 1,   "per_level": 0.5},
    "move_speed":    {"base": 4,   "per_level": 0.4},
}

# HUD #
SCORE = 0