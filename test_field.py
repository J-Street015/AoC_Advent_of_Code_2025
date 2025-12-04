



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

# find the two highest digits in the list

for i, num in enumerate(num_list_updated):
    num1 = (num, i)
    print(num1)

