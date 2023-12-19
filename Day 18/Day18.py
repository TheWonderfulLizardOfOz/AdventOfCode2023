import re
import numpy as np
import math

grid = {}
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
numToDirection = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def area(corners):
    a = 2
    for i in range(len(corners) - 1):
        a += determinant(corners[i + 1], corners[i])
        a += abs((corners[i][0] - corners[i + 1][0]) + (corners[i][1] - corners[i + 1][1]))

    a += determinant(corners[0], corners[-1])
    a += abs((corners[0][0] - corners[-1][0]) + (corners[0][1] - corners[-1][1]))

    return a // 2


def determinant(v1, v2):
    return (v1[0] * v2[1]) - (v1[1] * v2[0])


def move(location, direction, distance=1):
    vector = directions[direction]
    scaled = (distance * (vector[0]), distance * (vector[1]))
    return location[0] + scaled[0], location[1] + scaled[1]


def day18p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    # [0][0] = direction [0][1] = distance [0][2] = hex
    r = r"(L|R|U|D)\s(\d+)\s\(#(.*)\)"
    corners = []
    loc = (0, 0)

    for i in range(len(lines)):
        result = re.findall(r, lines[i])[0]
        direction = result[0]
        distance = int(result[1])
        loc = move(loc, direction, distance)
        corners.append(loc)

    return area(corners)


def day18p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    r = r"\(#(.*)\)"
    corners = []
    loc = (0, 0)
    
    for i in range(len(lines)):
        result = re.findall(r, lines[i])[0]
        direction = numToDirection[result[-1]]
        distance = int(result[0:5], 16)

        loc = move(loc, direction, distance)
        corners.append(loc)

    return area(corners)


print(day18p2())
