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
import numpy

SURFACE_WIDTH, SURFACE_HEIGHT = 256, 256


def get_bounding_rect(children):
    cmp_x = lambda rect: rect.location[0]
    cmp_y = lambda rect: rect.location[1] + rect.size[1]

    x_sorted_children = sorted(children, key=cmp_x)
    y_sorted_children = sorted(children, key=cmp_y)

    location = (x_sorted_children[0].location[0],
                y_sorted_children[0].location[1])

    size = (x_sorted_children[-1].location[0] - location[0] + x_sorted_children[-1].size[0],
            y_sorted_children[-1].location[1] - location[1] + y_sorted_children[-1].size[1])

    return SimpleRect(location, size)


class SimpleRect():
    "Simple rectangle"

    def __init__(self, location, size):
        self.location = location
        self.size = size
        
def draw_rect(ctx, rect):
    ctx.rectangle(
        rect.location[0], rect.location[1],
        rect.size[0], rect.size[1])

def add_padding(rect, padding):
    return SimpleRect(
        (rect.location[0] - padding, rect.location[1] - padding),
        (rect.size[0] + 2 * padding, rect.size[1] + 2 * padding))


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

    first_rect = SimpleRect((10, 10), size)
    second_rect = SimpleRect((60, 10), size)
    third_rect = SimpleRect((10, 60), size)
    fourth_rect = SimpleRect((60, 60), size)

    draw_rect(ctx, first_rect)
    draw_rect(ctx, second_rect)
    draw_rect(ctx, third_rect)
    draw_rect(ctx, fourth_rect)
    ctx.fill()

    rects = [second_rect, fourth_rect]

    padded = add_padding(get_bounding_rect(rects), 10)

    draw_rect(ctx, padded)
    ctx.stroke()

    surface.write_to_png("example.png")


if __name__ == "__main__":
    main()
