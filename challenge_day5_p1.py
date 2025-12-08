# this code works. dont touch
ranges = []
ids = []

with open("input_day5.txt") as f:
    for line in f.readlines():
        l = line.rstrip('\n')
        if "-" in l:
            # print(f"line: {l} is a range")
            ranges.append(l)
        else:
            # print(f'line: {l} is an ID')
            ids.append(l)

# turn string ids into integers

ids_int = [int(i) for i in ids]
# print(len(ranges))

# turn ranges into real ranges
list_of_ranges = []
for r in ranges:
    n1 = int(r.split("-")[0])
    n2 = int(r.split("-")[1])
    list_of_ranges.append([n1,n2])


# append item to fresh list if id is found in the range the numbers create.
fresh_list = []
for r in list_of_ranges:
    fresh_list.append([i for i in ids_int if i in range(r[0], r[1]+1)])
# print(fresh_list)


fresh_list_clean = []
for element in fresh_list:
    # print(element)
    for i in element:
        if len(element) > 0:
            fresh_list_clean.append(i)

#
fresh_dict= dict.fromkeys(fresh_list_clean)
fresh_no_dup=[]
for k,v in fresh_dict.items():
    fresh_no_dup.append(k)

print(len(fresh_no_dup))