import re
import math


def day6p1():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    times = re.findall(r'\d+', lines[0])
    times = [int(time) for time in times]
    distances = re.findall(r'\d+', lines[1])
    distances = [int(d) for d in distances]
    prod = 1
    for i in range(len(times)):
        #t1 = ((-distances[i]) + (math.sqrt((distances[i] ** 2) + (4*times[i])))) / 2
        #t2 = ((-distances[i]) - (math.sqrt((distances[i] ** 2) + (4*times[i])))) / 2
        #print(t1, t2)
        tot = 0
        for j in range(times[i]):
            d = (j * times[i]) - (j**2)
            if d > distances[i]:
                tot += 1
        print(tot)
        prod *= tot
    return prod


def day6p2():
    lines = open("input.txt", "r", encoding = "utf-8").read().splitlines()
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))
    print(time, distance)
    d = distance
    t = time
    heldTime = (t + math.sqrt((t*t) - (4*d))) // 2
    maxTime =  (t - math.sqrt((t*t) - (4*d))) // 2

    print(heldTime, maxTime)
    return heldTime-maxTime


print(day6p2())
