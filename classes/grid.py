from pygame import Surface
from window import Window

class Grid(Window):
    def __init__(self, dimensions):
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

    def add_component(self, component_name, component):
        self.components[component_name].extend(component)
    
    def remove_component(self, component_name, component):
        self.components[component_name].remove(component)

    def reset_component(self, component_name, component=None):
        self.components[component_name] = [] if component is None else component

    def reset_components(self):
        for component in self.components:
            self.components[component] = []

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