from constants import settings
from constants.enums import Directions, MoveRules
from pygame.locals import *
from classes.block import Block


class Snake(Block):
    def __init__(
        self, start_length=settings.START_LENGTH, head_image=settings.SNAKE_HEAD_IMAGE,
        body_image=settings.SNAKE_BODY_IMAGE, start_direction=Directions.RIGHT, start_location=(0, 0),
        score_board=None
        ):
        super(Snake, self).__init__(start_location, head_image)
        self.direction = start_direction
        self.controls = {
            K_DOWN: Directions.DOWN,
            K_UP: Directions.UP,
            K_LEFT: Directions.LEFT,
            K_RIGHT: Directions.RIGHT
        } # Different snakes will have different controls
        self.input_buffer = []
        self.body = []
        self.increase = start_length - 1
        self.body_image = body_image
        self.score = 1 - start_length
        self.score_board = score_board
        self.parent = None
        self.move_rule = MoveRules.WRAP_AROUND
        # self.move_rule = MoveRules.STANDARD

    def update(self):
        if len(self.input_buffer) > 0:
            self.direction = self.input_buffer.pop(0)
        self.body.append(Block(self.grid_location, self.body_image))
        self.move(self.direction.value)
        if self.increase > 0:
            self.increase -= 1
            self.increase_score()
        else:
            self.body.pop(0)
        # self.move(self.direction.value)
        # self.snake.append(self.location)
        # if self.increase == 0:
        #     self.snake.pop(0)
        # else:
        #     self.increase -= 1

    def render(self, onto_window):
        for segment in self.body:
            segment.render(onto_window)
        super(Snake, self).render(onto_window)

    @property
    def length(self):
        return len(self.body) + 1

    def increase_size(self):
        self.increase += 1

    def increase_score(self):
        # Probably a better way to do this?
        self.score += 1
        self.score_board.update({'draw_text': "Score: {0}".format(self.score), 'score': self.score})
        # score_board.set_property({'score': self.score})

    def move(self, direction, grid_dimensions=settings.PLAY_AREA_DIMENSIONS):
        if self.move_rule == MoveRules.WRAP_AROUND:
            self.grid_x = (self.grid_x + direction[0]) % grid_dimensions[0]
            self.grid_y = (self.grid_y + direction[1]) % grid_dimensions[1]
        else:
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
