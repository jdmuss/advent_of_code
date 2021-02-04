import os
import re
from numpy import char
from onr_py.utils import path_expander

os.chdir(path_expander('~/Documents/Code/Advent_of_code/2020'))

with open('day_2_data.txt', 'r') as in_file:
    data = [re.split('[-: ]+', row) for row in in_file.readlines()]

good_pwd = 0

for (min_ct, max_ct, val, pwd) in data:
    present_ct = char.count(pwd.strip(), val)
    if int(min_ct) <= present_ct <= int(max_ct):
        good_pwd += 1

print(f"Part 1:the answer is {good_pwd}")

# Part 2: do this again, but for three numbers
good_pwd = 0

for (min_ct, max_ct, val, pwd) in data:
    matches = re.finditer(val, pwd)
    ok = 0
    for m in matches:
        if m.start() + 1 in (int(min_ct), int(max_ct)):
            ok += 1
    if ok == 1: good_pwd += 1    


print(f"Part 2:the answer is {good_pwd}")
