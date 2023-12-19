import re


def day4p1():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    total = 0
    for line in lines:
        match = getMatches(line)
        if match >= 1:
            total += 2 ** (match - 1)
    return total


def day4p2():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()

    total = 0
    numOfCards = len(lines)
    cards = dict((i, 1) for i in range (0, numOfCards))
    for card in cards:
        line = lines[card]
        match = getMatches(line)
        total += cards[card]
        for i in range(1, match + 1):
            cards[card + i] += 1*cards[card]

    return total


def getMatches(line):
    nums = re.findall(r'(:)(.*?)(\|)(.*)', line)
    winningNums = nums[0][1].split()
    selectedNums = nums[0][3].split()
    match = 0
    for num in selectedNums:
        if num in winningNums:
            match += 1

    return match


print(day4p2())
