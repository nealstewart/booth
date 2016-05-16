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


def test_outside():
    rects = [
        shapes.SimpleRect((10, 10), (5, 5)),
        shapes.SimpleRect((20, 20), (30, 40))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (40, 50)

def test_contained():
    rects = [
        shapes.SimpleRect((10, 10), (10, 10)),
        shapes.SimpleRect((15, 10), (3, 3))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 10)
    assert bounding_rect.size == (10, 10)

def test_y_overlap():
    rects = [
        shapes.SimpleRect((10, 10), (10, 10)),
        shapes.SimpleRect((10, 7), (3, 3))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (10, 7)
    assert bounding_rect.size == (10, 13)
    
def test_x_overlap():
    rects = [
        shapes.SimpleRect((10, 10), (10, 10)),
        shapes.SimpleRect((7, 10), (3, 3))
    ]

    bounding_rect = utils.get_bounding_rect(rects)
    assert bounding_rect.location == (7, 10)
    assert bounding_rect.size == (13, 10)
