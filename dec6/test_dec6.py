from dec6.dec6 import part_one, part_two

data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'


def test_part_one():
    assert part_one(data) == 7


def test_part_two():
    assert part_two(data) == 19
