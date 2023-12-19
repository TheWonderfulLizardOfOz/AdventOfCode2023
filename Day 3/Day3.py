import re

def day3p1():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    symbolLocs = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' and not lines[i][j].isdigit():
                #line, column
                symbolLocs.append((i, j))

    tot = 0
    notPart = []
    currentNumStart = (0,0)
    currentNum = ''
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() and currentNum == '':
                currentNumStart = (i, j)
                currentNum += lines[i][j]
            elif lines[i][j].isdigit() and j == len(lines[i]) - 1:
                currentNum += lines[i][j]
                if isAdj(symbolLocs, currentNumStart, (i, j)):
                    tot += int(currentNum)
                else:
                    notPart.append(currentNum)
                currentNum = ''
            elif lines[i][j].isdigit():
                currentNum += lines[i][j]
            elif not lines[i][j].isdigit() and currentNum != '':
                if isAdj(symbolLocs, currentNumStart, (i, j - 1)):
                    tot += int(currentNum)
                else:
                    notPart.append(currentNum)
                currentNum = ''
    return tot


def day3p2():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    symbolLocs = []
    gears = {}

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' and not lines[i][j].isdigit():
                # line, column
                symbolLocs.append((i, j))
                gears[(i, j)] = []
    print(gears)
    currentNumStart = (0, 0)
    currentNum = ''
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() and currentNum == '':
                currentNumStart = (i, j)
                currentNum += lines[i][j]
            elif lines[i][j].isdigit() and j == len(lines[i]) - 1:
                currentNum += lines[i][j]
                adjs = checkGear(symbolLocs, currentNumStart, (i, j))
                for gear in adjs:
                    gears[gear].append(int(currentNum))
                currentNum = ''
            elif lines[i][j].isdigit():
                currentNum += lines[i][j]
            elif not lines[i][j].isdigit() and currentNum != '':
                adjs = checkGear(symbolLocs, currentNumStart, (i, j-1))
                for gear in adjs:
                    gears[gear].append(int(currentNum))
                currentNum = ''

    tot = 0
    print(gears)
    for gear in gears.values():
        if len(gear) == 2:
            tot += gear[0]*gear[1]

    return tot

def checkGear(symbL, startL, endL):
    adjs = []
    for loc in symbL:
        if loc[0] > startL[0] + 1:
            return adjs
        if -1 <= startL[0] - loc[0] <= 1:
            if startL[1] - 1 <= loc[1] <= endL[1] + 1:
                adjs.append(loc)
    return adjs


def isAdj(symbL, startL, endL):
    for loc in symbL:
        if loc[0] > startL[0] + 1:
            return False
        if -1 <= startL[0] - loc[0] <= 1:
            if startL[1] - 1 <= loc[1] <= endL[1] + 1:
                return True
    return False


print(day3p2())