from constants import settings
from constants.enums import Directions, GameStates
from classes.snake import Snake
from data_loaders.initialize_new_game import initialize, new_game
from render_functions.render import refresh
import pygame, time
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        # self._displays = {}
        self._display = None
        self._clock = None
        self._fonts = []
        self._images = []

        self.players = []
        self.apples = []
        self.game_speed = 0

        self._state = GameStates.MAIN_MENU

    def on_init(self):
        init = initialize()
        self._running = True
        # self._displays = init['displays']
        self._display = init['display']
        self._clock = init['clock']
        self._fonts = init['fonts']
        self._images = init['images']

        self.set_state(GameStates.PLAYING)

        self.new_game()
        #
        #
        # To be removed and put elsewhere, on_newgame?
        #
        #
        # Fucking gross tbh
        # game_vars = new_game(images=self._images, score_board=self._display.components['score'].components['text'])
        # self.players = game_vars['players']
        # self.apples = game_vars['apples']
        # self.game_speed = game_vars['game_speed']
        # self._display.components['play_area'].components = {'players': self.players[0], 'apples': self.apples[0]}

    def new_game(self):
        game_vars = new_game(images=self._images, score_board=self._display.components['score'].components['text'])
        self.players = game_vars['players']
        self.apples = game_vars['apples']
        self.game_speed = game_vars['game_speed']
        self._display.components['play_area'].components = {'players': self.players[0], 'apples': self.apples[0]}
        self._state = GameStates.PLAYING

    def process(self, event):
        if self._state == GameStates.PLAYING:
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


    def set_state(self, state):
        # State of main app window doesn't matter, its render doesn't take it into account.
        # Ew.
        for display in self._display.components:
            # self._displays[display].visible = False
            self._display.components[display].visible = False

        if state == GameStates.MAIN_MENU:
            # self._displays['main_menu'].visible = True
            self._display.components['main_menu'].visible = True
        elif state == GameStates.PAUSED:
            self._display.components['pause_menu'].visible = True
        elif state == GameStates.SETTINGS:
            self._display.components['game_settings'] = True
        elif state == GameStates.PLAYING:
            for display in ['play_area', 'score', 'ai_settings']:
                self._display.components[display].visible = True
        elif state == GameStates.NEW_GAME:
            pass
        elif state == GameStates.GAME_OVER:
            # self._displays....new_game?
            # TODO: Game over.
            self.set_state(GameStates.MAIN_MENU)

        self.state = state

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        # ew
        self._display.render()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            pygame.event.pump()
            for event in pygame.event.get():
                self.process(event)
                # if event.type == pygame.KEYDOWN:
                #     if event.key == K_RIGHT:
                #         self.players[0].set_direction(Directions.RIGHT)
                #     elif event.key == K_LEFT:
                #         self.players[0].set_direction(Directions.LEFT)
                #     elif event.key == K_UP:
                #         self.players[0].set_direction(Directions.UP)
                #     elif event.key == K_DOWN:
                #         self.players[0].set_direction(Directions.DOWN)
                #     elif event.key == K_ESCAPE:
                #         self._running = False

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
                        # self.on_init()
                        self.new_game()
                        # self._running = False
                # Out-of-bounds kill
                if not player.within_bounds():
                    # self.on_init()
                    self.new_game()
                    # self._running = False

            self.on_loop()
            self.on_render()
            # self._display.components['score'].render(self._display.surface)

            self._clock.tick(self.game_speed)
            # self.game_speed += 1
            # time.sleep(100.0 / 1000.0)

        self.on_cleanup()
