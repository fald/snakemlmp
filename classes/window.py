from constants.settings import *
from constants.enums import Locations
import pygame

class Window:
    main_window_resolution = RESOLUTION
    window_buffer = WINDOW_BUFFER

    def __init__(
        self, resolution=RESOLUTION, surface=None, color=BACKGROUND,
        image=None, rel_location=Locations.CENTER, components=None, visible=False
        ):
        self.resolution = resolution
        self.color = color
        self.image = image
        self.rel_location = rel_location
        if components is None:
            self.components = []
        else:
            self.components = components
        self.visible = visible
        if surface is None:
            self.surface = pygame.Surface(self.resolution)
        else:
            self.surface = surface

    @property
    def abs_location(self):
        x, y = (
            relative_location * (main_resolution - own_resolution - 2 * Window.window_buffer) + Window.window_buffer
            for 
            relative_location, main_resolution, own_resolution 
            in 
            zip(self.rel_location.value, Window.main_window_resolution, self.resolution)
            # self.rel_location * (main_window_resolution - self.resolution + 2 * window_buffer) - window_buffer
        )
        return x, y

    def add_component(self, component):
        self.components.append(component)

    def render(self, onto_window=None):
        # lol functions don't overload like I'm used to, this'll do for now.
        if onto_window is not None:
            if self.visible:
                self.surface.fill(self.color)
                for component in self.components:
                    if component.visible:
                        component.render(self.surface)
                onto_window.blit(self.surface, self.abs_location)
        else:
            # Main window use only? Assume visible.
            self.surface.fill(self.color)
            for component in self.components:
                if component.visible:
                    component.render(self.surface)
            pygame.display.flip()
