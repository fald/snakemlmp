import pygame
from constants import settings
from classes.snake import Snake
from classes.apple import Apple
from classes.grid import Grid
from classes.window import Window
from random import randint

def new_game(images, num_players=settings.NUM_PLAYERS, num_apples=1):
    players = [Snake(head_image=images['snake_head'], body_image=images['snake_body']) for i in range(num_players)]
    apples = [Apple((-1, -1), images['apple']) for i in range(num_apples)]
    for apple in apples:
        apple.new_location(players)
    game_speed = settings.START_GAME_SPEED

    return {
        'players': players,
        'apples': apples,
        'game_speed': game_speed
    }

def initialize():
    pygame.init()

    play_area_resolution = tuple(
        dimension * settings.BLOCK_SIZE for dimension in settings.PLAY_AREA_DIMENSIONS
    )

    displays = {
        # Main be separate in the application class?
        # 'main': Window(resolution=settings.RESOLUTION, surface=pygame.display.set_mode(settings.RESOLUTION), color=settings.BACKGROUND_MAIN),
        'play_area': Window(resolution=play_area_resolution, color=settings.BACKGROUND_PLAY_AREA, rel_location=settings.PLAY_AREA_LOCATION),
        'score': Window(resolution=settings.SCORE_BOARD_RESOLUTION, color=settings.BACKGROUND_SCORE, rel_location=settings.SCORE_BOARD_LOCATION),
        'ai_settings': Window(resolution=settings.AI_SETTINGS_RESOLUTION, color=settings.BACKGROUND_AI_SETTINGS, rel_location=settings.AI_SETTINGS_LOCATION),
        'main_menu': Window(resolution=settings.MAIN_MENU_RESOLUTION, color=settings.BACKGROUND_MAIN_MENU, rel_location=settings.MAIN_MENU_LOCATION),
        'pause_menu': Window(resolution=settings.PAUSE_MENU_RESOLUTION, color=settings.BACKGROUND_PAUSE_MENU, rel_location=settings.PAUSE_MENU_LOCATION),
        'game_settings': Window(resolution=settings.GAME_SETTINGS_RESOLUTION, color=settings.BACKGROUND_GAME_SETTINGS, rel_location=settings.GAME_SETTINGS_LOCATION),
    }

    components = list(displays.values())
    main = Window(resolution=settings.RESOLUTION, surface=pygame.display.set_mode(settings.RESOLUTION), color=settings.BACKGROUND_MAIN, components=components)

    displays['main'] = main

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
    
    images = {
        'snake_body': pygame.image.load(settings.SNAKE_BODY_IMAGE).convert(),
        'snake_head': pygame.image.load(settings.SNAKE_HEAD_IMAGE).convert(),
        'apple': pygame.image.load(settings.APPLE_IMAGE).convert()
    }
    
    return {
        'displays': displays,
        'clock': clock,
        'fonts': fonts,
        'images': images
    }