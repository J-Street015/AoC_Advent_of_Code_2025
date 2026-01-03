# AoC day3 part 1 challenge. Code works.

num = []
with open("input_day3") as f:
    for line in f.readlines():
        num.append(int(line.rstrip("\n")))

def find_greatest(num):
    # turn single number into a list of numbers
    num_list = list(str(num))
    new_num_list = []
    for num in num_list:
        new_num_list.append(int(num))

    highest = max(new_num_list)
    slice1 = new_num_list[:new_num_list.index(highest)+1]
    slice2 = new_num_list[new_num_list.index(highest)+1:]
    if slice2:
        new_number = int(str(max(slice1))+str(max(slice2)))
        return new_number
    else:
        slice1 = new_num_list[:new_num_list.index(highest)]
        slice2 = new_num_list[new_num_list.index(highest):]
        new_number = int(str(max(slice1)) + str(max(slice2)))
        return new_number


numbers_list =[]
for n in num:
    number_to_add = find_greatest(n)
    numbers_list.append(number_to_add)

print(sum(numbers_list))
