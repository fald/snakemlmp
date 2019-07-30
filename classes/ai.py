import pygame
from pygame.locals import *
from constants.enums import Directions
from random import choice

class AI:

    outputs = [
        Directions.DOWN,
        Directions.LEFT,
        Directions.UP,
        Directions.RIGHT
    ]

    def __init__(self, parent=None):
        self.parent = parent

    def determine_move(self, board):
        raise NotImplementedError("This method has not been implemented for this AI!")

    def check_obstacle(self, direction):
        # Just going to check for own tail right now.
        # Mod this to take into account walls, 'cause it doesn't.
        snake = self.parent
        direction = direction.value
        for segment in snake.body:
            if (
                segment.grid_x == snake.grid_x + direction[0] and
                segment.grid_y == snake.grid_y + direction[1]
            ):
                return True
        return False
    
    def check_obstacles(self):
        # for direction in Directions:
            # self.check_obstacle(direction)
        return {direction: self.check_obstacle(direction) for direction in Directions}

    def convert_relative_to_absolute(self, relative):
        # I -could- just if-else everything, but I wanna be smug about this mess.
        facing = self.parent.direction.value
        absolute = (
            facing[1] * -1 * (1 if (relative[0] > 0) else -1),
            facing[0] * -1 * (1 if (relative[0] < 0) else -1)
        )

        return absolute

    def find_apple(self, apples=None):
        # Return direction(s) to...one apple. Mod it for nearest apple in future.
        # Also mod it to take into account wrap-around, cause it doesn't.
        # Should probably use relative direction here.
        if apples is None:
            return self.parent.direction
        apple = apples[0]
        snake = self.parent
        x_move = apple.grid_x - snake.grid_x
        y_move = apple.grid_y - snake.grid_y

        dirs_to_apple = []
        if x_move != 0:
            dirs_to_apple.append(Directions((int(x_move / abs(x_move)), 0)))
        if y_move != 0:
            dirs_to_apple.append(Directions((0, int(y_move / abs(y_move)))))
        return dirs_to_apple


class Basic(AI):
    def __init__(self, parent=None):
        super(Basic, self).__init__(parent)

    def determine_move(self, board):
        # Real fuckin' dumb!
        return choice(AI.outputs)


class Defensive(AI):
    def __init__(self, aggression=0, parent=None):
        super(Defensive, self).__init__(parent)
        # Aggression is how much it goes towards the apples.
        # Keep in mind this AI is dumb as hell and only sees 1 move in advance. It will absolutely fuck itself immediately.
        self.aggression = aggression

    def determine_move(self, board, apples=None):
        danger = self.check_obstacles()
        available = []
        for direction in danger:
            if not danger[direction]:
                available.append(direction)

        apple = self.find_apple(apples)
        best = list(set(apple).intersection(available))
        if len(best) > 0:
            return choice(best)
        elif len(available) > 0:
            return choice(available)
        else:
            return self.parent.direction # Doomed, boys.


class ML(AI):
    def __init__(self, parent=None):
        super(ML, self).__init__(parent)
    
    def determine_move(self, board):
        pass
