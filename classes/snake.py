from constants import settings
from constants.enums import Directions


class Snake:
    def __init__(self, speed=10, start_length=settings.START_LENGTH, start_location=(0, 0), start_direction=Directions.RIGHT):
        self.x = start_location[0]
        self.y = start_location[1]
        self.speed = speed
        self.direction = start_direction
        self.controls = {} # Different snakes will have different controls

    def update(self):
        self.move(self.direction.value)

    # This does not work; why not?
    @property
    def location(self):
        return self.x, self.y

    def move(self, direction):
        self.x += self.speed * direction[0]
        self.y += self.speed * direction[1]
    
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
