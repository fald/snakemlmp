from random import choice
from classes.block import Block
from constants import settings


class Apple(Block):
    def __init__(self, image, location=None, visible=True, parent=None):
        super(Apple, self).__init__(location, image, visible, parent)
        self.location = self.new_location(self.parent)

    def new_location(self):
        candidate_locations = []
        for i in range(self.parent.dimensions[0]):
            for j in range(self.parent.dimensions[1]):
                candidate_locations.append((i, j))
        for snake in self.parent.components['snakes']:
            for segment in snake.body:
                if segment.grid_location in candidate_locations: # Just for while the snake can go out of bounds
                    candidate_locations.remove(segment.grid_location)
            candidate_locations.remove(snake.grid_location)
        self.grid_x, self.grid_y = choice(candidate_locations)

