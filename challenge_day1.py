# Script to solve the day1 challenge part 1 and part2

numbers = list(range(0, 100))
turns = []
with open("input_day1.txt") as f:
    for line in f.readlines():
        turns.append(line.rstrip("\n"))

code = []
start = 50
counter = 0

for turn in turns:
    if "L" in turn:
        steps = int(turn.split("L")[1])
        # For Left Turn
        # slice the list of numbers at the start depending on left or right
        # split the list at the start position
        end_list = numbers[start + 1:]
        start_list = numbers[:start + 1]  # left turn slice
        # when it is a left turn add the end list in front of the start list
        # update of numbers list.
        numbers = end_list + start_list
        # now the first step is 10 steps to the left
        # divide steps 10 by the length of the list with modulo
        steps_to_left = steps % len(numbers)
        # count zero occurrence
        lists_needed = float(steps / len(numbers)).__ceil__()
        extended_list = (numbers * lists_needed + numbers)
        extended_list.reverse()

        for step in range(1, steps + 1):
            if extended_list[step] == 0:
                counter += 1
        # if start == 0:
        #     counter = counter - 1
        start = numbers[-(steps_to_left + 1)]
        # update the code list:
        code.append(start)
        # use the start number index to update the new position
        start = numbers.index(start)
    elif "R" in turn:
        steps = int(turn.split("R")[1])
        # For Right Turn
        # slice the list of numbers at the start depending on left or right
        # split the list at the start position
        start_of_list = numbers[start:]
        end_of_list = numbers[:start]  # left turn slice
        # when it is a left turn add the end list in front of the start list
        # update of numbers list.
        numbers = start_of_list + end_of_list
        steps_to_right = steps % len(numbers)
        # count zero occurrence
        lists_needed = float(steps / len(numbers)).__ceil__()
        extended_list = (numbers * lists_needed + numbers)

        for step in range(1, steps + 1):
            if extended_list[step] == 0:
                counter += 1

        start = numbers[steps_to_right]
        # update code:
        code.append(start)
        start = numbers.index(start)

print(f"code: {code.count(0)}")  # Answer part1
print(f"counter: {counter}")  # Answer part2