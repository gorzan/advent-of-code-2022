import math


def part_one(data):
    stacks = get_stacks(data)
    for line in get_instructions(data):
        instruction = line.split(" ")
        moves = int(instruction[1])
        origin = int(instruction[3])
        destination = int(instruction[5])

        for move in range(0, moves):
            item = stacks[origin].pop()
            stacks[destination].append(item)

    return stacktops(stacks)


def part_two(data):
    stacks = get_stacks(data)
    for line in get_instructions(data):
        instruction = line.split(" ")
        moves = int(instruction[1])
        origin = int(instruction[3])
        destination = int(instruction[5])

        temp_stack = []
        for move in range(0, moves):
            item = stacks[origin].pop()
            temp_stack.append(item)

        for move in range(0, moves):
            item = temp_stack.pop()
            stacks[destination].append(item)

    return stacktops(stacks)


def get_instructions(data):
    return data.split("\n\n")[1].split("\n")


def get_stacks(data):
    stacks_string = data.split("\n\n")[0]
    stacks = [[]]
    for column in range(0, count_stacks(stacks_string)):
        stack = []
        for line in stacks_string.split("\n"):
            item = line[column*4:column*4+3]
            if item[0] == "[":
                stack.append(item[1:2])
        stack.reverse()
        stacks.append(stack)
    return stacks


def count_stacks(stacks_string):
    line_length = 0
    for line in stacks_string.split("\n"):
        if len(line) > line_length:
            line_length = len(line)

    return math.ceil(line_length / 4)


def stacktops(stacks):
    code = ""
    for stack in stacks:
        if len(stack)>0:
            code = code + stack.pop()
    return code
