def battle(you, them):
    if you == them:
        return "draw"
    elif you == "rock" and them == "scissors":
        return "win"
    elif you == "paper" and them == "rock":
        return "win"
    elif you == "scissors" and them == "paper":
        return "win"
    else:
        return "lose"


def score_battle(outcome):
    if outcome == "win":
        return 6
    elif outcome == "draw":
        return 3
    elif outcome == "lose":
        return 0


def score_shape(shape):
    if shape == "rock":
        return 1
    elif shape == "paper":
        return 2
    elif shape == "scissors":
        return 3


def decode_shape(input):
    if input == "A" or input == "X":
        return "rock"
    elif input == "B" or input == "Y":
        return "paper"
    elif input == "C" or input == "Z":
        return "scissors"


def decode_strategy(input):
    if input == "X":
        return "lose"
    elif input == "Y":
        return "draw"
    elif input == "Z":
        return "win"


def choose_shape(them, strategy):
    if strategy == "draw":
        return them
    elif strategy == "win":
        if them == "rock":
            return "paper"
        elif them == "paper":
            return "scissors"
        elif them == "scissors":
            return "rock"
    elif strategy == "lose":
        if them == "rock":
            return "scissors"
        elif them == "paper":
            return "rock"
        elif them == "scissors":
            return "paper"


def score_round(you, them):
    return score_shape(you) + score_battle(battle(you, them))


def part_two(data):
    total_score = 0
    for round in data.split('\n'):
        them = decode_shape(round.split(" ")[0])
        strategy = decode_strategy(round.split(" ")[1])
        you = choose_shape(them, strategy)
        total_score = total_score + score_round(you, them)
    return total_score


def part_one(data):
    total_score = 0
    for round in data.split('\n'):
        you = decode_shape(round.split(" ")[1])
        them = decode_shape(round.split(" ")[0])
        total_score = total_score + score_round(you, them)
    return total_score

