import pygame
from constants import settings
from constants.enums import Locations
from classes.snake import Snake
from classes.apple import Apple
from classes.grid import Grid
from classes.window import Window
from random import randint
from prefabs import snakes, windows, fonts

def new_game(images, score_board, num_players=settings.NUM_PLAYERS, num_apples=1):
    players = [Snake(head_image=images['snake_head'], body_image=images['snake_body'], score_board=score_board) for i in range(num_players)]
    apples = [Apple((-1, -1), images['apple']) for i in range(num_apples)]
    for apple in apples:
        apple.new_location(players)
    game_speed = settings.START_GAME_SPEED


    score_board.update({'draw_text': "Score: {0}".format(players[0].score)})
    score_board.render_text()

    return {
        'players': players,
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
        
    images = {
        'snake_body': pygame.image.load(settings.SNAKE_BODY_IMAGE).convert(),
        'snake_head': pygame.image.load(settings.SNAKE_HEAD_IMAGE).convert(),
        'apple': pygame.image.load(settings.APPLE_IMAGE).convert()
    }

    return {
        'display': main_display,
        'clock': clock,
        'fonts': fonts,
        'images': images
    }
    # Snakes in new_game, hurf.
