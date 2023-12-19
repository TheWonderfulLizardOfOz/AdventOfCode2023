# NESW is position of point relative to pipe
paths = {'|': {'N': (1, 0), 'S': (-1, 0)}, '-': {'E': (0, -1), 'W': (0, 1)}, 'L': {'N': (0, 1), 'E': (-1, 0)},
         'J': {'N': (0, -1), 'W': (-1, 0)}, '¬': {'W': (1, 0), 'S': (0, -1)}, 'F': {'E': (1, 0), 'S': (0, 1)}}

directions = {'|': {(1, 0), (-1, 0)}, '-': {(0, -1), (0, 1)}, 'L': {(-1, 0), (0, 1)},
              'J': {(-1, 0), (0, -1)}, '¬': {(0, -1), (1, 0)}, 'F': {(1, 0), (0, 1)}}

loopPoints = {}


def calcPath(grid, point):
    row, column = point
    symbol = grid[row][column]
    pathOpts = directions[symbol]

    for opt in pathOpts:
        nRow, nColumn = (row + opt[0], column + opt[1])
        if loopPoints.get((nRow, nColumn), -1) == -1:
            return nRow, nColumn

    return None


def day10p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    start = (0, 0)
    visited = set()

    for row in range(len(lines)):
        lines[row] = list(lines[row])
        for column in range(len(lines[row])):
            if lines[row][column] == 'S':
                start = (row, column)
                loopPoints[start] = 0
            if lines[row][column] == '7':
                lines[row][column] = '¬'

    adj = {'S': (start[0] - 1, start[1]), 'W': (start[0], start[1] + 1),
           'N': (start[0] + 1, start[1]), 'E': (start[0], start[1] - 1)}

    connectsTo = []

    for d in adj:
        point = adj[d]
        row, column = point
        symbol = lines[row][column]
        if symbol != '.':
            if paths[symbol].get(d, None):
                connectsTo.append(point)

    visited.add(start)
    loopPoints[start] = 0

    value = 1
    maxVal = value
    while len(connectsTo) > 0:
        newConnects = []
        for point in connectsTo:
            if point not in visited:
                newP = calcPath(lines, point)
                if newP:
                    newConnects.append(newP)

                visited.add(point)
                loopPoints[point] = value
                maxVal = value

        value += 1
        connectsTo = newConnects

    return maxVal


def day10p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    day10p1()

    for row in range(len(lines)):
        lines[row] = list(lines[row])
        for column in range(len(lines[row])):
            if lines[row][column] == 'S':
                # Replace whatever actual pipe of S is from input because I'm lazy
                lines[row][column] = '¬'
            if (row, column) not in loopPoints:
                lines[row][column] = '.'
            if lines[row][column] == '7':
                lines[row][column] = '¬'

    counter = 0
    flip = {'|', '¬', 'F'}
    for row in range(len(lines)):
        inside = False
        for column in range(len(lines[row])):
            if lines[row][column] == '.' and inside:
                lines[row][column] = 'I'
                counter += 1
            elif lines[row][column] in flip:
                inside = not inside
            elif lines[row][column] == '.':
                lines[row][column] = '0'

    return counter


print(day10p2())
