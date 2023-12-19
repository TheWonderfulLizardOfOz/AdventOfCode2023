import re
from functools import reduce

boxes = dict((i, {}) for i in range(0, 256))


def day15p1():
    return sum([reduce(lambda acc, x: ((acc + ord(x))*17) % 256, y, 0) for y in open("input.txt", "r", encoding="utf-8").read().strip().split(',')])


def day15p2():
    parts = open("input.txt", "r", encoding="utf-8").read().split(',')
    for part in parts:
        letters = re.findall(r'([A-Z|[a-z])', part)

        result = reduce(lambda acc, x: ((acc + ord(x))*17) % 256, letters, 0)
        letters = ''.join(letters)

        operator = re.findall(r'=|-', part)
        if operator[0] == '=':
            focalLength = re.findall(r'\d', part)
            boxes[result][letters] = int(focalLength[0])
        else:
            if letters in boxes[result]:
                boxes[result].pop(letters)

    tot = 0
    for box in boxes:
        i = 0
        for slot in boxes[box]:
            i += 1
            tot += (box + 1) * i * boxes[box][slot]
    return tot

print(day15p2())
