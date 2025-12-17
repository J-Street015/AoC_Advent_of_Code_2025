data = []
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

# for i in range(len(data[0])):
#     if all(position[i] == "." for position in data):
#         print(" ".join(position[i] for position in data)) # gives the columns where there are no carets


# test_dat = [['a', 'e', 'd'], ['c', 'g', 'e']]
#
# test = ["a", "b", "c"]
#
# for line in test_dat:
#     print(line)
#     for t in test:
#         if t in line:
#             print("found it")





# get the start position:
start_pos = [data[0].index("S")]

split_pos = start_pos # set the start position as the first split position
test = []

for line in data:
    indices = [i for i, x in enumerate(line) if x == "^"] # records all instances of caret in line and their indices.
    print(indices)
    temp = []
    for i in indices:
        if i in split_pos:
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




        # if line.index("^") in start_pos: # Perhaps not so smart since that will always check if the ^ is at the start position
            # print(f'first split at line {line}')


            # pos1 = 0
            # lower = line.index('^') - 1
            # upper = line.index('^') + 1
            # start_pos = [lower, upper]
            # print(start_pos)

        # print(line.index('^'))
        # print(line.index('^') -1, line.index('^') +1)
        # if len(line) == line.index("^") + 1:
        #     print(f'index out of range, {line}' )


# for line in test_dat:
#     print(line)
#     indices = [i for i, x in enumerate(line) if x == "e"]
#
#     print(indices)
