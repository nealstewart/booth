"Drawing logic for symbols"

from booth.symbols import shapes
from booth.symbols import utils


def draw_rect(ctx, rect):
    ctx.rectangle(
        rect.location[0], rect.location[1],
        rect.size[0], rect.size[1])
        
def draw_line(ctx, line):
    print('drawing line')
    
    first_point = utils.get_center(line[0])
    second_point = utils.get_center(line[1])
    
    ctx.move_to(first_point[0], first_point[1])
    ctx.line_to(second_point[0], second_point[1])
    ctx.close_path()
    ctx.stroke()

def draw_symbol(ctx, symbol):
    ctx.set_source_rgb(0, 0, 0)

    for shape in symbol.shapes:
        draw_rect(ctx, shape)

    ctx.fill()

    for container in symbol.containers:
        draw_rect(ctx, container)

    ctx.stroke()
    
    for line in symbol.lines:
        draw_line(ctx, line)