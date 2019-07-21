from constants import colors
from constants.enums import Locations
import sys

# I guess these technically aren't constants?

# Graphics, resolutions.
RESOLUTION = (800, 440)
WINDOW_TITLE = "SnAIke"
WINDOW_ICON = None
WINDOW_BUFFER = 10

PLAY_AREA_DIMENSIONS = (25, 25)
PLAY_AREA_LOCATION = Locations.TOP_LEFT
SCORE_BOARD_RESOLUTION = (395, 25)
SCORE_BOARD_LOCATION = Locations.BOTTOM_LEFT
AI_SETTINGS_RESOLUTION = (380, 400)
AI_SETTINGS_LOCATION = Locations.TOP_RIGHT
MAIN_MENU_RESOLUTION = (800, 400)
MAIN_MENU_LOCATION = Locations.CENTER
PAUSE_MENU_RESOLUTION = (400, 200)
PAUSE_MENU_LOCATION = Locations.CENTER
GAME_SETTINGS_RESOLUTION = (400, 200)
GAME_SETTINGS_LOCATION = Locations.CENTER

FPS = 60
BLOCK_SIZE = 16

BACKGROUND = colors.BLACK
WINDOW_BACKGROUND = colors.GREY

FONT = "umeuigothic"
FONT_SMALL = 20
FONT_MEDIUM = 32
FONT_LARGE = 64
FONT_BOLD = False

# Images to load
SNAKE_BODY_IMAGE = "./assets/snake_body.png"
SNAKE_HEAD_IMAGE = "./assets/snake_head.png"
APPLE_IMAGE = "./assets/snake_food.png"

# Game difficulty (lol)
START_LENGTH = 3
NUM_PLAYERS = 1
START_GAME_SPEED = 16
MAX_GAME_SPEED = 32
