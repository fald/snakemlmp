import pygame
from constants import settings
from constants.enums import Locations
from classes.snake import Snake
from classes.apple import Apple
from classes.grid import Grid
from classes.window import Window
from random import randint
from prefabs import snakes, windows, fonts

# TODO: Only accounts for 1 or 2 players right now, might need a change later.
def new_game(main_display, num_players=settings.NUM_PLAYERS, num_apples=1):
    snake_list = [snakes.player_1_snake] # lol named same as module before >.> 
    if num_players > 1:
        snake_list.append(snakes.player_2_snake)

    apples = [Apple(parent=main_display.get_display('play_area') for apple in num_apples]

    game_speed = settings.START_GAME_SPEED

    return {
        'players': snake_list,
        'apples': apples,
        'game_speed': game_speed
    }

def initialize():
    pygame.init()

    fonts = fonts.fonts
    main_display = windows.main_display
    clock = pygame.time.Clock()

    pygame.display.set_caption(settings.WINDOW_TITLE)
    
    if settings.WINDOW_ICON:
        icon_image = pygame.image.load(settings.WINDOW_ICON).convert()
        pygame.display.set_icon(icon_image)
    else:
        icon_image = None

    return {
        'main_display': main_display,
        'clock': clock,
        'fonts': fonts
    }
    # Snakes in new_game, hurf.
