data =[]
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))


# for i in range(len(data)):
#     if all(problem[i] == '.' for problem in data):
#         print(f"here is a dot: {i}")


# print(data)


for i in range(len(data[0])):
    if all(position[i] == "." for position in data):

       print(" ".join(position[i] for position in data)) # gives the columns where there are no carets



