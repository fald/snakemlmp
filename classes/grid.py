from pygame import Surface
import window

class Grid(window.Window):
    def __init__(self, dimensions):
        self.grid = [[None for x in range(dimensions[0])] for y in range(dimensions[1])]

    def remove(self, index):
        self.grid[index[0]][index[1]] = None

    def add(self, index, object):
        self.grid[index[0]][index[1]] = object


if __name__ == "__main__":
    g = Grid((10, 10))
    print(g.grid)