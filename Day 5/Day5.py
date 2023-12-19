import re


class Tree:
    def __init__(self, values, children):
        self.values = values
        self.children = children


def yToX(val, lines, search):
    start = 0
    for i in range(len(lines)):
        if lines[i] == search:
            start = i + 1

    for i in range(start, len(lines)):
        nums = [int(num) for num in re.findall(r'\d+', lines[i])]
        if len(nums) == 0:
            return val

        destRange = nums[0]
        startRange = nums[1]
        rangeLength = nums[2]

        if destRange <= val < destRange + rangeLength:
            diff = val - destRange
            return diff + startRange

    return val


def xToY(vals, lines, search):
    start = 0
    for i in range(len(lines)):
        if lines[i] == search:
            start = i + 1

    result = dict((x, x) for x in vals)
    for i in range(start, len(lines)):
        nums = [int(num) for num in re.findall(r'\d+', lines[i])]
        if len(nums) == 0:
            return result

        destRange = nums[0]
        startRange = nums[1]
        rangeLength = nums[2]

        for val in vals:
            diff = val - startRange
            if 0 <= diff <= rangeLength - 1:
                result[val] = destRange + diff
    return result


def smallestLocs(lines, smallest):
    start = 0
    for i in range(len(lines)):
        if lines[i] == "humidity-to-location map:":
            start = i + 1

    smalls = []
    for i in range(start, len(lines)):
        nums = [int(num) for num in re.findall(r'\d+', lines[i])]

        if nums[0] <= smallest:
            if nums[0] + nums[2] > smallest:
                smalls.append([nums[0], nums[1], -(nums[0] - smallest)])
            else:
                smalls.append(nums)

    smalls = sorted(smalls, key=lambda x: x[0], reverse=False)
    if smalls[0][0] != 0:
        smalls.append([0, 0, smalls[0][0]])
    return smalls


def seedToLoc(seeds, lines):
    seedSoil = xToY(seeds, lines, "seed-to-soil map:")
    soils = [seedSoil[x] for x in seedSoil]

    soilFert = xToY(soils, lines, "soil-to-fertilizer map:")
    ferts = [soilFert[x] for x in soilFert]

    fertWater = xToY(ferts, lines, "fertilizer-to-water map:")
    waters = [fertWater[x] for x in fertWater]

    waterLight = xToY(waters, lines, "water-to-light map:")
    lights = [waterLight[x] for x in waterLight]

    lightTemp = xToY(lights, lines, "light-to-temperature map:")
    temps = [lightTemp[x] for x in lightTemp]

    tempHumid = xToY(temps, lines, "temperature-to-humidity map:")
    humidity = [tempHumid[x] for x in tempHumid]

    humidLoc = xToY(humidity, lines, "humidity-to-location map:")
    locs = [humidLoc[x] for x in humidLoc]

    return locs


def getConnectors(val, lines, search):
    maps = []
    start = 0
    for i in range(len(lines)):
        if lines[i] == search:
            start = i + 1

    for i in range(start, len(lines)):
        if lines[i] == "":
            break
        maps.append([int(num) for num in re.findall(r'\d+', lines[i])])

    maps = sorted(maps, key=lambda x: x[1], reverse=False)
    newMaps = []
    if maps[0][1] != 0:
        newMaps.append([0, 0, maps[0][1]])

    for i in range(len(maps) - 1):
        currentMax = maps[i][1] + maps[i][2]
        if maps[i + 1][1] != currentMax:
            newMaps.append([currentMax, currentMax, maps[i + 1][1] - currentMax])

    high = maps[-1][1] + maps[-1][2]
    maxX = 9999999999
    newMaps.append([high, high, maxX - high])

    maps = maps + newMaps
    print(maps)


def day5p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    seeds = re.findall(r'\d+', lines[0])
    seeds = [int(seed) for seed in seeds]

    locs = seedToLoc(seeds, lines)
    return min(locs)


def day5p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    seeds = re.findall(r'\d+', lines[0])
    seeds = [(int(seeds[i]), int(seeds[i + 1])) for i in range(len(seeds)) if i % 2 == 0]
    seeds = sorted(seeds, key=lambda x: x[1], reverse=False)
    found = False
    i = 11555000
    while i >= 10000000 and not found:
        i -= 1
        humid = yToX(i, lines, "humidity-to-location map:")
        temp = yToX(humid, lines, "temperature-to-humidity map:")
        light = yToX(temp, lines, "light-to-temperature map:")
        water = yToX(light, lines, "water-to-light map:")
        fert = yToX(water, lines, "fertilizer-to-water map:")
        soil = yToX(fert, lines, "soil-to-fertilizer map:")
        possSeed = yToX(soil, lines, "seed-to-soil map:")
        for seed in seeds:
            if possSeed < seed[0]:
                break
            elif seed[0] <= possSeed < seed[0] + seed[1]:
                print(i)
                break

    return i

    # smallest = min(seedToLoc([seed[0] for seed in seeds], lines))
    # smalls = smallestLocs(lines, smallest)
    #
    # tree = Tree(smallest, [Tree(small, None) for small in smalls])
    # print([child.values for child in tree.children])
    #
    # print(getConnectors(1, lines, "temperature-to-humidity map:"))


print(day5p2())
