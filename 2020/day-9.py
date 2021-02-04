import os
from numpy import array, cumsum, nditer, roll, setdiff1d, where

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code/2020")
os.chdir(workPath)

with open("day-9_data.txt",  "r") as in_file:
    data = array([int(row.strip()) for row in in_file])

# Part 1:
num_rows = len(data)
preamble_length = 25

end_idx = preamble_length
preamble = data[:end_idx]
found = False
while not found and end_idx < num_rows:
    possibles = setdiff1d(preamble[preamble < data[end_idx]], data[end_idx]/2)
    remainder = set(data[end_idx] - possibles)
    if remainder.intersection(possibles):
        preamble = roll(preamble, shift=-1)
        preamble[-1] = data[end_idx]
        end_idx += 1
    else:
        found = True
        
bad_val = data[end_idx]
print(f"The first number that doesn't satisfy XMAS is {bad_val}")
# Part 2:
def get_weakness(val, dat):
    end, = where(cumsum(dat) == val)
    if end:
        end = end[0] + 1
        return dat[:end].min() + dat[:end].max()


possible_idx, = where(data < bad_val)
possible_idx = nditer(possible_idx)
found = False
while not found:
    idx = next(possible_idx)
    encryption_weakness = get_weakness(bad_val, data[idx:])
    if encryption_weakness:
        found = True

print(f"The XMAS encryption weakness is {encryption_weakness}")
