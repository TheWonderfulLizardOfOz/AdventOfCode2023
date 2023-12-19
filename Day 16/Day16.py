import re
import numpy as np
import math

grid = {}
energised = set()
doneMovements = set()
# direction beam moving in
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
backSlashDirection = {'R': 'D', 'D': 'R', 'L': 'U', 'U': 'L'}
forwSlashDirection = {'D': 'L', 'L': 'D', 'U': 'R', 'R': 'U'}


def move(loc, d):
    return loc[0] + directions[d][0], loc[1] + directions[d][1]


def energise(loc, direction):
    split = False
    finished = False

    if loc in grid:
        energised.add(loc)
    else:
        finished = True

    if (loc, direction) not in doneMovements:
        doneMovements.add((loc, direction))
    else:
        finished = True

    while not split and not finished:
        if grid[loc] == '.' or (grid[loc] == '-' and direction in {'R', 'L'}) or (grid[loc] == '|' and direction in {'U', 'D'}):
            loc = move(loc, direction)

        elif grid[loc] == '|':
            energise(move(loc, 'U'), 'U')
            energise(move(loc, 'D'), 'D')
            split = True

        elif grid[loc] == '-':
            energise(move(loc, 'R'), 'R')
            energise(move(loc, 'L'), 'L')
            split = True

        elif grid[loc] == '\\':
            direction = backSlashDirection[direction]
            loc = move(loc, direction)

        elif grid[loc] == '/':
            direction = forwSlashDirection[direction]
            loc = move(loc, direction)

        if not split:
            if loc in grid:
                energised.add(loc)
            else:
                finished = True

            if (loc, direction) not in doneMovements:
                doneMovements.add((loc, direction))
            else:
                finished = True


def day16p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]

    energise((0, 0), 'R')
    return len(energised)


def day16p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]

    maxEnergised = 0
    for column in range(numColumns):
        doneMovements.clear()
        energised.clear()
        energise((0, column), 'D')
        maxEnergised = max(maxEnergised, len(energised))

        doneMovements.clear()
        energised.clear()
        energise((numRows - 1, column), 'U')
        maxEnergised = max(maxEnergised, len(energised))

    for row in range(numRows):
        doneMovements.clear()
        energised.clear()
        energise((row, 0), 'R')
        maxEnergised = max(maxEnergised, len(energised))

        doneMovements.clear()
        energised.clear()
        energise((row, numColumns - 1), 'L')
        maxEnergised = max(maxEnergised, len(energised))
    return maxEnergised

print(day16p2())
