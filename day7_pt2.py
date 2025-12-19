# read in the data
from unittest.mock import right

data = []
with open("d7_input") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))


# define start position
beam_pos = set([i for i, x in enumerate(data[0]) if x == "S"]) # set the start position as the first split position
test = []
split_count = 0
for line in data:
    idxs = [i for i, x in enumerate(line) if x == "^"] # records all instances of caret in line and their indices.
    beam_pos = list(set(beam_pos)) # convert beam position to set to avoid duplicates in case the beam splits into same postion
    temp = []

    # go through all positions of the splitter and check if splitter is at the beam position
    for i in idxs:
        if i in beam_pos:
            split_count += 1 # update split if a splitter is in beam position
            left_idx = i -1 #get left beam
            right_idx = i +1 #get right beam
            beam_pos.append(left_idx)
            beam_pos.append(right_idx)
            beam_pos.pop(beam_pos.index(i))

            temp.append(left_idx)
            temp.append(right_idx)
    if len(temp) > 0:
        test.append(temp)
# print(split_count)
print(test)


test_count = 0
for i  in test:
    print(len(i))
    test_count += len(i)

print(test_count)
