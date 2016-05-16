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

from booth.symbols import shapes
from booth.symbols import drawing
from booth.symbols import utils as symbol_utils

SURFACE_WIDTH, SURFACE_HEIGHT = 256, 256


def main():
    """And I am here"""

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_WIDTH,
                                 SURFACE_HEIGHT)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, SURFACE_WIDTH, SURFACE_HEIGHT)
    ctx.fill()

    size = (20, 20)
    ctx.set_source_rgb(0, 0, 0)

    first_rect = shapes.SimpleRect((10, 10), size)
    second_rect = shapes.SimpleRect((60, 10), size)
    third_rect = shapes.SimpleRect((10, 60), size)
    fourth_rect = shapes.SimpleRect((60, 60), size)

    drawing.draw_rect(ctx, first_rect)
    drawing.draw_rect(ctx, second_rect)
    drawing.draw_rect(ctx, third_rect)
    drawing.draw_rect(ctx, fourth_rect)

    ctx.fill()

    rects = [second_rect, fourth_rect]

    padded = symbol_utils.add_padding(
        symbol_utils.get_bounding_rect(rects), 10)

    drawing.draw_rect(ctx, padded)
    ctx.stroke()

    surface.write_to_png("example.png")


if __name__ == "__main__":
    main()
