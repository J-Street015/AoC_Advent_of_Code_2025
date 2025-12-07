import scipy
import numpy
import scipy

grid_list = []

# read input and each line becomes a list so it can be turned into an array.
with open("input_day4.txt") as f:
    for line in f:
        print(line.rstrip("\n"))
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

boundaries = numpy.array(new_list) # creates the array
# for each number 1 at each position, the surrounding 1s are counted. Max can be 9 including the current position.
counts = scipy.signal.convolve2d(boundaries, numpy.ones((3,3)), mode="same")
c = numpy.zeros_like(counts) # creates a third array to be used as a container.
c[(boundaries > 0) & (counts<5)] = 1 # condition which iterates over the boundary array and checks were a paper
# roll was sitting indicated by 1. or bigger 0, if true, and counts are 4 (3+1 since the instance from where the count
# is done goes into the number), then add a 1. this leaves only 1s at the position with paper roll and adjacent elements
# less than 4.
#  print the sum of the paper rolls which can be removed.
print(sum(c[c ==1]))

