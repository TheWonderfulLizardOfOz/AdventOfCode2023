import re
import numpy as np
import math
import time

cubeRocks = set()
roundRocksLocs = set()
roundRocks = []
newRoundRocks = []
rowNum = 0
colNum = 0


def findDestination(roundRock):
    row, col = roundRock
    for i in range(row, -1, -1):
        if (i - 1, col) in cubeRocks:
            cubeRocks.add((i, col))
            return rowNum - i


def north(roundRock):
    row, col = roundRock
    for i in range(row, -1, -1):
        if (i - 1, col) in cubeRocks or (i - 1, col) in roundRocksLocs:
            roundRocksLocs.remove(roundRock)
            roundRocksLocs.add((i, col))
            newRoundRocks.append((i, col))
            return


def west(roundRock):
    row, col = roundRock
    for i in range(col, -1, -1):
        if (row, i - 1) in cubeRocks or (row, i - 1) in roundRocksLocs:
            roundRocksLocs.remove(roundRock)
            roundRocksLocs.add((row, i))
            newRoundRocks.append((row, i))
            return


def south(roundRock):
    row, col = roundRock
    for i in range(row, rowNum):
        if (i + 1, col) in cubeRocks or (i + 1, col) in roundRocksLocs:
            roundRocksLocs.remove(roundRock)
            roundRocksLocs.add((i, col))
            newRoundRocks.append((i, col))
            return


def east(roundRock):
    row, col = roundRock
    for i in range(col, colNum):
        if (row, i + 1) in cubeRocks or (row, i + 1) in roundRocksLocs:
            roundRocksLocs.remove(roundRock)
            roundRocksLocs.add((row, i))
            newRoundRocks.append((row, i))
            return


def cycle():
    global roundRocks, newRoundRocks
    for rock in roundRocks:
        north(rock)

    roundRocks = newRoundRocks
    newRoundRocks = []
    roundRocks = sorted(roundRocks, key=lambda x: x[1], reverse=False)

    for rock in roundRocks:
        west(rock)

    roundRocks = newRoundRocks
    newRoundRocks = []
    roundRocks = sorted(roundRocks, key=lambda x: x[0], reverse=True)

    for rock in roundRocks:
        south(rock)

    roundRocks = newRoundRocks
    newRoundRocks = []
    roundRocks = sorted(roundRocks, key=lambda x: x[1], reverse=True)

    for rock in roundRocks:
        east(rock)

    roundRocks = newRoundRocks
    newRoundRocks = []
    roundRocks = sorted(roundRocks, key=lambda x: (x[0]), reverse=False)


def calcLoad():
    tot = 0
    for rock in roundRocks:
        tot += (rowNum - rock[0])
    return tot


def day14p1():
    global rowNum, colNum
    lines = open("test.txt", "r", encoding="utf-8").read().splitlines()
    rowNum = len(lines)
    colNum = len(lines[0])
    for row in range(len(lines)):
        for column in range(len(lines)):
            if lines[row][column] == '#':
                cubeRocks.add((row, column))
            elif lines[row][column] == 'O':
                roundRocks.append((row, column))

    for i in range(colNum):
        cubeRocks.add((-1, i))

    tot = 0
    for rock in roundRocks:
        tot += findDestination(rock)
    return tot


def day14p2():
    global rowNum, colNum
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    rowNum = len(lines)
    colNum = len(lines[0])
    result = {}
    for row in range(len(lines)):
        for column in range(len(lines)):
            if lines[row][column] == '#':
                cubeRocks.add((row, column))
            elif lines[row][column] == 'O':
                roundRocks.append((row, column))
                roundRocksLocs.add((row, column))

    for i in range(colNum):
        cubeRocks.add((-1, i))
        cubeRocks.add((rowNum, i))

    for i in range(rowNum):
        cubeRocks.add((i, -1))
        cubeRocks.add((i, colNum))

    for i in range(500):
        cycle()
        r = calcLoad()
        if result.get(r, 0) != 0:
            result[r].append(i)
        else:
            result[r] = [i]
    loopResults = {}
    loopVal = 0
    minR = 999
    for r in result:
        if len(result[r]) > 5:
            loopVal = result[r][6] - result[r][5]
            loopResults[result[r][5]] = r
            minR = min(result[r][5], minR)
    a = 1000000000
    final = minR + ((a - minR) % loopVal) - 1
    return loopResults[final]


print(day14p2())
