import dec1.dec1
import dec2.dec2
import dec3.dec3
import dec4.dec4

def get_data(file):
    with open(file) as f:
        data = f.read()

    return data


def print_day(n, part_one_answer, part_two_answer):
    print(f"### December {n} ###")
    print(f"Part One: {part_one_answer}")
    print(f"Part Two: {part_two_answer}")


dec1_data = get_data(f"dec1/data/input.txt")
print_day(1, dec1.dec1.part_one(dec1_data), dec1.dec1.part_two(dec1_data))

dec2_data = get_data(f"dec2/data/input.txt")
print_day(2, dec2.dec2.part_one(dec2_data), dec2.dec2.part_two(dec2_data))

dec3_data = get_data(f"dec3/data/input.txt")
print_day(3, dec3.dec3.part_one(dec3_data), dec3.dec3.part_two(dec3_data))

dec4_data = get_data(f"dec4/data/input.txt")
print_day(4, dec4.dec4.part_one(dec4_data), dec4.dec4.part_two(dec4_data))