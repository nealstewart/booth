from booth.symbols import shapes

def get_center(shape):
    x_coord = shape.location[0] + (shape.size[0] / 2)
    y_coord = shape.location[1] + (shape.size[1] / 2)
    return (x_coord, y_coord)

def get_bounding_rect(children):
    cmp_left = lambda rect: rect.location[0]
    cmp_right = lambda rect: rect.location[0] + rect.size[0]
    cmp_bottom = lambda rect: rect.location[1]
    cmp_top = lambda rect: rect.location[1] + rect.size[1]

    x_min = min(children, key=cmp_left)
    x_max = max(children, key=cmp_right)

    y_min = min(children, key=cmp_bottom)
    y_max = max(children, key=cmp_top)

    location = (x_min.location[0],
                y_min.location[1])

    size = (x_max.location[0] - location[0] + x_max.size[0],
            y_max.location[1] - location[1] + y_max.size[1])

    return shapes.SimpleRect(location, size)

def add_padding(rect, padding):
    return shapes.SimpleRect(
        (rect.location[0] - padding, rect.location[1] - padding),
        (rect.size[0] + 2 * padding, rect.size[1] + 2 * padding))
