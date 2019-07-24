import pygame
from constants import settings
from constants.enums import Locations
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

    fonts = [
        pygame.font.SysFont(settings.FONT, settings.FONT_SMALL, settings.FONT_BOLD),
        pygame.font.SysFont(settings.FONT, settings.FONT_MEDIUM, settings.FONT_BOLD),
        pygame.font.SysFont(settings.FONT, settings.FONT_LARGE, settings.FONT_BOLD),
    ]

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

    main_display = Window(
        resolution=settings.RESOLUTION, surface=pygame.display.set_mode(settings.RESOLUTION), 
        color=settings.BACKGROUND_MAIN, components=displays
        )

    # main_components = list(displays.values())
    # displays['main'].add_components(main_components)

    # Ew
    # main_display.components['score'].surface = fonts[1].render("Eat shit and/or die, please.", True, (255, 0, 0))

    # Can't get it to work making the main score display have this surface, and I have no idea why!
    score_display = Window(
        surface=fonts[1].render("Score: 0", False, (255, 0, 0)), 
        visible=True, resolution=(100, 100), 
        color=None, rel_location=Locations.TOP_LEFT,
        components={'draw_text': [0]}
        )
    displays['score'].add_component({'text': score_display})

    pygame.display.set_caption(settings.WINDOW_TITLE)
    
    clock = pygame.time.Clock()
    
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
        'display': main_display,
        # 'displays': displays,
        'clock': clock,
        'fonts': fonts,
        'images': images
    }