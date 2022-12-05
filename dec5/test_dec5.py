from dec5.dec5 import part_one, part_two, get_instructions, get_stacks, stacktops

data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_part_one():
    assert part_one(data) == "CMZ"


def test_part_two():
    assert part_two(data) == "MCD"


def test_instructions():
    assert get_instructions(data)[0] == "move 1 from 2 to 1"


def test_get_stacks():
    assert get_stacks(data)[1] == ['Z', 'N']


def test_stacktops():
    assert stacktops(get_stacks(data)) == "NDP"