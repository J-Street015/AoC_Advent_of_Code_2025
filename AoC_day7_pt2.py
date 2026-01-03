# AoC day7 part2. Code fixed. works.

data = []
with open("d7_input") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

rows = len(data)
cols = len(data[0])

start_col = data[0].index("S")

dat_dict = {}


def calculation(row, col):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return 1
    if (row, col) in dat_dict:
        return dat_dict[(row, col)]
    current_cell = data[row][col]
    if current_cell == "^":
        left_path = calculation(row + 1, col - 1)
        right_path = calculation(row + 1, col + 1)
        res = left_path + right_path
    elif current_cell == ".":
        res = calculation(row + 1, col)
    else:
        res = 0

    dat_dict[(row, col)] = res
    return res


total_paths = calculation(1, start_col)
print(total_paths)
