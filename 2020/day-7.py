import os
import re

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code/2020")
os.chdir(workPath)

with open("day-7_input.txt",  "r") as in_file:
    data = [row.strip()[:-1] for row in in_file]

packing_rules = [re.split(' bag[s ] contain[s ]| bag[s ,]', rule)[:-1] for rule in data]
# Part 1:
contains = re.compile(' bag[s ] contain[s ]| bag[s ,]*')

color = 'shiny gold'
contains_gold = [contains.split(rule)[0] for rule in data if color in rule and not rule.startswith(color)]

bags = ['shiny gold']
answer = []
while bags:
    color = bags.pop()
    answer.append(color)
    bags = [contains.split(rule)[0] for rule in data if color in rule and not rule.startswith(color)] + bags

print(f"The number of bags that can contain shiny gold is {len(set(answer)) - 1}")
# Part 2:
# Answer: 5*17 + 4*4710 = 18925
def get_rule(color, rules):
    return [rule for rule in rules if color in rule and rule.startswith(color)][0]


def get_bag(color, rules):
    contents = 1
    bags = [contains.split(r) for r in rules if r.startswith(color)][0][:-1]
    if bags[-1] == 'no other':
        return contents
    else:
        for bag in bags[1:]:
            ct, *color = re.findall('\d+|[\w]+', bag)
            contents += int(ct)*get_bag(' '.join(color), rules)
        return contents


def get_contents(color, rules):
    bags = [contains.split(r)[:-1] for r in rules if r.startswith(color)][0][1:]
    cont = dict()
    if bags[-1] == 'no other':
        return {color:0}
    else:
        for bag in bags:
            ct, *col = re.findall('\d+|[\w]+', bag)
            col = ' '.join(col)
            cont[color] = int(ct)
        return {color:cont}


def bag_list(color, rules):
    contents = []
    bags = [contains.split(r)[:-1] for r in rules if r.startswith(color)][0]
    if bags[-1] == 'no other':
        return [bags[0], 0]
    else:
        for bag in bags[1:]:
            ct, *color = re.findall('\d+|[\w]+', bag)
            color = ' '.join(color)
            contents += [int(ct), color, bag_list(color, rules)]
        return contents


color = 'shiny gold'

shiny_gold = get_bag(color, data)
print(f"A shiny gold bag must contain {get_bag('shiny gold', data) - 1} bags")

