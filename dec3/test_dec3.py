from dec3.dec3 import part_one, part_two, common_item,identify_groups,badge

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_part_one():
    assert part_one(data) == 157


def test_part_two():
    assert part_two(data) == 70


def test_common_item():
    assert common_item("abcABc") == "c"


def test_groups_badges():
    assert badge(identify_groups(data)[0]) == "r"