import os
import re
from numpy import array, in1d, ma, where, zeros

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code/2020")
os.chdir(workPath)

arg = re.compile('[+-]|\d+')

with open("day-8_data.txt",  "r") as in_file:
    instructions = [[inst[0]] + arg.findall(inst[-1]) for inst in [row.strip().split() for row in in_file]]

# Part 1:
lines = zeros(len(instructions))
acc = 0
line_num = 0

while lines[line_num] == 0:
    lines[line_num] += 1
    inst, dir, val = instructions[line_num]
    if inst == 'jmp':
        exec(f"line_num {dir}= {val}")
    elif inst == 'acc':
        exec(f"acc {dir}= {val}")
        line_num += 1
    elif inst == 'nop':
        line_num += 1
        

print(f"The accumulator value at the infinite loop is {acc}")
# Part 2:
flip_op = {'nop':'jmp', 'jmp':'nop'}

last_instruction = len(instructions)
jmp_nop = in1d(array(instructions)[:,0], ('nop', 'jmp'))
visited = ma.masked_greater(lines, 0).mask
to_test, = sorted(where(jmp_nop & visited).tolist(), reverse=True)
to_test = sorted(to_test, reverse=True)

line_num = 0

while to_test and line_num < last_instruction:
    lines = zeros(len(instructions))
    acc = 0
    line_num = 0
    idx = to_test.pop()
    instructions[idx][0] = flip_op[instructions[idx][0]]
    while lines[line_num] == 0 and line_num < last_instruction:
        lines[line_num] += 1
        inst, dir, val = instructions[line_num]
        if inst == 'jmp':
            exec(f"line_num {dir}= {val}")
        elif inst == 'acc':
            exec(f"acc {dir}= {val}")
            line_num += 1
        elif inst == 'nop':
            line_num += 1
    if line_num < last_instruction:
        instructions[idx][0] = flip_op[instructions[idx][0]]

print(f"The correct accumulator value is {acc}")
