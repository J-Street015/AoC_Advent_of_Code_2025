numbers = list(range(0,100))

turns = []
with open("input.txt") as f:
    for line in f.readlines():

        turns.append(line.rstrip("\n"))
print(f"number_list: {numbers}")
print(f"turn_list: {turns}")




# numbers= [0, 1, 2, 3, 4]
#
# turns = ["L2", "R3", "R5" ]
#
# code = []
#
# start=2
#
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
#         print(f"steps_to_the_left: {steps_to_right}")
#         print(f"number_of_interest: {numbers[steps_to_right]}")
#         start = numbers[steps_to_right]
#         # update code:
#         code.append(start)
#         start = numbers.index(start)
#         print(f"new_start_index: {start}")
#
# print(code)



