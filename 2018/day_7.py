import os
#from numpy import where, zeros
import re
#from itertools import repeat

def build_depend_dict(data):
    depend_dict = {}
    for (i, d) in data:
        if d in depend_dict:
            depend_dict[d].append(i)
        else:
            depend_dict[d] = [i]
    return depend_dict

findRoutes = re.compile(r'((?<=\s)[A-Z](?=\s))')

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code")
os.chdir(workPath)

with open(os.path.join(workPath, "day_7_input.txt"),  "r") as inFile:
    lines = [findRoutes.findall(s.strip()) for s in inFile]

line_dict = {}
for (i, d) in lines:
    if i in line_dict:
        line_dict[i].append(d)
    else:
        line_dict[i] = [d]

for k, v in line_dict.items():
    line_dict[k] = sorted(v)

depend_dict = build_depend_dict(lines)

independant, dependant = zip(*lines)
independant = sorted(set(independant))
dependant = sorted(set(dependant))
numTasks = len(set(independant + dependant))

#vals = sorted(set([i for i in independant if i not in dependant]))
#vals += sorted([i for i in independant if i not in vals])
#vals += sorted([d for d in dependant if d not in independant])
#vals = iter(vals)

vals = sorted(set([i for i in independant if i not in dependant]))
# ['G', 'M', 'W', 'Z']

result = ''
while len(vals) > 0:
    next_val = vals[0]
    result += next_val
    vals = vals[1:]
    if next_val in line_dict:
        for p in line_dict[next_val]:
            if p in depend_dict:
                depend_dict[p].remove(next_val)
                if len(depend_dict[p]) == 0:
                    vals += [p]
        vals = sorted(set(vals))

# Answer = GLMVWXZDKOUCEJRHFAPITSBQNY

# Part 2: 1105
speed = 60
num_workers = 5
numTasks = len(set(independant + dependant))

task_duration = lambda c : 60 + ord(c.lower()) - 96

depend_dict = build_depend_dict(lines)
vals = sorted(set([i for i in independant if i not in dependant]))

workers = {w:0 for w in range(num_workers)}
worker_pool = list(workers.keys())
task_in_process = {}

result = ''
clock = 0
while len(result) < numTasks:
    # working
    try:
        time_worked = min([v for v in workers.values() if v > 0])
    except:
        time_worked = 0
    clock += time_worked
    
    for w in set(workers.keys()).difference(set(worker_pool)):
        workers[w] -= time_worked
        if workers[w] <= 0:
            worker_pool.append(w)
            finished_task = task_in_process[w]
            result += finished_task
            if finished_task in line_dict:
                for p in line_dict[finished_task]:
                    if p in depend_dict:
                        depend_dict[p].remove(finished_task)
                        if len(depend_dict[p]) == 0:
                            vals += [p]
                vals = sorted(set(vals))
    
    while len(worker_pool) > 0 and len(vals) > 0:
        # Assign work
        next_val = vals[0]
        vals = vals[1:]
        elf = worker_pool.pop()
        workers[elf] = task_duration(next_val)
        task_in_process[elf] = next_val

