from constants import settings
from constants.enums import Directions
from classes.snake import Snake
from data_loaders.initialize_new_game import initialize, new_game
from render_functions.render import refresh
import pygame, time
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._displays = []
        self._clock = None
        self._fonts = []
        self._images = []
        self._surfaces_to_render = []

        self.players = []
        self.apples = []
        self.game_speed = 0

    def on_init(self):
        init = initialize()
        self._running = True
        self._displays = init['displays']
        self._clock = init['clock']
        self._fonts = init['fonts']
        self._images = init['images']
        self._surfaces_to_render = [
            self._surfaces['main'],
            self._surfaces['main_menu']
            ]

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._main_surf.fill(settings.WINDOW_BACKGROUND)
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

            for player in self.players:
                player.update()
                for apple in self.apples:
                    if player.grid_location == apple.grid_location:
                        apple.new_location(self.players)
                        player.increase_size()
                # Self-collision
                # # Just doing it for 1 snake right now, fix later. 
                for segment in player.body:
                    if player.grid_location == segment.grid_location:
                        print("Game over, loser.")
                        self._running = False
                # Out-of-bounds kill
                if not player.within_bounds():
                    print("Watch out, loser.")
                    self._running = False

            self.on_loop()
            self.on_render()

            self._clock.tick(self.game_speed)
            # self.game_speed += 1
            # time.sleep(100.0 / 1000.0)

        self.on_cleanup()
