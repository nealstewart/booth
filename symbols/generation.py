def add_padding(rect, padding):
    return SimpleRect(
        (rect.location[0] - padding, rect.location[1] - padding),
        (rect.size[0] + 2 * padding, rect.size[1] + 2 * padding))
