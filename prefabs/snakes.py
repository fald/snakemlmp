from classes import snake
from constants import settings
from constants import enums
from constants.enums import Directions
from pygame.locals import *

player_1_snake = snake.Snake()

player_2_controls = {
    K_DOWN: Directions.DOWN,
    K_UP: Directions.UP,
    K_LEFT: Directions.LEFT,
    K_RIGHT: Directions.RIGHT
}

player_2_snake = snake.Snake(
    head_image=settings.SNAKE_HEAD_IMAGE_2, body_image=settings.SNAKE_BODY_IMAGE_2, start_direction=enums.Directions.LEFT,
    start_location=(settings.PLAY_AREA_DIMENSIONS[0] - 1, settings.PLAY_AREA_DIMENSIONS[1] - 1), 
    components={'controls': player_2_controls,  'ai': None}
    )
