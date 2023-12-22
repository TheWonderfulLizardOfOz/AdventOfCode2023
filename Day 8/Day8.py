import re
import numpy as np
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def day8p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    directions = lines[0]
    points = {}
    for i in range(2, len(lines)):
        line = re.findall(r'(.*)(=) \((.*),(.*)\)', lines[i])
        points[line[0][0].strip()] = (line[0][2], line[0][3].strip())

    current = 'AAA'
    stepCount = 0
    found = False
    while not found:
        for d in directions:
            stepCount += 1
            if d == 'L':
                current = points[current][0]
            else:
                current = points[current][1]
            if current == 'ZZZ':
                found = True
                break

    return stepCount


def day8p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    directions = lines[0]
    points = {}
    aLocs = {}
    for i in range(2, len(lines)):
        line = re.findall(r'(.*)(=) \((.*),(.*)\)', lines[i])
        points[line[0][0].strip()] = (line[0][2], line[0][3].strip())
        if line[0][0][2] == 'A':
            aLocs[line[0][0].strip()] = line[0][0].strip()

    zSteps = []
    for loc in aLocs:
        current = loc
        stepCount = 0
        found = False
        while not found:
            for d in directions:
                stepCount += 1
                if d == 'L':
                    current = points[current][0]
                else:
                    current = points[current][1]

                if current[2] == 'Z':
                    print(loc, current, stepCount)
                    zSteps.append(stepCount)
                    found = True
                    break

    x = zSteps[0]
    for i in range(1, len(zSteps)):
        x = lcm(x, zSteps[i])
    return x


print(day8p2())
