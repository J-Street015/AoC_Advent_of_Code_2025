# This Script worked and has done the job to solve the first puzzle

# import the numbers and turns from the input.py file

from input import turns
from input import numbers

code = []
start=50

# for turn in turns:
#     if "L" in turn:
#         steps = int(turn.split("L")[1])
#         # For Left Turn
#         # slice the list of numbers at the start depending on left or right
#         # split the list at the start position
#         end_list= numbers[start + 1:]
#         print(f"end_of_list_left: {end_list}")
#
#         start_list = numbers[:start + 1] # left turn slice
#         print(f"start_of_list_left: {start_list}")
#
#         # when it is a left turn add the end list in front of the start list
#         # update of numbers list.
#         numbers = end_list + start_list
#         print(numbers)
#
#         # now the first step is 10 steps to the left
#
#         # divide steps 10 by the length of the list with modulo
#
#         steps_to_left = steps % len(numbers)
#         print(f"steps_to_the_left: {steps_to_left}")
#         print(f"number_of_interest: {numbers[-(steps_to_left +1)]}")
#
#
#
#         #TODO
#         # Update the start position
#         start = numbers[-(steps_to_left +1)]
#         # update the code list:
#         code.append(start)
#         # use the start number index to update the new position
#         start = numbers.index(start)
#         print(f"new_start_index: {start}")
# #TODO
# # do the same for the right turn version.
#     elif "R" in turn:
#         steps = int(turn.split("R")[1])
#         # For Right Turn
#         # slice the list of numbers at the start depending on left or right
#         # split the list at the start position
#         start_of_list= numbers[start:]
#         print(f"end_of_list: {start_of_list}")
#
#         end_of_list = numbers[:start] # left turn slice
#         print(f"start_of_list: {end_of_list}")
#
#         # when it is a left turn add the end list in front of the start list
#         # update of numbers list.
#         numbers = start_of_list + end_of_list
#         print(f"new_list: {numbers}")
#
#
#         steps_to_right = steps % len(numbers)
#         print(f"steps_to_the_right: {steps_to_right}")
#         print(f"number_of_interest: {numbers[steps_to_right]}")
#         start = numbers[steps_to_right]
#         # update code:
#         code.append(start)
#         start = numbers.index(start)
#         print(f"new_start_index: {start}")
#
# print(code.count(0))

# code = []
counter = 0
# start = 50

for turn in turns:
    if "L" in turn:
        steps = int(turn.split("L")[1])
        # For Left Turn
        # slice the list of numbers at the start depending on left or right
        # split the list at the start position
        end_list= numbers[start + 1:]
        print(f"end_of_list_left: {end_list}")

        start_list = numbers[:start + 1] # left turn slice
        print(f"start_of_list_left: {start_list}")

        # when it is a left turn add the end list in front of the start list
        # update of numbers list.
        numbers = end_list + start_list
        print(f"left_list: {numbers}")

        # now the first step is 10 steps to the left

        # divide steps 10 by the length of the list with modulo

        steps_to_left = steps % len(numbers)
        print(f"steps_to_the_left: {steps_to_left}")
        print(f"number_of_interest: {numbers[-(steps_to_left +1)]}")

        # count zero occurrence
        lists_needed = float(steps/ len(numbers)).__ceil__()

        print(numbers * lists_needed)
        extended_list = (numbers * lists_needed + numbers)
        extended_list.reverse()

        for step in range(1, steps + 1):
            print(extended_list[step])
            if extended_list[step] == 0:
                counter += 1
        # if start == 0:
        #     counter = counter - 1

        print(counter)

        #TODO
        # Update the start position
        start = numbers[-(steps_to_left +1)]
        # update the code list:
        code.append(start)
        # use the start number index to update the new position
        start = numbers.index(start)
        print(f"new_start_index: {start}")
#TODO
# do the same for the right turn version.
    elif "R" in turn:
        steps = int(turn.split("R")[1])
        # For Right Turn
        # slice the list of numbers at the start depending on left or right
        # split the list at the start position
        start_of_list= numbers[start:]
        print(f"end_of_list: {start_of_list}")

        end_of_list = numbers[:start] # left turn slice
        print(f"start_of_list: {end_of_list}")

        # when it is a left turn add the end list in front of the start list
        # update of numbers list.
        numbers = start_of_list + end_of_list
        print(f"new_list: {numbers}")


        steps_to_right = steps % len(numbers)
        print(f"steps_to_the_left: {steps_to_right}")
        print(f"number_of_interest: {numbers[steps_to_right]}")

        # count zero occurrence

        lists_needed = float(steps/len(numbers)).__ceil__()

        print("lists_needed")
        print(numbers * lists_needed)
        extended_list = (numbers * lists_needed + numbers)

        for step in range(1, steps + 1):
            print(extended_list[step])
            if extended_list[step] == 0:
                counter += 1
        # if start == 0:
        #     counter = counter - 1

        print(counter)




        start = numbers[steps_to_right]
        # update code:
        code.append(start)
        start = numbers.index(start)
        print(f"new_start_index: {start}")


print(f"code: {code.count(0)}") # Answer to initial Riddle day1
print(f"counter: {counter}") # Answer to second riddle day 1

print(code.count(0) + counter)