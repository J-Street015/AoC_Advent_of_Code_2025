import numpy
import scipy

grid_list = []

# read input and each line becomes a list so it can be turned into an array.
with open("input_day4.txt") as f:
    for line in f:
        grid_list.append(list(line.rstrip("\n")))


# replace the placeholder and @ Paper roll with 0, 1 for array calculation.
new_list = []
new_element = []
for element in grid_list:
    for i in element:
        if i == ".":
            i = 0
            new_element.append(i)
        elif i == "@":
            i = 1
            new_element.append(i)
    new_list.append(new_element)
    new_element=[]

boundaries = numpy.array(new_list)
len_element= 0
row_nums= 0
for i in boundaries:
    len_element= len(i)
    row_nums +=1

# get the total number of elements in array
number_of_all_elements = (len_element * row_nums)

total_count= [] # empty list to store the count from every round
roll_count = (len_element * row_nums) # adds the max number of elements which can be removed from the array
while roll_count > 0: # while loop to keep track of the count from each repetition.
    # If 0, this means no more elements can be removed
    counts = scipy.signal.convolve2d(boundaries, numpy.ones((3,3)), mode="same")
    # print(counts)
    c = numpy.zeros_like(counts)
    c[(boundaries > 0) & (counts<5)] = 1
    # print(c)
    roll_count = sum(c[c ==1])
    boundaries[(boundaries ==1) & (c==1) ] = 0
    total_count.append(roll_count)
print(sum(total_count))


