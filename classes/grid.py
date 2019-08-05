from pygame import Surface
from window import Window

class Grid(Window):
    def __init__(self, dimensions):
        self.dimensions = dimensions # For querying
        self.grid = [[None for x in range(dimensions[0])] for y in range(dimensions[1])]
        self.components = {
            'snakes': [],
            'snake_body': [],
            'apples': []
            }

    def add_component(self, component_name, component):
        self.components[component_name].extend(component)
    
    def remove_component(self, component_name, component):
        self.components[component_name].remove(component)

    def reset_component(self, component_name, component=None):
        self.components[component_name] = [] if component is None else component

    def reset_components(self):
        for component in self.components:
            self.components[component] = []

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