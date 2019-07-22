from constants.settings import *
from constants.enums import Locations
import pygame

class Window:
    main_window_resolution = RESOLUTION
    window_buffer = WINDOW_BUFFER

    def __init__(
        self, resolution=RESOLUTION, surface=None, color=BACKGROUND,
        image=None, rel_location=Locations.CENTER, components=[], visible=True
        ):
        self.resolution = resolution
        self.color = color
        self.image = image
        self.rel_location = rel_location
        self.components = components
        self.visible = visible
        if surface is None:
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

    def render(self, onto_window):
        if self.visible:
            self.surface.fill(self.color)
            for component in self.components:
                if component.visible:
                    component.render(self.surface)
            onto_window.blit(self.surface, self.abs_location)

    def render(self):
        # Main window use only? Assume visible.
        self.surface.fill(self.color)
        for component in self.components:
            if component.visible:
                component.render(self.surface)
        pygame.display.flip()
