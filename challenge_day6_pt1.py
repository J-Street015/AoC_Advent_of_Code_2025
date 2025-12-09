dat = []
with open("d6_test") as f:
    line = f.readlines()
    for l in line:
        l_split = l.rstrip("\n").split("\t")
        dat.append(l_split)



with open('d6_test','r') as f:
    test=[x.strip().split('\t') for x in f]


import csv
list_of_elements = []
with open("d6_test", 'r') as f:
    for i in csv.reader(f, delimiter=" "):
        list_of_elements.append(i)

test_list2 = []
for i in list_of_elements:
    i = [x for x in i if x]
    test_list2.append(i)


for list in test_list2:
    for l in list:
        print(list[list.index(l)])
