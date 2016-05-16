"Tests for generation module"

from booth.symbols import utils
from booth.symbols import shapes


def test_bounding_rect_for_single():
    single_rect = shapes.SimpleRect((0, 10), (10, 10))
    bounding_rect = utils.get_bounding_rect([single_rect])
    assert bounding_rect.location == single_rect.location
    assert bounding_rect.size == single_rect.size


def test_bounding_rect_for_multiple():
    rects = [
        shapes.SimpleRect((10, 10), (10, 10)),
        shapes.SimpleRect((20, 20), (10, 10))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (20, 20)


def test_bounding_rect_for_size():
    rects = [
        shapes.SimpleRect((10, 10), (5, 5)),
        shapes.SimpleRect((20, 20), (30, 40))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (40, 50)
