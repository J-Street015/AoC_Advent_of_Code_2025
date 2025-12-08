# turn each large number in a list itself and then do the pop method


num = []
with open("input_day3") as f:
    for line in f.readlines():

        num.append(int(line.rstrip("\n")))

print(num)

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



def get_highest(num):
    num_list = list(str(num))


    # print(num_list)
    numbers = []
    for number in num_list:
        numbers.append(int(number))

    # print(numbers)



    # create an empty dictionary to store the
    # numbers and their index
    number_dict = {}


    while len(number_dict) < 2:
        # get highest number
        max_num = max(numbers)
        # get the index of the highest number
        max_num_index = numbers.index(max_num)

        number_dict[max_num_index]= max_num
        # The pop function is wrong here,
        numbers.pop(numbers.index(max_num))


        # print(numbers)
        # print(number_dict)

    ### Sort the number dictionary by key which is the index
    sorted_dict = dict(sorted(number_dict.items(), key=lambda item: item[0]))
    # print(sorted_dict)

    highest_number = []
    # now add the values from the dict to a list
    for key, value in sorted_dict.items():
        # print(value)
        highest_number.append(value)
    highest_number = ''.join(map(str, highest_number))
    return highest_number

list_of_numbers= []
for n in num:
    high = get_highest(n)
    print(high)
    list_of_numbers.append(int(high))
print(sum(list_of_numbers))