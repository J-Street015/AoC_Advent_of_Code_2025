



# turn each large number in a list itself and then do the pop method


num = 2712233521522212239633525221424223292522332923342263323223226223332531222232333293222213262324223122

# make list from the numbers
num_list = list(str(num))
# create a dictionary from the list of numbers with the number strings as keys.
# this removes the duplicated digits, but also keeps the order of numbers.
num_dict  = dict.fromkeys(list(str(num)))

num_list_updated = []
for key, value in num_dict.items():
    num_list_updated.append(int(key))

print(num_list_updated)

# The insert() method lets you add an item at a specific index in the list.
# As you know, list elements are ordered, starting with index 0 for the first item.
# The insert() method takes two parameters: the index of the new element to be added and the value of the element.

two_highest = []
for i in range(2):
    # find highest number:
    highest_number, index_highest = max(num_list_updated) ,num_list_updated.index(max(num_list_updated))
    print(highest_number, index_highest)
    two_highest.insert(index_highest, highest_number)
    # remove the highest number from the list
    num_list_updated.pop(index_highest)

    print(num_list_updated)
print(two_highest)