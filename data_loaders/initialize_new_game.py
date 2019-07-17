import pygame
from constants import settings
from classes.snake import Snake
from classes.apple import Apple
from classes.grid import Grid
from random import randint

def initialize():
    # TODO: Add sanity checks?
    pygame.init()

    main_display = pygame.display.set_mode(settings.RESOLUTION)
    game_display = pygame.Surface((
        settings.PLAY_AREA_DIMENSIONS[0] * settings.BLOCK_SIZE,
        settings.PLAY_AREA_DIMENSIONS[1] * settings.BLOCK_SIZE))
    # game_grid = Grid(settings.PLAY_AREA_DIMENSIONS)
    score_display = pygame.Surface(settings.SCORE_BOARD_RESOLUTION)

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
    
    snake_body_image = pygame.image.load(settings.SNAKE_BODY_IMAGE).convert()
    snake_head_image = pygame.image.load(settings.SNAKE_HEAD_IMAGE).convert()
    apple_image = pygame.image.load(settings.APPLE_IMAGE).convert()

    players = [Snake(head_image=snake_head_image, body_image=snake_body_image) for i in range(settings.NUM_PLAYERS)]
    apples = [Apple((-1, -1), apple_image)]
    for apple in apples:
        apple.new_location(players)

    game_speed = settings.START_GAME_SPEED

    # # Don't mind this ugly mess, just playing around 
    # grid_x, grid_y = (int(x / apple_image.get_size()[0]) for x in settings.RESOLUTION)
    # first_apple_location = randint(0, grid_x) * apple_image.get_size()[0], randint(0, grid_y) * apple_image.get_size()[1]
    # first_apple = Apple(location=first_apple_location, image=apple_image)
    # first_apple.new_location(players, settings.RESOLUTION)
    # apples = [first_apple]


    return {
        'main_display': main_display,
        'game_display': game_display,
        'score_display': score_display,
        'clock': clock,
        'fonts': fonts,
        'players': players,
        'game_speed': game_speed,
        'apples': apples
    }