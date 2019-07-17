from constants import colors
from constants.enums import Locations
import sys

# Graphics, resolutions.
RESOLUTION = (810, 410)
WINDOW_TITLE = "SnAIke"
WINDOW_ICON = None

PLAY_AREA_DIMENSIONS = (3, 3)
PLAY_AREA_LOCATION = Locations.BOTTOM
SCORE_BOARD_RESOLUTION = (400, 40)
SCORE_BOARD_LOCATION = Locations.TOP

FPS = 60
BLOCK_SIZE = 16

BACKGROUND = colors.BLACK

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
START_GAME_SPEED = 1
MAX_GAME_SPEED = 32
