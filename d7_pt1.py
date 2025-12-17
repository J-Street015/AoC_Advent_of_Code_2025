data =[]
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))


for i in range(len(data[0])):
    if all(position[i] == "." for position in data):

       print(" ".join(position[i] for position in data)) # gives the columns where there are no carets



test_dat = [['a', 'e','d'], ['c', 'g', 'e']]


for line in test_dat:
    if "e" in line:
        print(line.index('e'))
        print(line.index('e') -1, line.index('e') +1)
        if len(line) == line.index("e") + 1:
            print(f'index out of range, {line}' )
