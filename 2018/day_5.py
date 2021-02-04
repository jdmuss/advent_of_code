import os,  string
#import numpy as np
from tracktools.utils import pathExpander
from itertools import chain
import re

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

reactivePairs = [''.join([i,j]) for i, j in chain(zip(lowercase, uppercase), zip(uppercase, lowercase))]

polyRe = re.compile(r'([a-z]([A-Z]))+|([A-Z]([a-z]))+')
repeatsRE = re.compile(r"\a(?=\a)")
tst = re.compile(r'[a-z]*([a-z])\1([a-z])\2[a-z]*')

aocPath = pathExpander("~/Documents/Code/Advent_of_code")
os.path.cwd(aocPath)

with open(os.path.join(aocPath, "day_5_input.txt"),  "r") as inFile:
    poly = inFile.readlines()


poly = poly[0].strip()

result = [m.group() for m in polyRe.finditer(poly)]

def removePolys(pStr):
    finished = False
    while not finished:
        for p in reactivePairs:
            pStr = pStr.replace(p, '')
        if len([i for i in reactivePairs if pStr.find(i) > -1]) == 0:
            finished = True
    
    return pStr


def find_shortest(pStr):
    shortest = len(pStr)
    badPoly = None
    bestPoly = None
    for l, u in zip(lowercase, uppercase):
        newPoly = pStr.replace(l, '')
        newPoly = newPoly.replace(u, '')
        newPoly = removePolys(newPoly)
        if len(newPoly) < shortest:
            shortest = len(newPoly)
            badPoly = f"{l}/{u}"
            bestPoly = newPoly
    
    return (shortest, badPoly, bestPoly)


r = find_shortest(poly)

"""def removePolys(pStr):
    finished = False
    while not finished:
        print(len(pStr))
        foundPolys = [m.group() for m in polyRe.finditer(pStr) if len(m.group()) == 2]
        for p in foundPolys:
            pStr = pStr.replace(p, '')
        if len(polyRe.findall(pStr)) == 0:
            finished = True
    
    return pStr

"""
