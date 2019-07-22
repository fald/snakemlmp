from constants import settings

class Block:
    def __init__(self, location, image, visible=True):
        self.grid_x = location[0]
        self.grid_y = location[1]
        self.image = image
        self.visible = visible

    @property
    def grid_location(self):
        return self.grid_x, self.grid_y
    
    @property
    def abs_location(self):
        self.abs_x = self.grid_x * self.image.get_size()[0]
        self.abs_y = self.grid_y * self.image.get_size()[0]
        return self.abs_x, self.abs_y  

    def render(self, onto_window):
        if self.visible:
            onto_window.blit(self.image, self.abs_location)

    def within_bounds(self, grid=settings.PLAY_AREA_DIMENSIONS):
        if (
            self.grid_x not in range(grid[0]) or 
            self.grid_y not in range(grid[1])
            ):
            return False
        return True

    def roll_around(self):
        # Eyy, could probably compress this, but why
        if not self.within_bounds():
            if self.grid_x < 0:
                self.grid_x = grid[0] - 1
            elif self.grid_x > grid[0]:
                self.grid_x = 0

            if self.grid_y < 0:
                self.grid_y = grid[1] - 1
            elif self.grid_y > grid[1]:
                self.grid_y = 0
