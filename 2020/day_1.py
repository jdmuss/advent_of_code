import os
from numpy import array, argwhere, product, squeeze
from onr_py.utils import path_expander
from copy import deepcopy

os.chdir(path_expander('~/Documents/Code/Advent_of_code/2020'))

with open('day_1-1_data.txt', 'r') as in_file:
    original_data = [int(row.strip()) for row in in_file.readlines()]

data = deepcopy(original_data)
result = ()

while not result:
    val_1 = data.pop()
    match = squeeze(argwhere(val_1 + array(data) == 2020))
    if match:
        result = (val_1, data[match])


print(f"The answer is {product(result)}")

# Part 2: do this again, but for three numbers
data = deepcopy(original_data)
result = ()


while not result:
    val_1 = data.pop()
    data_2 = deepcopy(data)
    while not result and data_2:
        val_2 = data_2.pop()
        match = squeeze(argwhere(val_1 + val_2 + array(data_2) == 2020))
        if match:
            result = (val_1, val_2, data_2[match])


print(f"The answer is {product(result)}")
