from random import choice
from classes.block import Block
from constants import settings


class Apple(Block):
    def new_location(self, snakes):
        candidate_locations = []
        for i in range(settings.PLAY_AREA_DIMENSIONS[0]):
            for j in range(settings.PLAY_AREA_DIMENSIONS[1]):
                candidate_locations.append((i, j))
        for snake in snakes:
            for segment in snake.body:
                if segment in candidate_locations: # Just for while the snake can go out of bounds
                    candidate_locations.remove(segment)
            candidate_locations.remove(snake.grid_location)
        self.grid_x, self.grid_y = choice(candidate_locations)

# class Apple:
#     def __init__(self, location, image):
#         self.x = location[0]
#         self.y = location[1]
#         self.image = image

#     @property
#     def location(self):
#         return self.x, self.y

#     def render(self, surface):
#         surface.blit(self.image, self.location)

#     def new_location(self, snakes, area_resolution):
#         # TODO: Really should properly implement the grid instead of hacking it forever
#         # ...but will I?
#         # TODO: Select random from allowable cells instead of this monstrosity where I select
#         # random then verify whether or not its allowable >.<
#         grid_size = self.image.get_size()[0]
#         spot_found = False
#         grid_dimensions = int(area_resolution[0] / grid_size), int(area_resolution[1] / grid_size)
#         while not spot_found:
#             spot = randint(0, grid_dimensions[0] - 1) * grid_size, randint(0, grid_dimensions[1] - 1) * grid_size
#             for snake in snakes:
#                 for segment in snake.snake:
#                     if segment == spot:
#                         break
#                 else:
#                     spot_found = True
        # self.x, self.y = spot

