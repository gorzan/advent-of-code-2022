def part_one(data):
    return find_marker(data, 4)


def check_unique(string):
    for char in string:
        if string.count(char) > 1:
            return False
    return True


def part_two(data):
    return find_marker(data, 14)


def find_marker(signal, marker_length):
    buffer = [x for x in signal[0:marker_length]]
    pos = marker_length
    for char in signal[marker_length:]:
        if check_unique(buffer):
            return pos
        else:
            pos = pos + 1
            buffer.pop(0)
            buffer.append(char)
