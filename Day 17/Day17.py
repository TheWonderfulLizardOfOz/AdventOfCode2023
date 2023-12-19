import re
import numpy as np
import math
from collections import OrderedDict

grid = {}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
lTurn = {'R': 'U', 'D': 'R', 'L': 'D', 'U': 'L'}
rTurn = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}
minLoss = 999999
target = (0, 0)
high = 999999
cache = {}


def move(loc, d):
    return loc[0] + directions[d][0], loc[1] + directions[d][1]


def getConnectors(location, direction):
    connectors = []
    forward1 = move(location, direction)
    forward2 = move(forward1, direction)
    forward3 = move(forward2, direction)
    if forward1 in grid:
        w1 = grid[forward1]
        if (forward1, lTurn[direction]) not in visited:
            connectors.append((w1, forward1, lTurn[direction]))
        if (forward1, rTurn[direction]) not in visited:
            connectors.append((w1, forward1, rTurn[direction]))

    if forward2 in grid:
        w2 = w1 + grid[forward2]
        if (forward2, lTurn[direction]) not in visited:
            connectors.append((w2, forward2, lTurn[direction]))
        if (forward2, rTurn[direction]) not in visited:
            connectors.append((w2, forward2, rTurn[direction]))

    if forward3 in grid:
        w3 = w2 + grid[forward3]
        if (forward3, lTurn[direction]) not in visited:
            connectors.append((w3, forward3, lTurn[direction]))
        if (forward3, rTurn[direction]) not in visited:
            connectors.append((w3, forward3, rTurn[direction]))

    return connectors


def getConnectors2(location, direction):
    connectors = []
    forward1 = move(location, direction)
    forward2 = move(forward1, direction)
    forward3 = move(forward2, direction)

    if forward3 not in grid:
        return []

    forward = forward3
    w = grid[forward1] + grid[forward2] + grid[forward3]
    for i in range(4, 11):
        forward = move(forward, direction)
        if forward in grid:
            w += grid[forward]
            if (forward, lTurn[direction]) not in visited:
                connectors.append((w, forward, lTurn[direction]))
            if (forward, rTurn[direction]) not in visited:
                connectors.append((w, forward, rTurn[direction]))
        else:
            break
    return connectors


# {(location, direction): weight}
points = {}
visited = set()


def dijkstra(location, direction):
    visited.clear()
    points.clear()
    points[(location, direction)] = 0
    found = False
    cLoc = location
    cDir = direction
    cWeight = 0
    while not found:
        print(cWeight)
        visited.add((cLoc, cDir))
        points.pop((cLoc, cDir), None)
        # finds all connections that haven't been visited
        connectors = getConnectors2(cLoc, cDir)
        for c in connectors:
            weight = c[0] + cWeight
            point = c[1]
            direction = c[2]
            if (point, direction) not in points:
                points[(point, direction)] = high
            points[(point, direction)] = min(weight, points[(point, direction)])

        minPoint = ((-1, -1), '')
        minWeight = high
        for point, weight in points.items():
            if weight < minWeight:
                minWeight = weight
                minPoint = point

        if minPoint[0] == target:
            found = True
            cWeight = minWeight
        else:
            cLoc = minPoint[0]
            cDir = minPoint[1]
            cWeight = minWeight

    print(cWeight)
    return cWeight


def day17p1():
    global target
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])
    target = (numRows - 1, numColumns - 1)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = int(lines[row][column])

    #print(dfs((0, 0), 'R', 0, set()))
    #print(dfs((0, 0), 'D', 0, set()))
    return min(dijkstra((0, 0), 'R'), dijkstra((0, 0), 'D'))


def day17p2():
    global target
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])
    target = (numRows - 1, numColumns - 1)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = int(lines[row][column])

    # print(dfs((0, 0), 'R', 0, set()))
    # print(dfs((0, 0), 'D', 0, set()))
    return min(dijkstra((0, 0), 'R'), dijkstra((0, 0), 'D'))


print(day17p2())
