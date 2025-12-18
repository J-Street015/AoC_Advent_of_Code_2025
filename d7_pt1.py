data = []
with open("d7_input") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))



# get the start position:
start_pos = [data[0].index("S")]

split_pos = start_pos # set the start position as the first split position
test = []
split_count = 0
for line in data:
    indices = [i for i, x in enumerate(line) if x == "^"] # records all instances of caret in line and their indices.
    print(indices)
    temp = []

    for i in indices:
        if i in split_pos:
            split_count += 1
            lower = i -1
            higher = i +1
            split_pos.append(lower)
            split_pos.append(higher)
            temp.append(lower)
            temp.append(higher)
    if len(temp) > 0:
        test.append(set(temp))
            # try create a set of the numbers

# print(split_pos)
print(test)
print(split_count)



