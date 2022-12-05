import sys
import os

day = sys.argv[1]

logicfile = """def part_one(data):
    score = 0
    return score


def part_two(data):
    score = 0
    return score
"""

testfile = f"""from {day}.{day} import part_one, part_two

data = ''


def test_part_one():
    assert part_one(data) == 0


def test_part_two():
    assert part_two(data) == 0
"""

if os.path.exists(day):
    print ("exists!")
    exit()

os.makedirs(f"{day}/data")
print("folder structure created")

with open(f"{day}/data/input.txt", "w+") as f:
    f.write("")
    print("input file created")

with open(f"{day}/__init__.py", "w+") as f:
    f.write("")
    print("__init__.py file created")

with open(f"{day}/test_{day}.py", "w+") as f:
    f.write(testfile)
    print("test file created")

with open(f"{day}/{day}.py", "w+") as f:
    f.write(logicfile)
    print("logic file created")