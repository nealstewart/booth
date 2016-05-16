from booth.symbols import shapes

def get_bounding_rect(children):
    cmp_x = lambda rect: rect.location[0]
    cmp_y = lambda rect: rect.location[1] + rect.size[1]

    x_sorted_children = sorted(children, key=cmp_x)
    y_sorted_children = sorted(children, key=cmp_y)

    location = (x_sorted_children[0].location[0],
                y_sorted_children[0].location[1])

    size = (x_sorted_children[-1].location[0] - location[0] + x_sorted_children[-1].size[0],
            y_sorted_children[-1].location[1] - location[1] + y_sorted_children[-1].size[1])

    return shapes.SimpleRect(location, size)

def add_padding(rect, padding):
    return shapes.SimpleRect(
        (rect.location[0] - padding, rect.location[1] - padding),
        (rect.size[0] + 2 * padding, rect.size[1] + 2 * padding))
