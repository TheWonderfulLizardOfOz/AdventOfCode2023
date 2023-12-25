import re
from sympy import symbols, Eq, solve

hailStones = []
testArea = (200000000000000, 400000000000000)


def getLine():
    stone1, stone2, stone3 = hailStones[0], hailStones[1], hailStones[2]

    x, y, z, vx, vy, vz, t, u, v = symbols("x y z vx vy vz t u v")

    (sx1, sy1, sz1), (svx1, svy1, svz1) = stone1

    eq1 = Eq(x + t * vx - svx1 * t, sx1)
    eq2 = Eq(y + t * vy - svy1 * t, sy1)
    eq3 = Eq(z + t * vz - svz1 * t, sz1)

    (sx2, sy2, sz2), (svx2, svy2, svz2) = stone2

    eq4 = Eq(x + u * vx - svx2 * u, sx2)
    eq5 = Eq(y + u * vy - svy2 * u, sy2)
    eq6 = Eq(z + u * vz - svz2 * u, sz2)

    (sx3, sy3, sz3), (svx3, svy3, svz3) = stone3

    eq7 = Eq(x + v * vx - svx3 * v, sx3)
    eq8 = Eq(y + v * vy - svy3 * v, sy3)
    eq9 = Eq(z + v * vz - svz3 * v, sz3)

    solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (x, y, z, vx, vy, vz, t, u, v))

    print(solution)
    return solution[0][0] + solution[0][1] + solution[0][2]


def checkFuture(initial, intersect, change):
    if not (testArea[0] <= intersect <= testArea[1]):
        return False

    return (change >= 0 and initial <= intersect) or (change < 0 and initial > intersect)


def doesIntersectInFuture(stone1, stone2):
    (x1, y1, z1), (dx1, dy1, dz1) = stone1
    (x2, y2, z2), (dx2, dy2, dz2) = stone2

    m1 = dy1/dx1
    m2 = dy2/dx2

    if m1 == m2:
        return False

    c1 = y1 - (m1*x1)
    c2 = y2 - (m2*x2)

    xIntersect = (c2 - c1) / (m1 - m2)
    yIntersect = (m1 * xIntersect) + c1

    return checkFuture(x1, xIntersect, dx1) and checkFuture(x2, xIntersect, dx2) and checkFuture(y1, yIntersect, dy1) and checkFuture(y2, yIntersect, dy2)


def day24p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    for line in lines:
        nums = [int(num) for num in re.findall(r"-?\d+", line)]
        hailStones.append((nums[0:3], nums[3:]))

    tot = 0
    for i in range(len(hailStones)):
        for j in range(i + 1, len(hailStones)):
            if doesIntersectInFuture(hailStones[i], hailStones[j]):
                tot += 1

    return tot


def day24p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    for line in lines:
        nums = [int(num) for num in re.findall(r"-?\d+", line)]
        hailStones.append((nums[0:3], nums[3:]))

    return getLine()


print(day24p2())
