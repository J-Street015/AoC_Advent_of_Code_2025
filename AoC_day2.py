# Script for challenge day 2 part 1 and part2. Code works.

ids = []
with open("input_day2.txt") as f:
    ids.append(f.readlines())

id_ranges = ids[0][0]
result = id_ranges.split(",")


num_list_part1 = []

for i in result:
    split_range= i.split("-")
    first_number: int = int(split_range[0])
    second_number= int(split_range[1])
    test = (range(first_number, second_number + 1))
    # Solution for the first part of the challenge. My idea to divide the strings into two halfs if possible, then compare the
    # first and second part, if they match you got a hit. Help by stack overflow
    for i in test:
        firstpart, secondpart = str(i)[:len(str(i)) // 2], str(i)[len(str(i)) // 2:]
        if firstpart == secondpart:
            num_list_part1.append(int(firstpart + secondpart))
print(sum(num_list_part1))

# This is the solution for the second part of the challenge, and uses string concatenation and starts searching
# from the second character in the doubled string, to see if the substring is still found. Ingenious but not my idea,
# GeeksForGeeks https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/
num_list_part2 = []
for i in result:
    split_range = i.split("-")
    first_number: int = int(split_range[0])
    second_number = int(split_range[1])
    test = (range(first_number, second_number + 1))
    # Solution for the first part of the challenge. My idea to divide the strings into two halfs if possible, then compare the
    # first and second part, if they match you got a hit. Help by stack overflow
    for t in test:
        # Check for repeating pattern using string concatenation
        res = (str(t) + str(t)).find(str(t), 1) != len(str(t))
        if res:
            num_list_part2.append(int(t))

print(sum(num_list_part2))