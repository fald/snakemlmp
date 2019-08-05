from random import choice
from classes.block import Block
from constants import settings


class Apple(Block):
    def __init__(self, image=settings.APPLE_IMAGE, location=None, visible=True, parent=None):
        super(Apple, self).__init__(location, image, visible, parent)
        self.new_location()

    def new_location(self):
        # candidate_locations = []
        # for i in range(self.parent.dimensions[0]):
        #     for j in range(self.parent.dimensions[1]):
        #         candidate_locations.append((i, j))
        # for snake in self.parent.components['snakes']:
        #     for segment in snake.body:
        #         if segment.grid_location in candidate_locations: # Just for while the snake can go out of bounds
        #             candidate_locations.remove(segment.grid_location)
        #     candidate_locations.remove(snake.grid_location)
        # self.grid_x, self.grid_y = choice(candidate_locations)

        occupied = self.parent.is_occupied()
        candidate_locations = []
        for i in len(occupied[0]):
            for j in len(occupied[1]):
                if occupied[i][j]:
                    candidate_locations.append((i, j))
        self.grid_x, self.grid_y = choice(candidate_locations)


