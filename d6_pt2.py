# Code is maybe not good looking but it works.
import array

import pandas as pd
import array
dat = pd.read_csv("d6_test", sep='\s+', header= None)

df = pd.DataFrame(dat)

############## Keep and dont touch for now ###################
# print(len(df.columns))
# test_list = []
# for i in range(len(df.columns)):
#     for l in range(len(df)):
#         num_string = df[i][l]
#         sub_list = []
#         for d in num_string:
#
#
#             sub_list.append(d)
#             # print(sub_list)
#         test_list.append(sub_list)
# print(test_list)
#
# print(pd.DataFrame(test_list))

############## Keep and dont touch for now ###################


# # iterate over rows
# for i, row in df.iterrows():
#     print(i, row)
#     print()

# print(df[0])

# Iterate over columns:

for label, value in df.items():
    # print(value)
    top_list = []
    for element in value:
        new_list = []
        top_list.append(new_list)
        for i in element:
            new_list.append(i)

        # print(new_list)
    # print(top_list)
    for i in top_list:
        print(i)
