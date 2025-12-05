# turn each large number in a list itself and then do the pop method


# num = []
# with open("input_day3") as f:
#     for line in f.readlines():
#
#         num.append(int(line.rstrip("\n")))

# print(num)

# turn number into string and then into list items

def find_number(num):
    num_list = list(str(num))
    # print(num_list)

    num_dict = dict.fromkeys(num_list)
    # print(num_dict)
    value = 1

    for key in num_dict:
        value +=1
        num_dict[key] = int(key)


    # print(num_dict)
    # print(list(num_dict.items()))

    num_list_new = list(num_dict.items())
    highest_list = []
    for i in range(2):
        highest = max(num_list_new)
        # print(highest)
        highest_list.append(highest)
        num_list_new.pop(num_list_new.index(highest))
        # print(num_list_new)
    dict_highest = (dict(highest_list))

    highest_number = []

    for key, value in dict_highest.items():
        highest_number.append(value)
    highest_number = ''.join(map(str, highest_number))
    return highest_number


num =22122386335252214242232925223327233422
num_list = list(str(num))


print(num_list)
numbers = []
for number in num_list:
    numbers.append(int(number))

# print(numbers)

num_saved = int()

for i in range(2):
    max_num = max(numbers)
    print(max(numbers), numbers.index(max_num))
    numbers.pop(numbers.index(max_num))
    print(numbers)

# add the elements to a dictionary and then sort and get the
# print(keys)

my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sort by values (ascending)
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# sorted_by_values is {'a': 1, 'c': 2, 'b': 3}

# Sort by values (descending)
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
# sorted_by_values_desc is {'b': 3, 'c': 2, 'a': 1}
