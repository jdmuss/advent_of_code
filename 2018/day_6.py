import os
from numpy import where, zeros
#from itertools import repeat

test = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
#xt, yt = zip(*test)

res = {i:[] for i in test}
for x1, y1 in test:
    idx = test.index((x1,y1))
    for x2, y2 in (test[:idx]+test[(idx+1):]):
        res[(x1, y1)].append((abs(x2-x1)+1 + abs(y2-y1)+1))
    #res[(x1, y1)] = sum(res[(x1, y1)])


workPath = os.path.expanduser("~/Documents/Code/Advent_of_code")
os.chdir(workPath)

with open(os.path.join(workPath, "day6_input.txt"),  "r") as inFile:
    lines = [s.strip() for s in inFile]

x, y = zip(*[(int(c), int(r)) for c, r in [line.split(', ') for line in lines] ])
coords = list(zip(x, y))

minX = min(x)
maxX = max(x) + 1
minY = min(y)
maxY = max(y) + 1

left, right = -1, +1
up, down = -1, +1

neighbors = [(0, 1), (1, 0), (1, 2), (2, 1)]

field = zeros((maxY, maxX), dtype=int)
field[:minY, :] = -1
field[:, :minX] = -1

for i, (c, r) in enumerate(coords):
    field[r, c] = i + 1


stop = False
while not stop:
    fill = where(field == 0)
    if len(fill[0]) == 0:
        stop = True
    else:
        field_copy = field.copy()
        for r, c in zip(*fill):
            g = where(field[(r-1):(r+2), (c-1):(c+2)] > 0)
            fill_coords = [(i,j) for i, j in zip(g[0], g[1]) if (i,j) in neighbors]
            vals = set([field[r+fill_row-1, c+fill_col-1] for fill_row, fill_col in [fc for fc in fill_coords]])
            if len(vals) == 1:
                field_copy[r, c] = list(vals)[0]
            elif len(fill_coords) > 1:
                field_copy[r, c] = -1
        
        field = field_copy

field
# answer = 3401
# ignore (46, 188), (352, 115), (251, 67), (346, 348)
good_vals = [i+1 for i, c in enumerate(coords) if c not in [(46, 188), (352, 115), (251, 67), (346, 348)]]
bad_vals = set(list(field[:,minX]) + list(field[:,maxX-1]) + list(field[minY, :]) + list(field[maxY-1, :]))
good_vals = [v+1 for v in range(len(x)) if v not in bad_vals]

max([len(where(field==val)[0]) for val in good_vals])


#for r, c in zip(*where(field == 0)):
# Part 2:
from numpy import zeros_like
from itertools import product

def get_dist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

field = zeros((maxY, maxX), dtype=int)

for i, (c, r) in enumerate(coords):
    field[r, c] = i + 1

field = field[minY:, :]
field = field[:, minX:]

new_coords = where(field > 0)
new_coords = list(zip(new_coords[0], new_coords[1]))

results = zeros_like(field)
h, w = results.shape
for r, c in product(range(h),range(w)):
    results[r, c] = sum([get_dist((r,c), nc) for nc in new_coords])

t = where(results<10000)
len(t[0]) # = 49327

# A nice picture for good measure
import matplotlib.pyplot as plt

norm_color = results.copy()
norm_color[t] = 500

plt.imshow(norm_color)
plt.colorbar()
plt.show()

"""
aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
"""

from collections import defaultdict


#def d((x1,y1), (x2,y2)):
def d(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])


def closest(x,y):
    ds = [(d(p, (x,y)), p) for p in coords]
    ds.sort()
    if ds[0][0] < ds[1][0]:
        return ds[0][1]
    else:
        return (-1,-1)


def score_around(W):
    score = defaultdict(int)
    for x in range(minX-W, maxX+W):
        for y in range(minY-W, maxY+W):
            score[closest(x,y)] += 1
    return score


S2 = score_around(400)
S3 = score_around(600)


best = [(S2[k] if S2[k]==S3[k] else 0, k) for k in S2.keys()]
best.sort()
for area, p in best:
    print(area, p)


[517, 539, 655, 663, 698, 734, 808, 845, 856, 902, 1202, 1204, 1299, 1439, 1546, 1711, 1719, 1907, 1965, 2034, 2048,
2063, 2226, 2281, 2979, 3351, 3511, 3599, 4149, 5036]

# Another version of #1:
import numpy as np
from scipy.spatial import distance

# read the data using scipy
points = np.loadtxt('input.txt', delimiter=', ')

# build a grid of the appropriate size - note the -1 and +2 to ensure all points
# are within the grid
xmin, ymin = points.min(axis=0) - 1
xmax, ymax = points.max(axis=0) + 2

# and use mesgrid to build the target coordinates
xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

# happily scipy.spatial.distance has cityblock (or manhatten) distance out
# of the box
cityblock = distance.cdist(points, targets, metric='cityblock')
# the resulting array is an input points x target points array
# so get the index of the maximum along axis 0 to tie each target coordinate
# to closest ID
closest_origin = np.argmin(cityblock, axis=0)
# we need to filter out points with competing closest IDs though
min_distances = np.min(cityblock, axis=0)
competing_locations_filter = (cityblock == min_distances).sum(axis=0) > 1
# note, integers in numpy don't support NaN, so make the ID higher than
# the possible point ID
closest_origin[competing_locations_filter] = len(points) + 1
# and those points around the edge of the region for "infinite" regions
closest_origin = closest_origin.reshape(xgrid.shape)
infinite_ids = np.unique(np.vstack([
    closest_origin[0],
    closest_origin[-1],
    closest_origin[:, 0],
    closest_origin[:, -1]
]))
closest_origin[np.isin(closest_origin, infinite_ids)] = len(points) + 1

# and because we know the id of the "null" data is guaranteed to be last
# in the array (it's highest) we can index it out before getting the max
# region size
print(np.max(np.bincount(closest_origin.ravel())[:-1]))

# finally, make a pretty picture for good measure
import matplotlib.pyplot as plt
plt.imshow(np.where(closest_origin > len(points), np.NaN, closest_origin))
plt.colorbar()
plt.show()

