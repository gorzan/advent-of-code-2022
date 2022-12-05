from dec4.dec4 import part_one, part_two, list_sections, encompasses

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_part_one():
    assert part_one(data) == 2


def test_part_two():
    assert part_two(data) == 4


def test_list_sections():
    assert list_sections(data.split(",")[0]) == [2,3,4]


def test_encompasses():
    pairs = data.split("\n")
    assert encompasses(pairs[0]) == False
    assert encompasses(pairs[3]) == True