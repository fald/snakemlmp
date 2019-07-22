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
        self._displays = []
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
        self._displays = init['displays']
        self._clock = init['clock']
        self._fonts = init['fonts']
        self._images = init['images']

        self.set_state(GameStates.PLAYING)

        #
        #
        # To be removed and put elsewhere.
        #
        #
        game_vars = new_game(images=self._images)
        self.players = game_vars['players']
        self.apples = game_vars['apples']
        self.game_speed = game_vars['game_speed']
        self._displays['play_area'].components = [self.players[0], self.apples[0]]
        
    def set_state(self, state):
        # State of main app window doesn't matter, its render doesn't take it into account.
        for display in self._displays:
            self._displays[display].visible = False

        if state == GameStates.MAIN_MENU:
            self._displays['main_menu'].visible = True
        elif state == GameStates.PAUSED:
            self._displays['pause_menu'].visible = True
        elif state == GameStates.SETTINGS:
            self._displays['game_settings'] = True
        elif state == GameStates.PLAYING:
            for display in ['play_area', 'score', 'ai_settings']:
                self._displays[display].visible = True
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
        self._displays['main'].render()

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
