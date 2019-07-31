from constants.settings import *
from constants.enums import Locations
import pygame


# Components:
#   windows -> sub-windows
#   text    -> Dict of text, font, color and location
#   grid    -> grid system in place to hold snakes, apples

class Window:
    def __init__(
        self, resolution=RESOLUTION, surface=None, 
        color=BACKGROUND, image=None, rel_location=Locations.CENTER, 
        components=None, visible=False, properties=None,
        parent=None
        ):
        self.resolution = resolution
        self.surface = surface if surface is not None else pygame.Surface(self.resolution)
        self.color = color
        self.image = image
        self.rel_location = rel_location
        self.components = components if components is not None else {}
        self.visible = visible
        self.parent = parent

    @property
    def abs_location(self):
        if self.parent is not None:
            x, y = (
                relative_location * (main_resolution - own_resolution - 2 * WINDOW_BUFFER) + WINDOW_BUFFER
                for 
                relative_location, main_resolution, own_resolution 
                in 
                zip(self.rel_location.value, self.parent.resolution, self.resolution)
            )
            return x, y        
        else:
            return 0, 0

    def update(self, component):
        self.components.update(component)

    def render_text(self):
        try:
            texts = self.properties['text']
            for text in texts:
                text_surface = text['font'].render(text['text'], False, text['color'])
                self.blit(text_surface, text['location'])
        except KeyError:
            pass

    def blit(self, source, destination):
        try:
            self.surface.blit(source, destination)
        except:
            pass

    def render(self):
        if self.color is not None and self.visible:
            self.surface.fill(self.color)
            for window in self.components.get('windows'):
                if window.visible:
                    window.render()
        if self.parent is None:
            # Then we're the main window and thus always visible.
        else:
            # Then we're a sub window and need to check visibility!
            # Or just make sure base window is always visible.

        if onto_window is not None:
            if self.visible:
                for component in self.components:
                    # hasattr(self.components[component], 'visible') and 
                    if self.components[component].visible:
                        self.components[component].render(self.surface)
                onto_window.blit(self.surface, self.abs_location)
        else:
            for component in self.components:
                if self.components[component].visible:
                    self.components[component].render(self.surface)
            pygame.display.flip()
