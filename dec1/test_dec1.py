from dec1.dec1 import part_one, part_two

data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def test_part_one():
    assert part_one(data) == 24000

def test_part_two():
    assert part_two(data) == 45000