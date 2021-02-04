import os
from itertools import product
import re
from numpy import append, array, bincount, diff, sort #cumsum, nditer, roll, setdiff1d, where
from numpy import product as np_prod

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code/2020")
os.chdir(workPath)

with open("day-10_data.txt",  "r") as in_file:
    data = array([int(row.strip()) for row in in_file])

# Part 1:
sorted_adapters = sort(data)
sorted_adapters = append(append(array([0]), sorted_adapters), sorted_adapters[-1]+3)
jolts = diff(sorted_adapters)

distribution  = {k:v for k, v in zip(range(max(set(jolts))+4), bincount(jolts))}
print(f"The product of the counts of 1- and 3-jolt differences is {distribution[1]*distribution[3]}")
# Part 2:
def possible_permutations(n, m):
    perms = (i for i in product(list(range(m + 1)), repeat=n) if sum(i) == n)
    return set(tuple(n for n in sublist if n != 0) for sublist in perms)


max_step = 3
reps = re.findall('1{2,}', ''.join([str(i) for i in jolts]))
rep_lens = [len(i) for i in reps]

perm_dict = {s:len(possible_permutations(s, max_step)) for s in range(2, max(rep_lens) + 1)}
counts = np_prod([perm_dict[possibilities] for possibilities in rep_lens])
print(f"There are {counts} possible permutations of the adapters")

