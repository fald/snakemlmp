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

def get_abs_location(main_surface, sub_surface, location, buffer=WINDOW_BUFFER):
    # Fucking gross.
    # TODO: Find more elegant way to do this :/
    x_pos = 0
    y_ pos = 0
    size_x, size_y = main_surface.get_size()
    sub_x, sub_y = sub_surface.get_size()
    if location[0] == 0:
        x_pos = WINDOW_BUFFER
    elif location[0] == 0.5:
        x_pos = int(size_x / 2) - int(sub_x / 2)
    elif location[0] == 1:
        x_pos = size_x - sub_x - WINDOW_BUFFER

    if location[1] == 0:
        y_pos = WINDOW_BUFFER
    elif location[1] == 0.5:
        y_pos = int(size_y / 2) - int(sub_y / 2)
    elif location[1] == 1:
        y_pos = size_y - sub_y - WINDOW_BUFFER

    return x_pos, y_pos
    