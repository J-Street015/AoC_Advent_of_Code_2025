data =[]
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))


for i in range(len(data[0])):
    if all(position[i] == "." for position in data):

       print(" ".join(position[i] for position in data)) # gives the columns where there are no carets



test_dat = [['a', 'e','d'], ['c', 'g', 'e']]


# get the start position:
start_pos = [data[0].index("S")]

print(start_pos)


split_pos = [start_pos]

for line in data:
    if "^" in line:
        if line.index("^") in start_pos:
            print(f'first split at line {line}')
            lower = line.index('^') -1
            upper = line.index('^') + 1
            start_pos = [lower, upper]
            print(start_pos)




        # print(line.index('^'))
        # print(line.index('^') -1, line.index('^') +1)
        # if len(line) == line.index("^") + 1:
        #     print(f'index out of range, {line}' )


