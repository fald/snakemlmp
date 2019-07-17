from constants import settings
from random import randint

class Apple:
    def __init__(self, location, image):
        self.x = location[0]
        self.y = location[1]
        self.image = image

    @property
    def location(self):
        return self.x, self.y

    def render(self, surface):
        surface.blit(self.image, self.location)

    def new_location(self, snakes, area_resolution):
        # TODO: Really should properly implement the grid instead of hacking it forever
        # ...but will I?
        # TODO: Select random from allowable cells instead of this monstrosity where I select
        # random then verify whether or not its allowable >.<
        grid_size = self.image.get_size()[0]
        spot_found = False
        grid_dimensions = int(area_resolution[0] / grid_size), int(area_resolution[1] / grid_size)
        while not spot_found:
            spot = randint(0, grid_dimensions[0] - 1) * grid_size, randint(0, grid_dimensions[1] - 1) * grid_size
            for snake in snakes:
                for segment in snake.snake:
                    if segment == spot:
                        break
                else:
                    spot_found = True
        self.x, self.y = spot

