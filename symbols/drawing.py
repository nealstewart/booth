"Drawing logic for symbols"

from booth.symbols import shapes
from booth.symbols import utils

def draw_rect(ctx, rect):
    ctx.rectangle(
        rect.location[0], rect.location[1],
        rect.size[0], rect.size[1])

def draw_symbol(ctx, symbol):
    ctx.set_source_rgb(0, 0, 0)

    for shape in symbol.shapes:
        draw_rect(ctx, shape)

    ctx.fill()

    for container in symbol.containers:
        draw_rect(ctx, container)

    ctx.stroke()