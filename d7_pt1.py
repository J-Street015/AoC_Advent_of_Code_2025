data = []
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

# get the start position:
start_pos = [data[0].index("S")]

split_pos = start_pos # set the start position as the first split position
test = []
split_count = 0
for line in data:
    split_pos = []
    indices = [i for i, x in enumerate(line) if x == "^"] # records all instances of caret in line and their indices.
    print(f'splitter postions {indices}')
    # temp = []
    for i in indices:
        print(f"splitter sits at pos: {i}")
        if i in indices:
            split_count += 1
            lower = i -1
            higher = i +1
            split_pos.append(lower)
            print(f'beam goes to position {lower}, {higher}')
            split_pos.append(higher)
            print(f'split count: {split_count}')
    #         temp.append(lower)
    #         temp.append(higher)
    # if len(temp) > 0:
    #     test.append(set(temp))
            # try create a set of the numbers

# print(split_pos)
print(test)
print(split_count)



