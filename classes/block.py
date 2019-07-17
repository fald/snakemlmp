from constants import settings

class Block:
    def __init__(self, location, image):
        self.grid_x = location[0]
        self.grid_y = location[1]
        self.image = image

    @property
    def grid_location(self):
        return self.grid_x, self.grid_y
    
    @property
    def abs_location(self):
        self.abs_x = self.grid_x * self.image.get_size()[0]
        self.abs_y = self.grid_y * self.image.get_size()[0]
        return self.abs_x, self.abs_y  

    def render(self, onto_window):
        onto_window.blit(self.image, self.abs_location)
