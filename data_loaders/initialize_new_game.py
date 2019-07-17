import pygame
from constants import settings
from classes.snake import Snake
from classes.apple import Apple
from random import randint

def initialize(num_players=1):
    pygame.init()
    game_display = pygame.display.set_mode(settings.RESOLUTION)
    pygame.display.set_caption(settings.WINDOW_TITLE)
    clock = pygame.time.Clock()
    fonts = [
        pygame.font.SysFont(settings.FONT, settings.FONT_SMALL, settings.FONT_BOLD),
        pygame.font.SysFont(settings.FONT, settings.FONT_MEDIUM, settings.FONT_BOLD),
        pygame.font.SysFont(settings.FONT, settings.FONT_LARGE, settings.FONT_BOLD),
    ]
    if settings.WINDOW_ICON:
        icon_image = pygame.image.load(settings.WINDOW_ICON).convert()
        pygame.display.set_icon(icon_image)
    else:
        icon_image = None
    body_image = pygame.image.load(settings.SNAKE_BODY).convert()

    players = [Snake(step=body_image.get_size()[0]) for i in range(num_players)]

    game_speed = 15

    # Don't mind this ugly mess, just playing around 
    apple_image = pygame.image.load(settings.APPLE_IMAGE)
    grid_x, grid_y = (int(x / apple_image.get_size()[0]) for x in settings.RESOLUTION)
    first_apple_location = randint(0, grid_x) * apple_image.get_size()[0], randint(0, grid_y) * apple_image.get_size()[1]
    first_apple = Apple(location=first_apple_location, image=apple_image)
    first_apple.new_location(players, settings.RESOLUTION)
    apples = [first_apple]


    return {
        'display': game_display,
        'clock': clock,
        'fonts': fonts,
        'image': body_image,
        'players': players,
        'game_speed': game_speed,
        'apples': apples
    }