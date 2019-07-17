from constants import settings
from constants.enums import Directions


class Snake:
    def __init__(self, speed=0.1, step=0, start_length=settings.START_LENGTH, start_location=(0, 0), start_direction=Directions.RIGHT):
        # Location of just the head
        self.x = start_location[0]
        self.y = start_location[1]
        self.step = step
        self.speed = speed
        self.direction = start_direction
        self.controls = {} # Different snakes will have different controls
        self.input_buffer = [] # Just in case >>
        self.snake = [(self.x, self.y)]
        self.increase = start_length - 1
        self.body_image = settings.SNAKE_BODY

    def update(self):
        self.move(self.direction.value)
        self.snake.append(self.location)
        if self.increase == 0:
            self.snake.pop(0)
        else:
            self.increase -= 1

    def render(self, surface, image):
        for i in range(self.length):
            surface.blit(image, self.snake[i])

    @property
    def location(self):
        return self.x, self.y

    @property
    def length(self):
        return len(self.snake)

    def increase_size(self):
        self.increase += 1

    def move(self, direction):
        self.x += self.step * direction[0]
        self.y += self.step * direction[1]
    
    def set_direction(self, direction):
        # No doubling back on yourself, foo'
        not_allowed = {
            Directions.RIGHT: Directions.LEFT,
            Directions.LEFT: Directions.RIGHT,
            Directions.UP: Directions.DOWN,
            Directions.DOWN: Directions.UP
        }

        if not not_allowed[direction] == self.direction:
            self.direction = direction

    # def move_right(self):
    #     self.x += self.speed

    # def move_left(self):
    #     self.x -= self.speed

    # def move_up(self):
    #     self.y -= self.speed

    # def move_down(self):
    #     self.y += self.speed
