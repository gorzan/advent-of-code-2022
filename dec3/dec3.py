def part_two(data):
    total_score = 0
    groups = identify_groups(data)
    for group in groups:
        total_score = total_score + priority(badge(group))
    return total_score


def part_one(data):
    total_score = 0
    for rucksack in data.split("\n"):
        total_score = total_score + priority(common_item(rucksack))
    return total_score


def priority(item):
    unicode = ord(item)
    if unicode <= 90:
        priority = unicode - 64 + 26
    else:
        priority = unicode - 96
    return priority


def common_item(rucksack):
    first_compartment  = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    for item in first_compartment:
        if item in second_compartment:
            return item


def badge(group):
    rucksacks = group.split("\n")
    candidates = []
    for item in rucksacks[0]:
        if item in rucksacks[1]:
            candidates.append(item)
    for item in candidates:
        if item in rucksacks[2]:
            return item


def identify_groups(data):
    rucksacks = data.split("\n")
    return ["\n".join(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]

