import os
#import numpy as np
from tracktools.utils import pathExpander
from itertools import cycle

aocPath = pathExpander("~/Documents/Code/Advent_of_code")
os.path.cwd(aocPath)

with open(os.path.join(aocPath, "day_1_input.txt"),  "r") as inFile:
    freqs = [int(i.strip()) for i in inFile]

freqCircle = cycle(freqs)

cums = set()
idx = -1
cFreq = 0
stop = False
while not stop:
    idx += 1
    cFreq += next(freqCircle)
    if cFreq not in cums:
        cums.add(cFreq)
    else:
        shiftIdx = idx%len(freqs)
        print(f"{cFreq} is the first repeated frequency. As a bonus, it happened on the {idx}th step for (shiftIndex, shift)=({shiftIdx}, {freqs[shiftIdx]})")
        stop = True

