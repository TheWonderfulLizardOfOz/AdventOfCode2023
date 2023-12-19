import re
import math
from functools import cache
import time

@cache
def bfs(sequence, nums):
    hashes = re.findall(r'#+', sequence)

    if len(nums) == 0 and len(hashes) != 0:
        return 0
    elif len(nums) == 0:
        return 1

    if len(sequence) < sum(nums) + len(nums) - 1:
        return 0

    if sequence[0] == '.':
        return bfs(sequence[1:], nums)

    if sequence[0] == '#':
        if len(hashes[0]) == nums[0]:
            return bfs(sequence[nums[0] + 1:], nums[1:])
        elif len(hashes[0]) > nums[0]:
            return 0
        elif len(hashes[0]) < nums[0] and all((c == '?' or c == '#') for c in sequence[len(hashes[0]):nums[0]]):
            if nums[0] == len(sequence):
                return 1
            elif sequence[nums[0]] == '.' or sequence[nums[0]] == '?':
                return bfs(sequence[nums[0] + 1:], nums[1:])
            else:
                return 0
        else:
            return 0

    if sequence[0] == '?':
        s = re.findall(r'\?+\.*', sequence)
        if len(s) == 1 and len(s[0]) == len(sequence):
            s = s[0].strip('.')
            w = len(s)
            n = len(nums)
            t = sum(nums)
            if t > w:
                return 0
            return math.comb(w - t + 1, n)
        else:
            return bfs('#' + sequence[1:], nums) + bfs(sequence[1:], nums)


def day12p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    tot = 0
    for i in range(len(lines)):
        line = lines[i].split()
        sequence = line[0].strip('.')
        nums = (int(x) for x in line[1].split(','))
        val = bfs(sequence, nums)
        tot += val
    return tot


def day12p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    tot = 0
    for i in range(len(lines)):
        line = lines[i].split()
        sequence = (line[0] + '?')*4 + line[0]
        sequence = sequence.strip('.')
        nums = tuple([int(x) for x in line[1].split(',')]*5)
        val = bfs(sequence, nums)
        tot += val
    return tot


start = time.time()
print(day12p2())
end = time.time()
print(end - start)
