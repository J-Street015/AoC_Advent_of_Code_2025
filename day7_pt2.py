# read in the data


data = []
with open("d7_test") as f:
    for line in f.readlines():
        data.append(line.rstrip("\n"))

position_map = []

# define start position
beam_pos = set([i for i, x in enumerate(data[0]) if x == "S"]) # set the start position as the first split position

split_count = 0
for line in data:
    idxs = [i for i, x in enumerate(line) if x == "^"] # records all instances of caret in line and their indices.
    beam_pos = list(beam_pos) # convert beam position to set to avoid duplicates in case the beam splits into same postion
    position_map.append(sorted(beam_pos))

    # go through all positions of the splitter and check if splitter is at the beam position
    for i in idxs:
        if i in beam_pos:
            # split_count += 1 # update split if a splitter is in beam position
            idx = i -1  # left beam
            right_idx = i +1 #right beam
            beam_pos.append(idx)
            beam_pos.append(right_idx)
            beam_pos.pop(beam_pos.index(i))

import itertools
# position_map.sort()
cleaned_pos = list(k for k,_ in itertools.groupby(position_map))

for i in cleaned_pos:
    print(i)

