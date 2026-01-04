# AoC day9 part 1. Code works.
import pandas as pd
import numpy as np

dat = pd.read_csv('d9_input', sep=",", header=None, index_col=False)
points = np.array(dat)

def largest_square(points):
    squares = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            a = abs(int(points[i][0] - points[j][0]))
            b = abs(int(points[i][1] - points[j][1]))

            area = (a + 1) * (b + 1)
            squares.append(area)
    return max(squares)


print(largest_square(points))
