"""
Procedural Symbol Generator
Ok, so the plan here is to:

1. get the basic symbol from the book rendering
2. use a "contains" method to draw a rectangle around the other two rectangles
3. extract a first iteration of the shape type
4. extract a first iteration of the symbol type
5. play with the symbol data type to try and render other versions

"""

import cairocffi as cairo
from itertools import repeat

from symbols import creation
from symbols import drawing

SURFACE_WIDTH, SURFACE_HEIGHT = 256, 256

def main():
    """And I am here"""

    for i in iter(range(10)):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_WIDTH,
                                     SURFACE_HEIGHT)
        ctx = cairo.Context(surface)

        ctx.set_source_rgb(1, 1, 1)
        ctx.rectangle(0, 0, SURFACE_WIDTH, SURFACE_HEIGHT)
        ctx.fill()
        symbol = creation.Symbol((SURFACE_WIDTH, SURFACE_HEIGHT))
        drawing.draw_symbol(ctx, symbol)
        surface.write_to_png("output/example " + str(i) + ".png")

    print("Created symbols!")


if __name__ == "__main__":
    main()
