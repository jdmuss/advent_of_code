import os
from numpy import product
from onr_py.utils import path_expander

os.chdir(path_expander('~/Documents/Code/Advent_of_code/2020'))

with open('day_3_data.txt', 'r') as in_file:
    data = [row.strip() for row in in_file.readlines()]

# Part 1:
right = 3
down = 1
wrap = len(data[0])


def ride(right, down, map):
    trees = 0
    right_idx = 0
    for row_idx in range(1, len(map), down):
        right_idx = (right_idx + right) % wrap
        if map[row_idx][right_idx] == '#': trees += 1
    return trees


print(f"Part 1:the tobbogan hit {ride(right, down, data)} trees")

# Part 2: do this again, but for three numbers
# Part 2: do this again, but for five different slopes
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []

for i, (right, down) in enumerate(slopes):
    trees.append(ride(right, down, data))


print(f"Part 2:the answer is {product(trees)}")
