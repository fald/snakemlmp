from constants.settings import *
from constants.enums import Locations
import pygame

class Window:
    main_window_resolution = RESOLUTION

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
        # Fucking gross.
        # TODO: Find more elegant way to do this :/
        x, y = 0, 0
        size_x, size_y = main_surface.get_size()    # main_window_resolution
        sub_x, sub_y = sub_surface.get_size()       # self.resolution
        location = self.rel_location                #
        if location[0] == 0:
            x_pos = WINDOW_BUFFER
        elif location[0] == 0.5:
            x_pos = int(size_x / 2) - int(sub_x / 2)
        elif location[0] == 1:
            x_pos = size_x - sub_x - WINDOW_BUFFER

            # pattern:
            #   pos = size*loc - sub*loc - window_buffer * (-1, 0, 1)
            #
            #
            #
            #

        if location[1] == 0:
            y_pos = WINDOW_BUFFER
        elif location[1] == 0.5:
            y_pos = int(size_y / 2) - int(sub_y / 2)
        elif location[1] == 1:
            y_pos = size_y - sub_y - WINDOW_BUFFER

        return x_pos, y_pos