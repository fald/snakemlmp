from constants import settings
from constants.enums import Directions
from classes.snake import Snake
from data_loaders.initialize_new_game import initialize
from render_functions.render import refresh
import pygame, time
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.players = []
        self._fonts = []
        self._clock = None
        self.game_speed = 0

    def on_init(self):
        init = initialize()
        self._running = True
        self._main_surf = init['main_display']
        self._game_surf = init['game_display']
        self._score_surf = init['score_display']
        self._fonts = init['fonts']
        self._clock = init['clock']
        self.players = init['players']
        self.game_speed = init['game_speed']
        self.apples = init['apples']

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        # refresh(self._display_surf, self._image_surf, self.players[0].location)
        self._main_surf.fill(Color(50, 50, 50))
        self._game_surf.fill(settings.BACKGROUND)
        self._score_surf.fill(settings.BACKGROUND)
        for apple in self.apples:
            apple.render(self._game_surf)
        for player in self.players:
            player.render(self._game_surf)
        self._main_surf.blit(self._game_surf, (0, 0))
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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RIGHT:
                        self.players[0].set_direction(Directions.RIGHT)
                    elif event.key == K_LEFT:
                        self.players[0].set_direction(Directions.LEFT)
                    elif event.key == K_UP:
                        self.players[0].set_direction(Directions.UP)
                    elif event.key == K_DOWN:
                        self.players[0].set_direction(Directions.DOWN)
                    elif event.key == K_ESCAPE:
                        self._running = False
            # keys = pygame.key.get_pressed()
            # if keys[K_RIGHT]:
            # #     self.players[0].move_right()
            #     self.players[0].set_direction(Directions.RIGHT)
            # if keys[K_LEFT]:
            # #     self.players[0].move_left()
            #     self.players[0].set_direction(Directions.LEFT)
            # if keys[K_UP]:
            # #     self.players[0].move_up()
            #     self.players[0].set_direction(Directions.UP)
            # if keys[K_DOWN]:
            # #     self.players[0].move_down()
            #     self.players[0].set_direction(Directions.DOWN)
            # if keys[K_ESCAPE]:
            #     self._running = False

            for player in self.players:
                player.update()
                for apple in self.apples:
                    if player.grid_location == apple.grid_location:
                        apple.new_location(self.players)
                        player.increase_size()

            self.on_loop()
            self.on_render()

            self._clock.tick(self.game_speed)
            # self.game_speed += 1
            # time.sleep(100.0 / 1000.0)

        self.on_cleanup()
