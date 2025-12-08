num = []
with open("input_day3") as f:
    for line in f.readlines():

        num.append(int(line.rstrip("\n")))

def find_greatest(num):
    # turn single number into a list of numbers
    num_list = list(str(num))
    # print(num_list)
    new_num_list = []
    for num in num_list:
        new_num_list.append(int(num))

    # max1 = max2 = float('-inf')
    # for n in new_num_list:
    #     if n > max1:
    #         max2 = max1
    #         max1 = n
    #     elif n > max2 and n != max1:
    #         max2 = n

    # find max in num list

    highest = max(new_num_list)
    # print(highest)
    slice1 = new_num_list[:new_num_list.index(highest)+1]
    # print(slice1)
    slice2 = new_num_list[new_num_list.index(highest)+1:]
    # print(slice2)

    if slice2:
        new_number = int(str(max(slice1))+str(max(slice2)))
        return new_number
    else:
        slice1 = new_num_list[:new_num_list.index(highest)]
        # print(slice1)

        slice2 = new_num_list[new_num_list.index(highest):]
        # print(slice2)
        new_number = int(str(max(slice1)) + str(max(slice2)))
        return new_number


numbers_list =[]
for n in num:
    number_to_add = find_greatest(n)
    numbers_list.append(number_to_add)

print(sum(numbers_list))
