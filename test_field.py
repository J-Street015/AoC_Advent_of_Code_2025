import numpy
import scipy

import numpy as np
import scipy
ranges = []
ids = []

with open("input_day5.txt") as f:
    for line in f.readlines():
        l = line.rstrip('\n')
        if "-" in l:
            # print(f"line: {l} is a range")
            ranges.append(l)
            # for part 2 of the challenge code below not needed.
        # else:
        #     # print(f'line: {l} is an ID')
        #     ids.append(l)


# create a list with range
list_of_ranges = []
for r in ranges:
    n1 = int(r.split("-")[0])
    n2 = int(r.split("-")[1])
    for i in range(n1, n2+1):
        list_of_ranges.append(i)
# print(list_of_ranges)

# ranges_array = np.array(list_of_ranges, dtype=object)object
# print(ranges_array)
#

# turn list of ranges into
# turn the range lists into real ranges, but doing it in a for loop
# breaks the memory of the machine.
# fresh_list = []
# for r in list_of_ranges:
#         id_range = range(r[0], r[1] + 1)
#         for id in id_range:
#             fresh_list.append(id)
#


#
# fresh_list_clean = []
# for element in fresh_list:
#     print(element)
#     for i in element:
#         if len(element) > 0:
#             fresh_list_clean.append(i)
#
# fresh = []
# for f in fresh_list:
#     fresh.append(f[0])
#
#
#
# rotten= []
# # for n in ids_int:
# #     print(n)
# #     for element in ranges_array:
# #         if n in element:
# #             # print(f"found {n} in {element}")
# #             fresh.append(n)
# #         else:
# #             rotten.append(n)
# #             # ids_int.pop(ids_int.index(n))
#
# # remove duplicated elements from the list fresh
#
# fresh_dict= dict.fromkeys(fresh_list_clean)
# fresh_no_dup=[]
# for k,v in fresh_dict.items():
#     fresh_no_dup.append(k)
# #
# # rotten_dict= dict.fromkeys(fresh)
# # rotten_no_dup=[]
# # for k,v in rotten_dict.items():
# #     rotten_no_dup.append(k)
# #
# print(len(fresh_no_dup))

