data =[]
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

#
# for i in range(len(data[0])):
#     if all(position[i] == "." for position in data):
#
#        print(" ".join(position[i] for position in data)) # gives the columns where there are no carets
#

start_pos = int()
# find the starting position
for line in data:
    if "S" in line:
        start_pos = line.index("S")

print(start_pos)

for line in data:
    if "^" in line[start_pos]:
        print(f"first split at: {data.index(line)}")
        # try to get the upstream and downstream positions of where the split happens.
        # temp_pos = [position for position in line if "^" in line[start_pos]]
        # print(temp_pos)
        print(start_pos -1, start_pos +1)





