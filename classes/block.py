from constants import settings
import pygame

class Block:
    def __init__(self, location, image, visible=True, parent=None):
        self.grid_x = location[0]
        self.grid_y = location[1]
        self.visible = visible
        self.parent = parent
        self.image = pygame.image.load(image).convert()


    @property
    def grid_location(self):
        return self.grid_x, self.grid_y
    
    @property
    def abs_location(self):
        self.abs_x = self.grid_x * self.image.get_size()[0]
        self.abs_y = self.grid_y * self.image.get_size()[0]
        return self.abs_x, self.abs_y  

    def render(self):
        if self.visible:
            self.parent.blit(self.image, self.abs_location)

    def within_bounds(self):
        grid = self.parent.dimensions
        if (
            self.grid_x not in range(grid[0]) or 
            self.grid_y not in range(grid[1])
            ):
            return False
        return True
