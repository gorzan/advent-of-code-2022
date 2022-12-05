import importlib
import sys


if len(sys.argv) <= 1:
    luke = 1
else:
    luke = int(sys.argv[1])


def get_data(file):
    with open(file) as f:
        data = f.read()

    return data


def print_day(n, part_one_answer, part_two_answer):
    print(f"### December {n} ###")
    print(f"Part One: {part_one_answer}")
    print(f"Part Two: {part_two_answer}")


for day in range(1, luke + 1):
    module = importlib.import_module(f"dec{day}.dec{day}")
    data = get_data(f"dec{day}/data/input.txt")
    print_day(day, module.part_one(data), module.part_two(data))