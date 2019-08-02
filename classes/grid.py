from pygame import Surface
from window import Window

class Grid(Window):
    def __init__(self, dimensions):
        self.grid = [[None for x in range(dimensions[0])] for y in range(dimensions[1])]

    def remove(self, index):
        self.grid[index[0]][index[1]] = None

    def add(self, index, object):
        self.grid[index[0]][index[1]] = object
