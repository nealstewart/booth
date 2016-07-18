from symbols import shapes
from symbols import utils
from random import randint

# Symbols have:
# - shapes
# - lines
# - containers

# Lines have
# - start : Shape
# - end : Shape

class Symbol():

    def create_rect(self):
        size = (20, 20)
        x = (randint(0, self.bounds[0] - size[0] - 10))
        y = (randint(0, self.bounds[1] - size[1] - 10))
        return shapes.SimpleRect((x, y), size)

    def __init__(self, bounds):
        self.bounds = bounds

        self.shapes = [
            self.create_rect(),
            self.create_rect(),
            self.create_rect(),
            self.create_rect()
        ]

        contained = [self.shapes[1], self.shapes[3]]

        self.containers = [
            utils.add_padding(utils.get_bounding_rect(contained), 10)
        ]

        self.lines = [
            (self.shapes[0], self.shapes[2]),
            (self.shapes[2], self.shapes[3])
        ]
