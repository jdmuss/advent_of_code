import os
import re
#from numpy import product
from onr_py.utils import path_expander

os.chdir(path_expander('~/Documents/Code/Advent_of_code/2020'))

required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
optional_key = 'cid'

with open('day_4_data.txt', 'r') as in_file:
    data = [row.strip().split() for row in in_file.readlines()]

passports = []
new_record = []
for row in data:
    if row:
        new_record += row
    else:
        passports.append(dict(r.split(':') for r in new_record))
        new_record = []

if new_record not in passports : passports.append(dict(r.split(':') for r in new_record))
# Part 1:
valid_passports = 0
for p in passports:
    if not required_keys.difference(p.keys()):
        valid_passports += 1

print(f"Part 1:there are {valid_passports} valid passports")

# Part 2: Verify fields meet requirements
requirements = {'byr':'^19[2-9][0-9]|200[0-2]',
                'iyr':'^201[0-9]|2020',
                'eyr':'^202[0-9]|2030',
                'hgt':'^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in',
                'hcl':'^#[a-f0-9]*$',
                'ecl':'amb|blu|brn|gry|grn|hzl|oth',
                'pid':'^[0-9]{9}$'
               }

valid_passports = 0
for p in passports:
    if not required_keys.difference(p.keys()):
        good = 0
        for fld in required_keys:
            if re.match(requirements[fld], p[fld]):
                good += 1
        if good == 7 : valid_passports += 1


print(f"Part 2:there are {valid_passports} valid passports")
