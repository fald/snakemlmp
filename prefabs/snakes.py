from classes import snake
from constants import settings
from constants import enums

player_1_snake = snake.Snake()

player_2_controls = {
    K_DOWN: Directions.DOWN,
    K_UP: Directions.UP,
    K_LEFT: Directions.LEFT,
    K_RIGHT: Directions.RIGHT
}

player_2_snake = snake.Snake(
    head_image="", body_image="", start_direction=enums.Directions.LEFT,
    start_location=(settings.PLAY_AREA_DIMENSIONS[0] - 1, settings.PLAY_AREA_DIMENSIONS[1] - 1), 
    components={'controls': player_2_controls,  'ai': None}
    )
