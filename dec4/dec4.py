def part_two(data):
    total_score = 0
    for pair in data.split("\n"):
        if overlaps(pair):
            total_score = total_score + 1
    return total_score


def part_one(data):
    total_score = 0
    for pair in data.split("\n"):
        if encompasses(pair):
            total_score = total_score + 1
    return total_score


def list_sections(section_range):
    start = int(section_range.split("-")[0])
    stop = int(section_range.split("-")[1])
    return [x for x in range(start, stop + 1)]


def subset_of(subset, fullset):
    for x in subset:
        if x not in fullset:
            return False
    return True


def encompasses(pair):
    range1 = list_sections(pair.split(",")[0])
    range2 = list_sections(pair.split(",")[1])

    if subset_of(range1, range2):
        return True
    elif subset_of(range2, range1):
        return True
    return False


def overlaps(pair):
    range1 = list_sections(pair.split(",")[0])
    range2 = list_sections(pair.split(",")[1])

    for x in range1:
        if x in range2:
            return True
    for x in range2:
        if x in range1:
            return True
    return False

