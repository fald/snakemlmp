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
    pass