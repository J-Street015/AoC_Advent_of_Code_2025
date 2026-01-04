# AoC day9 part 2. Help from Yordi at https://github.com/Froodooo/aoc/blob/main/aoc25/9.py
import pandas as pd
import numpy as np

dat = pd.read_csv('d9_input', sep=",", header=None, index_col=False)
points = np.array(dat)



from typing import List
from shapely.geometry import Polygon


def area_size(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def poly_rectangle_area(x1: int, y1: int, x2: int, y2: int) -> Polygon:
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    return Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])



def part_two(data: List[str]) -> int:
    largest = 0
    poly_area = Polygon(data)
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            rectangle = poly_rectangle_area(x1, y1, x2, y2)
            if rectangle.within(poly_area):
                area = area_size(x1, y1, x2, y2)
                if area > largest:
                    largest = area
    return largest

print(part_two(points))

