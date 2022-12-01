def calculate_backpacks(data):
    backpacks = []
    for backpack in data.split("\n\n"):
        backpacks.append(sum([int(food) for food in backpack.split("\n")]))
    return backpacks


def part_two(data):
    backpacks = calculate_backpacks(data)
    backpacks.sort(reverse=True)
    return backpacks[0] + backpacks[1] + backpacks[2]


def part_one(data):
    backpacks = calculate_backpacks(data)
    return max(backpacks)

