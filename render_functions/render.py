import pygame
from constants.settings import BACKGROUND

def refresh(display_surface, image_surface, location, background=BACKGROUND):
    display_surface.fill(background)
    display_surface.blit(image_surface, location)

def render(main_surface, sub_surface, location):
    pass

def render_all(surfaces)