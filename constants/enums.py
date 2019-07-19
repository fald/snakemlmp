from enum import Enum

class Directions(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

class Locations(Enum):
    TOP_LEFT = (0, 0)
    BOTTOM_LEFT = (0, 1)
    TOP_RIGHT = (1, 0)
    BOTTOM_RIGHT = (1, 1)
    TOP = (0.5, 0)
    BOTTOM = (0.5, 1)
    LEFT = (0, 0.5)
    RIGHT = (1, 0.5)
    CENTER = (0.5, 0.5)

class GameStates(Enum):
    PLAYING = 0
    PAUSED = 1
    MAIN_MENU = 2
    SETTINGS = 3
    GAME_OVER = 4
    NEW_GAME = 5
