def part_one(data):
    visible_trees = 0
    forest = data.split("\n")
    for y, row in enumerate(forest):
        for x, tree in enumerate(row):
            if visible(x, y, forest):
                visible_trees = visible_trees + 1

    return visible_trees


def part_two(data):
    optimal_scenic = 0
    forest = data.split("\n")
    for y, row in enumerate(forest):
        for x, tree in enumerate(row):
            scenic = scenic_up(x, y, forest) * scenic_down(x, y, forest) * scenic_left(x, row) * scenic_right(x, row)
            if scenic > optimal_scenic:
                optimal_scenic = scenic
    return optimal_scenic


def visible_from_left(index, row):
    if index == 0:
        return True

    height = row[index]
    for tree in row[0:index]:
        if tree >= height:
            return False
    return True


def visible_from_right(index, row):
    if index == len(row) - 1:
        return True

    height = row[index]
    for tree in row[index+1:]:
        if tree >= height:
            return False
    return True


def visible_from_top_or_bottom(col_index, row_index, forest):
    column = []
    for row in forest:
        column.append(int(row[col_index]))

    if visible_from_left(row_index, column):
        return True
    elif visible_from_right(row_index, column):
        return True
    return False


def visible(x, y, forest):
    if visible_from_left(x, forest[y]):
        return True
    elif visible_from_right(x, forest[y]):
        return True
    elif visible_from_top_or_bottom(x, y, forest):
        return True
    return False


def scenic_left(index, row):
    height = row[index]
    scenic = 0
    for tree in row[0:index][::-1]:
        scenic = scenic + 1
        if tree >= height:
            break
    return scenic


def scenic_right(index, row):
    height = row[index]
    scenic = 0
    for tree in row[index+1:]:
        scenic = scenic + 1
        if tree >= height:
            break
    return scenic


def scenic_up(col_index, row_index, forest):
    column = []
    for row in forest:
        column.append(int(row[col_index]))

    scenic = scenic_left(row_index, column)
    return scenic


def scenic_down(col_index, row_index, forest):
    column = []
    for row in forest:
        column.append(int(row[col_index]))

    scenic = scenic_right(row_index, column)
    return scenic
