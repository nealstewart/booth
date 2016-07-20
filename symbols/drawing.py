"Drawing logic for symbols"

from symbols import shapes
from symbols import utils


def draw_line(ctx, line):
    first_point = utils.get_center(line[0])
    second_point = utils.get_center(line[1])

    ctx.move_to(first_point[0], first_point[1])
    ctx.line_to(second_point[0], second_point[1])
    ctx.close_path()
    ctx.stroke()

def draw_symbol(ctx, symbol):
    ctx.set_source_rgb(0, 0, 0)

    for shape in symbol.shapes:
        shape.draw(ctx)

    ctx.fill()

    for container in symbol.containers:
        container.draw(ctx)

    ctx.stroke()

    for line in symbol.lines:
        draw_line(ctx, line)
