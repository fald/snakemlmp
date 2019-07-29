import pygame
from pygame.locals import *
from random import choice

class AI:
    def __init__(self):
        self.a = 1

    def determine_move(self, board, moves):
        raise NotImplementedError("This method has not been implemented for this AI!")

class Basic(AI):
    def __init__(self):
        super(Basic, self).__init__()

    def determine_move(self, board, moves):
        # Real fuckin' dumb!
        return choice(moves)

class ML(AI):
    pass