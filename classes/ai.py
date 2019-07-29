import pygame
from pygame.locals import *
from constants.enums import Directions
from random import choice

class AI:

    outputs = [
        Directions.DOWN,
        Directions.LEFT,
        Directions.UP,
        Directions.RIGHT
    ]

    def __init__(self):
        pass

    def determine_move(self, board, moves):
        raise NotImplementedError("This method has not been implemented for this AI!")

class Basic(AI):
    def __init__(self):
        super(Basic, self).__init__()

    def determine_move(self, board):
        # Real fuckin' dumb!
        return choice(AI.outputs)

class ML(AI):
    def __init__(self):
        super(ML, self).__init__()
    
    def determine_move(self, board):
        pass

    def convert_relative_to_absolute(self, relative):
        # Relative left
        # If facing abs UP -> LT        (0, -1) ->  (-1, 0)     Flip
        #               DN -> RT        (0, 1)  ->  (1, 0)      Flip
        #               RT -> UP        (1, 0)  ->  (0, -1)     Flip + Invert
        #               LT -> DN        (-1, 0) ->  (0, 1)      Flip + Invert
        # Relative right
        # If facing abs UP -> RT        (0, -1) ->  (1, 0)      Flip + Invert
        #               RT -> DN        (1, 0)  ->  (0, 1)      Flip
        #               DN -> LT        (0, 1)  ->  (-1, 0)     Flip + Invert
        #               LT -> UP        (-1, 0) ->  (0, -1)     Flip
        # Relative ahead
        # No change

        # If not ahead,
        # a, b = b, a
        #   if relative left and b == 0:
        #       a *= -1
        #   if relative left and b != 0:
        #       b *= -1
    
    def check_obstacle(self, direction):
        pass
    
    def check_obstacles(self):
        pass