
import math
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
import heapq # For efficient top-N selection


dat = pd.read_csv('d8_full', sep=",", header=None, index_col=False)
dat = dat.rename(columns={0:"X", 1:"Y", 2:"Z"})


# Array of points (each row is a 3D point)
points_array_dat = np.array(dat)
# Sample 3D Coordinates (N points)

points = points_array_dat

# 1. Calculate all pairwise distances
# pdist gives a condensed distance matrix (upper triangle)
condensed_distances = pdist(points)
# 2. Squareform converts to a full matrix (optional, but useful for indexing)
dist_matrix = squareform(condensed_distances)

# 3. Create a list of (distance, point1_index, point2_index) tuples
# We iterate through the upper triangle of the matrix to avoid duplicates and self-distances (0)
all_pairs = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        all_pairs.append((dist_matrix[i, j], i, j))

# 4. Find the N smallest distances using heapq.nsmallest
N = 1000 # Number of shortest distances to find here it was set to 1000 since this is the number of all junction boxes
shortest_n = heapq.nsmallest(N, all_pairs, key=lambda x: x[0])

# 5. Format the output
results = []
for dist, i, j in shortest_n:
    results.append({
        # 'distance': float(dist),
        # 'point1': points[i].tolist(), # Convert numpy array to list
        # 'point2': points[j].tolist(),
        'indices': (i, j) # only keep the indices for each position
    })

# print(f"Top {N} shortest distances:\n", results)

indices= []
for i in results:
    # print(i["indices"])
    indices.append(list(i['indices']))
# print(indices) # use for test data only

pooled = [set(subList) for subList in indices]
merging = True
while merging:
    merging=False
    for i,group in enumerate(pooled):
        merged = next((g for g in pooled[i+1:] if g.intersection(group)),None)
        if not merged: continue
        group.update(merged)
        pooled.remove(merged)
        merging = True

number_list= set()
for p in pooled:
    number_list.add(len(p))

sorted_numbers = sorted(number_list, reverse=True)

print(math.prod(sorted_numbers[:3]))


















