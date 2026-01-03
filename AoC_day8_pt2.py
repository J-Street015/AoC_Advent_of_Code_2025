# AoC day8 part2
# used help from https://yordi.me/advent-of-code-2025-day-8/
# for part2

import math
import pandas as pd
import numpy as np


dat = pd.read_csv('d8_full', sep=",", header=None, index_col=False)
dat = dat.rename(columns={0:"X", 1:"Y", 2:"Z"})

# Array of points (each row is a 3D point)
points = np.array(dat)

distances = []

for i in range(len(points)):
    # print("index:", i, points[i])
    for j in range(i+1, len(points)):
        p1, p2 = points[i], points[j]
        d = math.dist(p1,p2)
        distances.append(((i,j), d))

sorted_dist = sorted(distances, key=lambda x: x[1]) # sorts the list of tuples by the distance but keeps the

def init_circuits(num_points):
    return [{i} for i in range(num_points)]

circuits = init_circuits(len(points))


def connect(circuits, p1, p2):
    set1 = set2 = None
    for s in circuits:
        if p1 in s:
            set1 = s
        if p2 in s:
            set2 = s
    if set1 is not set2:
        set1.update(set2)
        circuits.remove(set2)

for i in range(1000):
    ((p1, p2), _) = sorted_dist[i]
    connect(circuits, p1, p2)

circuits = sorted(circuits, key=lambda x: len(x), reverse=True)



def get_max_circuit(points):
    distances = sorted_dist
    circuits = init_circuits(len(points))
    i = 0
    p1 = p2 = -1
    while len(circuits) != 1:
        ((p1, p2), _) = distances[i]
        connect(circuits, p1, p2)
        i += 1
    return points[p1][0] * points[p2][0]

print(get_max_circuit(points))