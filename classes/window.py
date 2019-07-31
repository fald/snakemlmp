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
            texts = self.components['text']
            for text in texts:
                text_surface = text['font'].render(text['text'], False, text['color'])
                self.blit(text_surface, text['location'])
        except KeyError:
            pass

    def blit(self, source, location=None):
        # Don't wanna bother with location if its a sub-window, but text becomes trickier.
        location = source.abs_location if location is None else location
        try:
            self.surface.blit(source.surface, location)
        except:
            pass

    def render(self):
        if self.color is not None and self.visible:
            self.surface.fill(self.color)
            # Render sub-windows
            try:
                for window in self.components.get('windows'):
                    if window.visible:
                        window.render()
            except TypeError:
                pass
            # Render on-window stuff like grids/snakes whatever

            # Render text
            self.render_text()

        # Blit onto main window or if main window, update main display
        if self.parent is None:
            # Then we're the main window
            pygame.display.flip()
        else:
            self.parent.blit(self)
