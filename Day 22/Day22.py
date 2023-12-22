import re

bricks = []
fallenBricks = []
grid = {}
soleSupports = {}
count = 0
supportedBy = {}


def disintegrateBrick(brick):
    falls = soleSupports[brick].copy()
    if len(falls) == 0:
        return set()

    noChanges = False
    while not noChanges:
        noChanges = True
        for b in supportedBy:
            if b not in falls and len(supportedBy[b]) > 0 and all(supportB in falls for supportB in supportedBy[b]):
                falls.add(b)
                noChanges = False

    return falls


def addToGrid(x1, y1, z1, x2, y2, z2):
    global count
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                grid[(x, y, z)] = count
    soleSupports[count] = set()
    supportedBy[count] = set()
    count += 1


def parseAndSort():
    global bricks
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    for line in lines:
        nums = [int(num) for num in re.findall(r"\d+", line)]
        (x1, y1, z1), (x2, y2, z2) = nums[0:3], nums[3:]
        bricks.append(((x1, y1, z1), (x2, y2, z2)))

    bricks = sorted(bricks, key=lambda x: (x[0][2], x[1][2]), reverse=False)


def fall(b):
    (x1, y1, z1), (x2, y2, z2) = b[0], b[1]
    for z in range(z1, 0, -1):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if (x, y, z - 1) in grid:
                    addToGrid(x1, y1, z, x2, y2, z + (z2 - z1))
                    fallenBricks.append(((x1, y1, z), (x2, y2, z + (z2 - z1))))
                    return
    addToGrid(x1, y1, 1, x2, y2, 1 + (z2 - z1))
    fallenBricks.append(((x1, y1, 1), (x2, y2, 1 + (z2 - z1))))


def setSupports():
    for b in fallenBricks:
        supports = set()
        bID = grid[b[0]]
        (x1, y1, z1), (x2, y2, z2) = b[0], b[1]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y, z1 - 1) in grid:
                    supports.add(grid[(x, y, z1 - 1)])

        supportedBy[bID].update(supports)

        if len(supports) == 1:
            soleSupports[supports.pop()].add(bID)


def day22p1():
    global fallenBricks
    parseAndSort()
    for b in bricks:
        fall(b)

    setSupports()

    return sum([1 for x in soleSupports.values() if len(x) == 0])


def day22p2():
    global fallenBricks
    parseAndSort()
    for b in bricks:
        fall(b)

    setSupports()

    tot = 0
    for brick in soleSupports:
        tot += len(disintegrateBrick(brick))
    return tot


print(day22p1())
