import constants.settings
from classes.snake import Snake
from data_loaders.initialize_new_game import initialize
from render_functions.render import refresh
import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.players = []
        self._fonts = []
        self._clock = None

    def on_init(self):
        init = initialize()
        self._running = True
        self._display_surf = init['display']
        self._image_surf = init['image']
        self._fonts = init['fonts']
        self._clock = init['clock']
        self.players = init['players']

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        refresh(self._display_surf, self._image_surf, (self.players[0].x, self.players[0].y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        # Clean this up, handle keys separately like in roguelike, and taking into account control schemes,
        # just trying to get a base done right now
        # Also allow buffering on movement keys
        # Also have different handlers for different game states; menus, play, pause
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if keys[K_RIGHT]:
                self.players[0].move_right()
            if keys[K_LEFT]:
                self.players[0].move_left()
            if keys[K_UP]:
                self.players[0].move_up()
            if keys[K_DOWN]:
                self.players[0].move_down()
            
            if keys[K_ESCAPE]:
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()
