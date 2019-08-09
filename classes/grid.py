from pygame import Surface
from window import Window
from constants.settings import BLOCK_SIZE, BACKGROUND_PLAY_AREA

class Grid(Window):
    def __init__(
        self, dimensions, surface=None, 
        color=BACKGROUND_PLAY_AREA, image=None, rel_location=Locations.CENTER, 
        components=None, visible=False, properties=None, parent=None
        ):
        resolution = BLOCK_SIZE
        super(Grid, self).__init__(
            resolution=resolution, surface=surface, color=color,
            image=image, rel_location=rel_location, components=components,
            visible=visible, properties=properties, parent=parent
            )

        self.dimensions = dimensions # For querying
        self.components = {
            'snakes': [],
            # ?? The fuck was I thinking.
            #'snake_body': [],
            'apples': []
            }
        self.grid = None
        self.clear_grid()

    def clear_grid(self):
        self.grid = [[None for x in range(dimensions[0])] for y in range(dimensions[1])]

    def update(self):
        # ew.
        self.clear_grid()
        for component in components:
            for individual in component:
                # uh no, I built it weird, how do I get body parts...
                if type(individual) == Snake:
                    individual.update()
                    for segment in individual.body:                
                        self.grid[segment.grid_x][segment.grid_y] = segment
                self.grid[individual.grid_x][individual.grid_y] = individual

    def update_score(self):
        self.parent.components['windows']['score'].update_score(self.components['snakes'])

    def remove(self, index):
        self.grid[index[0]][index[1]] = None

    def add(self, index, object):
        self.grid[index[0]][index[1]] = object

    def get(self, location):
        return self.grid[location[0]][location[1]]

    def is_occupied(self, location=None):
        if location is not None:
            return self.get(location) is not None
        else:
            return [[row is not None for row in column] for column in self.grid]