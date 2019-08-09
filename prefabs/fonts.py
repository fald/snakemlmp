import pygame
from constants import settings

pygame.font.init()

fonts = [
    pygame.font.SysFont(settings.FONT, settings.FONT_SMALL, settings.FONT_BOLD),
    pygame.font.SysFont(settings.FONT, settings.FONT_MEDIUM, settings.FONT_BOLD),
    pygame.font.SysFont(settings.FONT, settings.FONT_LARGE, settings.FONT_BOLD),
]
