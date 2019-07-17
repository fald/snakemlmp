from pygame import Surface

# class Window(Surface):
#     # Just a modded surface that'll take into account grid style coords.
#     # Hm, but maybe just a grid that's a 2d array would be best.
#     pass

# This was a bad idea
class Grid:
    def __init__(self, dimensions):
        self.grid = [[None for x in range(dimensions[0])] for y in range(dimensions[1])]

    def remove(self, index):
        self.grid[index[0]][index[1]] = None

    def add(self, index, object):
        self.grid[index[0]][index[1]] = object


if __name__ == "__main__":
    g = Grid((10, 10))
    print(g.grid)