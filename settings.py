# game options/settings
TITLE = "Cloud Jumpy!"
WIDTH = 550
HEIGHT = 800
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 1.4
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 25

#starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (20, HEIGHT - 350),
                 (75, 75),
                 (10, 30)]

# define colors
WHITE = (100, 255, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (100, 255, 166)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE