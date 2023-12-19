import re
import numpy as np
import math

mirrorSet = {}


def columnToString(column, maxRow):
    result = ""
    for i in range(1, maxRow + 1):
        result += mirrorSet[(i, column)]
    return result


def rowToString(row, maxColumn):
    result = ""
    for i in range(1, maxColumn + 1):
        result += mirrorSet[(row, i)]
    return result


def findReflection(maxRow, maxColumn):
    global mirrorSet
    # check vertical
    isMirror = False
    for i in range(1, maxColumn):
        isMirror = True
        for j in range(0, i):
            if i + j + 1 > maxColumn:
                break
            if columnToString(i-j, maxRow) != columnToString(i + j + 1, maxRow):
                isMirror = False
                break

        if isMirror:
            return i, False

    # check horizontal
    for i in range(1, maxRow):
        isMirror = True
        for j in range(0, i):
            if i + j + 1 > maxRow:
                break
            if rowToString(i - j, maxColumn) != rowToString(i + j + 1, maxColumn):
                isMirror = False
                break

        if isMirror:
            return i, True


def findReflectionSmudge(maxRow, maxColumn):
    global mirrorSet
    # check vertical
    for i in range(1, maxColumn):
        isMirror = True
        smudgeCount = 0
        for j in range(0, i):
            if i + j + 1 > maxColumn:
                break

            c1 = columnToString(i-j, maxRow)
            c2 = columnToString(i + j + 1, maxRow)
            diff = sum([1 for i in range(len(c1)) if c1[i] != c2[i]])
            if diff == 1 and smudgeCount == 0:
                smudgeCount = 1
                diff = 0
            if diff != 0:
                isMirror = False
                break

        if isMirror and smudgeCount == 1:
            return i, False

    # check horizontal
    for i in range(1, maxRow):
        isMirror = True
        smudgeCount = 0
        for j in range(0, i):
            if i + j + 1 > maxRow:
                break

            r1 = rowToString(i - j, maxColumn)
            r2 = rowToString(i + j + 1, maxColumn)
            diff = sum([1 for i in range(len(r1)) if r1[i] != r2[i]])
            if diff == 1 and smudgeCount == 0:
                smudgeCount = 1
                diff = 0
            if diff != 0:
                isMirror = False
                break

        if isMirror and smudgeCount == 1:
            return i, True
    return


def day13p1():
    global mirrorSet
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    i = 0
    j = 0
    tot = 0
    for row in range(len(lines)):
        if lines[row] == "" and i != 0:
            val = findReflection(i, j)
            if val[1]:
                tot += val[0]*100
            else:
                tot += val[0]
            mirrorSet.clear()
            i = 0
            continue
        i += 1
        j = 0
        for column in range(len(lines[row])):
            j += 1
            mirrorSet[(i, j)] = lines[row][column]

    val = findReflection(i, j)
    if val[1]:
        tot += val[0] * 100
    else:
        tot += val[0]
    mirrorSet.clear()
    return tot


def day13p2():
    global mirrorSet
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    i = 0
    j = 0
    tot = 0
    for row in range(len(lines)):
        if lines[row] == "" and i != 0:
            val = findReflectionSmudge(i, j)
            if val[1]:
                tot += val[0] * 100
            else:
                tot += val[0]
            mirrorSet.clear()
            i = 0
            continue
        i += 1
        j = 0
        for column in range(len(lines[row])):
            j += 1
            mirrorSet[(i, j)] = lines[row][column]

    val = findReflectionSmudge(i, j)
    if val[1]:
        tot += val[0] * 100
    else:
        tot += val[0]
    mirrorSet.clear()
    return tot


print(day13p2())
