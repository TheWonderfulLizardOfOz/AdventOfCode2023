import re
import numpy as np
import math


def allZero(nums):
    for num in nums:
        if num != 0:
            return False
    return True


def day9p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    tot = 0
    for line in lines:
        nums = [int(n) for n in line.split()]
        newVal = nums[-1]
        while not allZero(nums):
            diff = []
            for i in range(1, len(nums)):
                change = nums[i] - nums[i - 1]
                diff.append(change)
            newVal += diff[-1]
            nums = diff
        tot += newVal
    return tot


def day9p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    tot = 0
    for line in lines:
        nums = [int(n) for n in line.split()]
        newVal = nums[0]
        j = 0
        while not allZero(nums):
            diff = []
            for i in range(1, len(nums)):
                change = nums[i] - nums[i - 1]
                diff.append(change)
            if j % 2 == 0:
                newVal -= diff[0]
            else:
                newVal += diff[0]
            j += 1
            nums = diff
        tot += newVal
    return tot


print(day9p2())
