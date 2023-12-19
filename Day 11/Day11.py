galaxyLocs = set()
rows = {}
columns = {}


def setGalaxies(val):
    global rows, columns

    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    noRows = len(lines)
    noColumns = len(lines[0])

    rows = dict((row, val) for row in range(noRows))
    columns = dict((column, val) for column in range(noColumns))

    for row in range(noRows):
        for column in range(noColumns):
            if lines[row][column] == '#':
                rows[row] = 1
                columns[column] = 1
                galaxyLocs.add((row, column))


def totalDistances():
    total = 0
    for g1 in galaxyLocs:
        for g2 in galaxyLocs:
            if g1 != g2:
                total += getDistance(g1, g2)
    return total


def getDistance(g1, g2):
    dist = 0
    for row in range(g1[0], g2[0]):
        dist += rows[row]
    for col in range(g1[1], g2[1]):
        dist += columns[col]

    return dist


def day11p1():
    setGalaxies(2)
    return totalDistances()


def day11p2():
    setGalaxies(1000000)
    return totalDistances()


print(day11p2())
