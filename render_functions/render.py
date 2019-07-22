import pygame
from constants.settings import BACKGROUND, WINDOW_BUFFER

def refresh(display_surface, image_surface, location, background=BACKGROUND):
    display_surface.fill(background)
    display_surface.blit(image_surface, location)

def render(main_surface, sub_surface, location, background):
    # Doesn't refresh the main display, that's for render_all
    # main_surface.fill(background)
    abs_location = get_abs_location(main_surface, sub_surface, location)
    main_surface.blit(sub_surface, abs_location)

def render_all(surfaces):
    pass


    