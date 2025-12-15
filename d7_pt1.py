data =[]
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))


for i in range(len(data[0])):
    if all(position[i] == "." for position in data):

       print(" ".join(position[i] for position in data)) # gives the columns where there are no carets



test_dat = ["a", "b", "c"]

for line in data:
    for i in range(len(line)):
        print(line[i])
        if line[i] == "^":
            print(line.index(line[i -1]), line.index(line[i +1]))

