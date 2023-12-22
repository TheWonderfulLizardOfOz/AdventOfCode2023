import re
import time

import numpy as np
import math
from functools import cache

evenReachable = set()
oddReachable = set()
unvisited = set()
visited = set()
nextStepLocs = set()

grid = {}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}


@cache
def getValidNeighbours(location):
    validDirections = []
    for d in directions:
        nRow, nColumn = move(location, d)
        if grid[(nRow % numRows, nColumn % numColumns)] == '.':
            validDirections.append(d)
    return validDirections


def move(location, direction):
    vector = directions[direction]
    return location[0] + vector[0], location[1] + vector[1]


def step(location):
    newLocs = set()
    for d in directions:
        nLocation = move(location, d)
        if nLocation in grid and grid[nLocation] == '.':
            newLocs.add(nLocation)
            nextStepLocs.add(nLocation)

    if location in evenReachable:
        oddReachable.update(newLocs)
    if location in oddReachable:
        evenReachable.update(newLocs)


def run(noSteps):
    global unvisited
    for i in range(noSteps):
        while len(unvisited) > 0:
            step(unvisited.pop())
        unvisited = nextStepLocs.copy()
        nextStepLocs.clear()


@cache
def stepInf(location, validDirections):
    newLocs = set()
    for d in validDirections:
        newLocs.add(move(location, d))

    return newLocs


def runInf(noSteps):
    global unvisited
    for i in range(noSteps):
        while len(unvisited) > 0:
            currentLoc = unvisited.pop()
            visited.add(currentLoc)
            validDirections = getValidNeighbours((currentLoc[0] % numRows, currentLoc[1] % numColumns))
            newLocs = stepInf(currentLoc, tuple(validDirections))

            for loc in newLocs:
                if loc not in visited:
                    nextStepLocs.add(loc)
                elif currentLoc in evenReachable and loc not in oddReachable:
                    nextStepLocs.add(loc)
                elif currentLoc in oddReachable and loc not in evenReachable:
                    nextStepLocs.add(loc)

            if currentLoc in oddReachable:
                evenReachable.update(newLocs)
            if currentLoc in evenReachable:
                oddReachable.update(newLocs)

        unvisited = nextStepLocs.copy()
        nextStepLocs.clear()


def getFormula(steps):
    evenReachable.add(start)
    unvisited.add(start)
    runInf(65)
    x = len(oddReachable)
    visited.clear()
    oddReachable.clear()
    evenReachable.clear()
    unvisited.clear()

    evenReachable.add(start)
    unvisited.add(start)
    runInf(196)
    y = len(evenReachable)
    visited.clear()
    oddReachable.clear()
    evenReachable.clear()
    unvisited.clear()

    evenReachable.add(start)
    unvisited.add(start)
    runInf(327)
    z = len(oddReachable)

    print(x, y, z)

    firstDiff = y - x
    secondDiff = (z - y) - (y - x)

    a = secondDiff // 2
    b = firstDiff - 3*a
    c = x - a - b

    n = (steps // 131) + 1

    return a*(n**2) + b*n + c

#629720570456311
def day21p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])

    start = (0, 0)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]
            if grid[(row, column)] == 'S':
                start = (row, column)

    evenReachable.add(start)
    unvisited.add(start)

    noSteps = 131
    run(noSteps)

    if noSteps % 2 == 0:
        return len(evenReachable)
    else:
        return len(oddReachable)


def day21p2():
    global numRows, numColumns, start
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])

    start = (0, 0)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]
            if grid[(row, column)] == 'S':
                start = (row, column)
                grid[(row, column)] = '.'

    evenReachable.add(start)
    unvisited.add(start)

    return getFormula(26501365)


startTime = time.time()
print(day21p2())
endTime = time.time()
print(endTime - startTime)
