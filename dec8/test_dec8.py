from dec8.dec8 import part_one, part_two, visible_from_left, visible_from_right, visible_from_top_or_bottom, visible, scenic_left, scenic_right

data = """30373
25512
65332
33549
35390"""

forest = data.split("\n")


def test_part_one():
    assert part_one(data) == 21


def test_part_two():
    assert part_two(data) == 8


def test_visible_from_left():
    assert visible_from_left(2, forest[0]) is False
    assert visible_from_left(3, forest[0]) is True
    assert visible_from_left(0, forest[2]) is True
    assert visible_from_left(1,  [7, 1, 3, 4, 9]) is False


def test_visible_from_right():
    assert visible_from_right(1, forest[2]) is True
    assert visible_from_right(2, forest[2]) is False
    assert visible_from_right(4, forest[2]) is True
    assert visible_from_right(1,  [7, 1, 3, 4, 9]) is False


def test_visible_from_top_or_bottom():
    assert visible_from_top_or_bottom(0, 0, forest) is True
    assert visible_from_top_or_bottom(2, 1, forest) is True
    assert visible_from_top_or_bottom(3, 1, forest) is False


def test_visible():
    assert visible(1, 1, forest) is True
    assert visible(2, 1, forest) is True
    assert visible(3, 1, forest) is False
    assert visible(1, 2, forest) is True
    assert visible(2, 2, forest) is False
    assert visible(3, 2, forest) is True
    assert visible(2, 3, forest) is True
    assert visible(1, 3, forest) is False
    assert visible(3, 3, forest) is False


def test_scenic_left():
    assert scenic_left(0, forest[0]) == 0
    assert scenic_left(1, forest[0]) == 1
    assert scenic_left(4, forest[0]) == 1
    assert scenic_left(4, forest[1]) == 2


def test_scenic_right():
    assert scenic_right(4, forest[0]) == 0
    assert scenic_right(3, forest[0]) == 1
    assert scenic_right(0, forest[0]) == 2
    assert scenic_right(2, forest[1]) == 2
