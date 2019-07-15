from constants import settings


class Snake:
    def __init__(self, start_length=settings.START_LENGTH, start_location=(0, 0)):
        self.x = start_location[0]
        self.y = start_location[1]
        self.speed = 1
        self.controls = {} # Different snakes will have different controls

    # This does not work; why not?
    @property
    def location(self):
        return x, y

    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed
