from booth.symbols import generation


def test_bounding_rect_for_single():
    single_rect = generation.SimpleRect((0, 10), (10, 10))
    bounding_rect = generation.get_bounding_rect([single_rect])
    assert bounding_rect.location == single_rect.location
    assert bounding_rect.size == single_rect.size


def test_bounding_rect_for_multiple():
    rects = [
        generation.SimpleRect((10, 10), (10, 10)),
        generation.SimpleRect((20, 20), (10, 10))
    ]

    bounding_rect = generation.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (20, 20)


def test_bounding_rect_for_size():
    rects = [
        generation.SimpleRect((10, 10), (5, 5)),
        generation.SimpleRect((20, 20), (20, 20))
    ]

    bounding_rect = generation.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (30, 30)

