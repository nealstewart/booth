from booth.symbols import shapes
from booth.symbols import utils


class Symbol():

    def __init__(self):
        print("hello")

        size = (20, 20)

        self.shapes = [
            shapes.SimpleRect((10, 10), size),
            shapes.SimpleRect((60, 10), size),
            shapes.SimpleRect((10, 60), size),
            shapes.SimpleRect((60, 60), size)
        ]

        contained = [self.shapes[1], self.shapes[3]]

        self.containers = [
            utils.add_padding(utils.get_bounding_rect(contained), 10)
        ]

        self.lines = [
            (self.shapes[0], self.shapes[1]),
            (self.shapes[2], self.shapes[3])
        ]
