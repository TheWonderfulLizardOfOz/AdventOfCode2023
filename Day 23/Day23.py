import re
import numpy as np
import math
import sys

sys.setrecursionlimit(1000000)

start = (0, 1)
target = (0, 0)
grid = {}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
oppositeDirection = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
slopeDirection = {'>': 'R', '<': 'L', '^': 'U', 'v': 'D'}
children = {}
# (parent, child)
edges = {}
parents = {}


def move(loc, d):
    return loc[0] + directions[d][0], loc[1] + directions[d][1]


def availableMovements(loc, currentD, path):
    availableLocs = []
    for d in directions:
        if d != oppositeDirection[currentD]:
            nLocation = move(loc, d)
            if nLocation in grid and nLocation not in path:
                symbol = grid[nLocation]
                if (symbol != '#') and (symbol == '.' or slopeDirection[symbol] == d):
                    availableLocs.append((nLocation, d))
    return availableLocs


def availableDirectionsNodes(loc, currentD):
    availableDirections = []
    for d in directions:
        if d != oppositeDirection[currentD]:
            nLocation = move(loc, d)
            if nLocation in grid:
                symbol = grid[nLocation]
                if symbol != '#':
                    availableDirections.append(d)
    return availableDirections


def findLongestPath(loc, direction, path):
    path.add(loc)
    nextMovements = availableMovements(loc, direction, path)

    if len(nextMovements) == 0:
        return 0

    maxPath = 0
    for mov in nextMovements:
        nLoc, d = mov
        if nLoc == target:
            maxPath = max(maxPath, len(path))
        else:
            maxPath = max(maxPath, findLongestPath(nLoc, d, path.copy()))

    return maxPath


def createNetwork(node, direction):
    queue = [(node, direction)]
    visited = set()

    while len(queue) > 0:
        current = queue.pop(0)
        cNode, cDirection = current
        visited.add(current)
        cNode = move(cNode, cDirection)
        nextMovements = availableDirectionsNodes(cNode, cDirection)
        edgeDistance = 1

        while len(nextMovements) == 1:
            cNode = move(cNode, nextMovements[0])
            cDirection = nextMovements[0]
            edgeDistance += 1

            if cNode == target or cNode in visited:
                nextMovements = []
            else:
                nextMovements = availableDirectionsNodes(cNode, cDirection)

        for d in nextMovements:
            if (cNode, d) not in visited:
                queue.append((cNode, d))

        edges[(current[0], cNode)] = edgeDistance

        if current[0] in children:
            children[current[0]].add(cNode)
        else:
            children[current[0]] = {cNode}
        if cNode in parents:
            parents[cNode].add(current[0])
        else:
            parents[cNode] = {current[0]}



def dfs(node, path, length):
    path.add(node)

    maxPath = 0
    for child in children[node]:
        if child == target:
            maxPath = max(maxPath, length + edges[(node, child)])
        elif child not in path:
            newPath = path.copy()
            newPath.add(child)
            maxPath = max(maxPath, dfs(child, newPath, length + edges[(node, child)]))

    return maxPath



def day23p1():
    global target
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])
    target = (numRows - 1, numColumns - 2)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]

    return findLongestPath(start, 'D', set())


def day23p2():
    global target
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    numRows = len(lines)
    numColumns = len(lines[0])
    target = (numRows - 1, numColumns - 2)

    for row in range(numRows):
        for column in range(numColumns):
            grid[(row, column)] = lines[row][column]

    #return findLongestPathP2(start, 'D', set())
    createNetwork(start, 'D')
    return dfs(start, set(), 0)


print(day23p2())
