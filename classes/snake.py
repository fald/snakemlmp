from constants import settings
from constants.enums import Directions, MoveRules
from pygame.locals import *
from classes.block import Block


class Snake(Block):
    default_controls = {
        K_s: Directions.DOWN,
        K_w: Directions.UP,
        K_a: Directions.LEFT,
        K_d: Directions.RIGHT
    }

    def __init__(
        self, start_length=settings.START_LENGTH, 
        head_image=settings.SNAKE_HEAD_IMAGE,
        body_image=settings.SNAKE_BODY_IMAGE, 
        start_direction=Directions.RIGHT, 
        start_location=(0, 0), components=None,
        parent=None, move_rule=MoveRules.WRAP_AROUND
        ):
        super(Snake, self).__init__(start_location, head_image, parent=parent)
        self.direction = start_direction
        self.input_buffer = []
        self.body = []
        self.increase = start_length - 1
        self.body_image = body_image
        self.score = 1 - start_length
        self.parent = parent
        self.move_rule = move_rule # Not settings, can be different between snakes with powerups and such
        # self.move_rule = MoveRules.STANDARD
        if components is None:
            self.components = {'controls': Snake.default_controls,  'ai': None}
        else:
            self.components = components

    def update(self):
        if len(self.input_buffer) > 0:
            self.direction = self.input_buffer.pop(0)
        self.move(self.direction)
        if self.increase > 0:
            self.increase_score()
        else:
            self.body.pop(0)

    def render(self):
        for segment in self.body:
            segment.render()
        super(Snake, self).render()

    @property
    def length(self):
        return len(self.body) + 1

    def increase_size(self):
        self.increase += 1

    def increase_score(self):
        # Probably a better way to do this?
        self.score += 1
        self.increase -= 1
        # Asking the grid to ask the scoreboard to update, since the scoreboard is elsewhere.
        # Don't really want the grid to update score every frame, seems wasteful, so this won't be in the grid's update.
        self.parent.upate_score()
        # self.score_board.update({'draw_text': "Score: {0}".forma11t(self.score), 'score': self.score})
        # score_board.set_property({'score': self.score})

    def move(self, direction):
        # Grid updates itself and snake together.
        self.body.append(Block(self.grid_location, self.body_image))
        # self.parent.update_grid()
        if self.move_rule == MoveRules.WRAP_AROUND:
            self.grid_x = (self.grid_x + direction[0]) % grid_dimensions[0]
            self.grid_y = (self.grid_y + direction[1]) % grid_dimensions[1]
        else: # separated so you can crash
            self.grid_x += direction[0]
            self.grid_y += direction[1]

    def set_direction(self, direction):
        # No doubling back on yourself, foo'
        not_allowed = {
            Directions.RIGHT: Directions.LEFT,
            Directions.LEFT: Directions.RIGHT,
            Directions.UP: Directions.DOWN,
            Directions.DOWN: Directions.UP
        }

        if not not_allowed[direction] == self.direction:
            self.input_buffer.append(direction)

    def process_input(self, input):
        try:
            self.set_direction(self.controls[input])
        except KeyError:
            pass
