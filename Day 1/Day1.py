import re

def day1p1():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    tot = 0
    for line in lines:
        nums = re.findall(r'\d', line)
        tot += (int(nums[0] + nums[-1]))
    return tot

def day1p2():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    tot = 0
    for line in lines:
        print(line)
        nums = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
        num1 = convertToInt(nums[0])
        num2 = convertToInt(nums[-1])
        print(num1, num2)
        tot += (num1*10) + num2
    return tot

def convertToInt(num):
    numDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    upNum = numDict.get(num, None)
    if not upNum:
        return int(num)
    return upNum

print(day1p2())