# AoC day6 part 2. Code is maybe not good-looking, but it works.
from math import prod

number_map = []
with open("d6_input") as f:
    for line in f.readlines():
        number_map.append(line.rstrip("\n"))


def calculation(data):
    numbers = data[:-1]  # Keep as strings
    operators = data[-1].split()  # Last line contains operations
    total = 0
    digits = []
    # while numbers are not at position -1, they get added to numbers, if loop reaches pos -1 instead
    # of adding the code sums or multiplies the numbers collected so far, and resets the number list
    # # Iterate column-wise from right to left
    for i in range(len(numbers[0]) - 1, -2, -1):
        # If the column is empty (all spaces) or end of row
        if all(problem[i] == ' ' for problem in numbers) or i == -1:
            if numbers:
                op = operators.pop()
                if op == '+':
                    total += sum(digits)
                elif op == '*':
                    total += prod(digits)
                digits = []
        else:
            # Build the column as a string
            column = ''.join(problem[i] for problem in numbers).strip()
            if column:  # Ignore empty columns
                digits.append(int(column))

    return total


print(calculation(number_map))
