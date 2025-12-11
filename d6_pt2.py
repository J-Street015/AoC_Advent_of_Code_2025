# Code is maybe not good looking but it works.
import array

import pandas as pd
import array
dat = pd.read_csv("d6_test", sep='\s+', header= None)

df = pd.DataFrame(dat)

# print(len(df.columns))
test_list = []
for i in range(len(df.columns)):
    for l in range(len(df)):
        num_string = df[i][l]
        sub_list = []
        for d in num_string:


            sub_list.append(d)
            # print(sub_list)
            test_list.append(sub_list)
print(test_list)


