import re

def day2p1():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    possTot = 0

    for line in lines:
        valid = True
        gNumber = re.findall(r'\d+:', line)
        gNumber = int(gNumber[0].strip(":"))
        game = line.split(": ")[1]
        sets = game.split("; ")
        for s in sets:
            reds = re.findall(r'\d+ red', s)
            rCount = sum([int((x.split(" ")[0])) for x in reds])

            greens = re.findall(r'\d+ green', s)
            gCount = sum([int((x.split(" ")[0])) for x in greens])

            blues = re.findall(r'\d+ blue', s)
            bCount = sum([int((x.split(" ")[0])) for x in blues])
            if not (rCount <= 12 and gCount <= 13 and bCount <= 14):
                valid = False

        if valid == True:
            possTot += gNumber

    return possTot

def day2p2():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    powTot = 0

    for line in lines:
        valid = True
        gNumber = re.findall(r'\d+:', line)
        gNumber = int(gNumber[0].strip(":"))
        game = line.split(": ")[1]
        sets = game.split("; ")
        rMax = 0
        gMax = 0
        bMax = 0

        for s in sets:
            reds = re.findall(r'\d+ red', s)
            rCount = sum([int((x.split(" ")[0])) for x in reds])
            rMax = max(rCount, rMax)

            greens = re.findall(r'\d+ green', s)
            gCount = sum([int((x.split(" ")[0])) for x in greens])
            gMax = max(gCount, gMax)

            blues = re.findall(r'\d+ blue', s)
            bCount = sum([int((x.split(" ")[0])) for x in blues])
            bMax = max(bCount, bMax)

        power = rMax*bMax*gMax
        powTot += power
    return powTot

print(day2p2())