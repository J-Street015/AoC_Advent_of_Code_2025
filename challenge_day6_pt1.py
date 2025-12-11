# Code is maybe not good looking but it works.

import pandas as pd

dat = pd.read_csv("d6_input", sep='\s+',header=None)

dat = pd.DataFrame(dat)

num = 0
num_sum = []
for i in dat:
    # print(dat[i]) # prints columns 1 by 1
    test = []
    for i in dat[i]:
        test.append(i)
        if "+" in test:
            test.pop(len(test) -1)
            for i in test:
                num += int(i)
            num_sum.append(num)
            num = 0

        elif "*" in test:
            test.pop(len(test) -1)
            num = num +1
            for i in test:
                num *= int(i)
            num_sum.append(num)
            num = 0
print(sum(num_sum))

