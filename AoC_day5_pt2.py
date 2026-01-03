# read input and add the number which contain a dash to the list of ranges.
ranges = []
with open("input_day5") as f:
    for line in f.readlines():
        l = line.rstrip('\n')
        if "-" in l:
            n1, n2 = int(l.split("-")[0]), int(l.split("-")[1])
            ranges.append([n1, n2])

# Compare intervals in the list of ranges
# returns a list with new ranges, which are merged.
# code based on the tutorial from https://blog.seancoughlin.me/mastering-the-merging-of-overlapping-intervals-in-python

def merge(intervals):
    if not intervals:
        return []
    # Sort the intervals based on the starting points
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]
        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval to the merged list
            merged_intervals.append(current)
    return merged_intervals


merged_ranges = merge(ranges)

count = 0
for i in merged_ranges:
    if len(range(i[0], i[1] + 1)) > 0:
        count += len(range(i[0], i[1] + 1))

print(count)
