from random import choice
from classes.block import Block
from constants import settings


class Apple(Block):
    def __init__(self, image=settings.APPLE_IMAGE, location=None, visible=True, parent=None):
        location = (-1, -1) if location is None else location
        super(Apple, self).__init__(location, image, visible, parent)
        self.new_location()

    def new_location(self):
        occupied = self.parent.is_occupied()
        candidate_locations = []
        for i in len(occupied[0]):
            for j in len(occupied[1]):
                if occupied[i][j]:
                    candidate_locations.append((i, j))
        self.grid_x, self.grid_y = choice(candidate_locations)


