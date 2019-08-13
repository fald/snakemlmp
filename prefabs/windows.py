from classes.window import Window
from classes.grid import Grid
from constants import settings
from constants.enums import Locations
import pygame

play_area_resolution = tuple(
    dimension * settings.BLOCK_SIZE for dimension in settings.PLAY_AREA_DIMENSIONS
)

main_display = Window(
    resolution=settings.RESOLUTION, surface=pygame.display.set_mode(settings.RESOLUTION),
    color=settings.BACKGROUND_MAIN
)

play_area = Grid(rel_location=Locations.TOP_LEFT, visible=True, parent=main_display)
score_board = Window(resolution=settings.SCORE_BOARD_RESOLUTION, visible=True, rel_location=settings.SCORE_BOARD_LOCATION, color=settings.BACKGROUND_SCORE, parent=main_display)
main_menu = Window(resolution=settings.MAIN_MENU_RESOLUTION, color=settings.BACKGROUND_MAIN_MENU, rel_location=settings.MAIN_MENU_LOCATION, parent=main_display)
pause_menu = Window(resolution=settings.PAUSE_MENU_RESOLUTION, color=settings.BACKGROUND_PAUSE_MENU, rel_location=settings.PAUSE_MENU_LOCATION, parent=main_display)
game_settings =  Window(resolution=settings.GAME_SETTINGS_RESOLUTION, color=settings.BACKGROUND_GAME_SETTINGS, rel_location=settings.GAME_SETTINGS_LOCATION, parent=main_display)

main_display.add_displays({
    'play_area': play_area, 
    'score_board': score_board, 
    'main_menu': main_menu, 
    'pause_menu': pause_menu, 
    'game_settings': game_settings
})

# displays = {
#     'play_area': Window(resolution=play_area_resolution, color=settings.BACKGROUND_PLAY_AREA, rel_location=settings.PLAY_AREA_LOCATION),
#     'score': Window(resolution=settings.SCORE_BOARD_RESOLUTION, color=settings.BACKGROUND_SCORE, rel_location=settings.SCORE_BOARD_LOCATION),
#     'ai_settings': Window(resolution=settings.AI_SETTINGS_RESOLUTION, color=settings.BACKGROUND_AI_SETTINGS, rel_location=settings.AI_SETTINGS_LOCATION),
#     'main_menu': Window(resolution=settings.MAIN_MENU_RESOLUTION, color=settings.BACKGROUND_MAIN_MENU, rel_location=settings.MAIN_MENU_LOCATION),
#     'pause_menu': Window(resolution=settings.PAUSE_MENU_RESOLUTION, color=settings.BACKGROUND_PAUSE_MENU, rel_location=settings.PAUSE_MENU_LOCATION),
#     'game_settings': Window(resolution=settings.GAME_SETTINGS_RESOLUTION, color=settings.BACKGROUND_GAME_SETTINGS, rel_location=settings.GAME_SETTINGS_LOCATION),
# }