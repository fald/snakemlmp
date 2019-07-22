from constants.settings import *
from constants.enums import Locations
import pygame

class Window:
    main_window_resolution = RESOLUTION
    window_buffer = WINDOW_BUFFER

    def __init__(
        self, resolution=RESOLUTION, surface=None, color=BACKGROUND,
        image=None, rel_location=Locations.CENTER
        ):
        self.resolution = resolution
        self.color = color
        self.image = image
        self.rel_location = rel_location

        self.surface = pygame.Surface(self.resolution)

    @property
    def abs_location(self):
        x, y = (
            relative_location * (main_resolution - own_resolution + 2 * Window.window_buffer) - Window.window_buffer
            for 
            relative_location, main_resolution, own_resolution 
            in 
            zip(self.rel_location, Window.main_window_resolution, self.resolution)
            # self.rel_location * (main_window_resolution - self.resolution + 2 * window_buffer) - window_buffer
        )
        return x, y
