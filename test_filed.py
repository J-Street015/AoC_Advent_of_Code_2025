numbers = [0, 1, 10]
steps = 7
counter = 0
start = 0
lists_needed = float(steps / len(numbers)).__ceil__()

print(numbers * lists_needed)
extended_list = (numbers * lists_needed)
extended_list.reverse()
print(extended_list)
for step in range(1, steps+1 ):
    print(extended_list[step])
    if extended_list[step] == 0:
        counter += 1
if start == 0:
    counter = counter -1

# print(counter)
