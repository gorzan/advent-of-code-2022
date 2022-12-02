from dec2.dec2 import part_one, part_two, battle, choose_shape

data = """A Y
B X
C Z"""


def test_part_one():
    assert part_one(data) == 15


def test_part_two():
    assert part_two(data) == 12


def test_battle():
    assert(battle("rock","paper") == "lose")
    assert(battle("scissors","paper") == "win")
    assert(battle("paper","paper") == "draw")


def test_strategy():
    assert(choose_shape("rock", "win")=="paper")
    assert(choose_shape("paper", "draw")=="paper")
    assert(choose_shape("scissors", "lose")=="paper")