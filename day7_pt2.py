# read in the data

from numpy.ma.core import left_shift

data = []
with open("d7_input") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

# grid = [list(line) for line in open("day7.txt", "r").read().splitlines()]
grid = data
rows = len(grid)
cols = len(grid[0])

start_col = grid[0].index("S")

memo = {}


def traverse(row, col):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return 1

    if (row, col) in memo:
        return memo[(row, col)]

    current_cell = grid[row][col]

    if current_cell == "^":
        left_path = traverse(row + 1, col - 1)
        right_path = traverse(row + 1, col + 1)
        result = left_path + right_path
    elif current_cell == ".":
        result = traverse(row + 1, col)
    else:
        result = 0

    memo[(row, col)] = result
    return result


total_paths = traverse(1, start_col)
print(total_paths)
