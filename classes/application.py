from constants import settings
from constants.enums import Directions, GameStates
from classes.snake import Snake
from classes import ai
from data_loaders.initialize_new_game import initialize, new_game
import pygame, time
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display = None
        self._clock = None
        self._fonts = []

        self.players = []
        self.apples = []
        self.game_speed = 0

        self._ai = ai.Defensive()
        self._state = GameStates.MAIN_MENU

    def on_init(self):        
        self._running = True

        init = initialize()
        self._display = init['main_display']
        self._clock = init['clock']
        self._fonts = init['fonts']
        self.game_speed = init['game_speed']

        self.set_state(GameStates.PLAYING)
        self.top_score = 0
        self.new_game()

    def new_game(self):
        # game_vars = new_game(images=self._images, score_board=self._display.components['score'].components['text'])
        new_game(self._display)
        self._state = GameStates.PLAYING
        self._ai.parent = self.players[0]

    def process(self, event):
        if self._state == GameStates.PLAYING:
            if event.type == pygame.KEYDOWN:
                self.players[0].process_input(event.key)
                if event.key == K_ESCAPE:
                    self._running = False

    def set_state(self, state):
        # State of main app window doesn't matter, its render doesn't take it into account.
        # # Ew.
        # for display in self._display.displays:
        #     self._display.displays[display].visible = False

        # if state == GameStates.MAIN_MENU:
        #     self._display.components['main_menu'].visible = True
        # elif state == GameStates.PAUSED:
        #     self._display.components['pause_menu'].visible = True
        # elif state == GameStates.SETTINGS:
        #     self._display.components['game_settings'] = True
        # elif state == GameStates.PLAYING:
        #     for display in ['play_area', 'score', 'ai_settings']:
        #         self._display.components[display].visible = True
        # elif state == GameStates.NEW_GAME:
        #     pass
        # # el
        # if state == GameStates.GAME_OVER:
        #     # self._displays....new_game?
        #     # TODO: Game over.
        #     self.set_state(GameStates.MAIN_MENU)

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
            try:
                # moves = list(self.players[0].controls.values())
                window = self._display.components['play_area']
                self.players[0].set_direction(self._ai.determine_move(window, self.apples)) #, moves))
            except Exception as e:
                print(e)
                print("AI not implemented yet, genius.")

            for event in pygame.event.get():
                self.process(event)

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
                        # Holy fuck.
                        self.top_score = max(self.top_score, self._display.components['score'].components['text'].properties['score'])
                        print(self.top_score)
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
