import pygame
from constants import settings
from classes.snake import Snake

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

    players = [Snake(speed=body_image.get_size()[0]) for i in range(num_players)]

    return {
        'display': game_display,
        'clock': clock,
        'fonts': fonts,
        'image': body_image,
        'players': players
    }