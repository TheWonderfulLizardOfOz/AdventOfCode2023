import math

highs = {}

modules = {}
cons = {}
flipFlops = {}
queue = []
lowCount = 0
highCount = 0


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def sendPulses(sentFrom, moduleName, pulse):
    global lowCount, highCount

    if pulse == "low":
        lowCount += 1
    else:
        highCount += 1

    if moduleName == connectsToRX:
        for h in highs:
            if not all(cons[h][c] == "high" for c in cons[h]):
                if len(highs[h]) == 0:
                    highs[h].append(i)
                elif highs[h][-1] != i:
                    highs[h].append(i)

    if moduleName not in modules:
        return

    if moduleName in cons:
        cons[moduleName][sentFrom] = pulse
        if all(cons[moduleName][cName] == "high" for cName in cons[moduleName]) and pulse == "high":
            newPulse = "low"
        else:
            newPulse = "high"
    elif moduleName in flipFlops:
        if pulse == "high":
            return
        elif flipFlops[moduleName] == "off":
            flipFlops[moduleName] = "on"
            newPulse = "high"
        else:
            flipFlops[moduleName] = "off"
            newPulse = "low"
    else:
        newPulse = pulse

    for connector in modules[moduleName]:
        queue.append((moduleName, connector, newPulse))


def pushButton():
    queue.append(("button", "broadcaster", "low"))

    while len(queue) > 0:
        sentFrom, currentModule, currentPulse = queue.pop(0)
        sendPulses(sentFrom, currentModule, currentPulse)


def day20p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    for line in lines:
        moduleName, connection = line.split(" -> ")
        if moduleName[0] == '&':
            moduleName = moduleName[1:]
            cons[moduleName] = {}
        elif moduleName[0] == '%':
            moduleName = moduleName[1:]
            flipFlops[moduleName] = "off"

        modules[moduleName] = connection.split(", ")

    for c in cons:
        for m in modules:
            if c in modules[m]:
                cons[c][m] = "low"

    for i in range(10000):
        pushButton()

    return highCount*lowCount


def day20p2():
    global i, connectsToRX
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    for line in lines:
        moduleName, connection = line.split(" -> ")
        if moduleName[0] == '&':
            moduleName = moduleName[1:]
            cons[moduleName] = {}
        elif moduleName[0] == '%':
            moduleName = moduleName[1:]
            flipFlops[moduleName] = "off"

        modules[moduleName] = connection.split(", ")

    for c in cons:
        for m in modules:
            if c in modules[m]:
                cons[c][m] = "low"

    for m in modules:
        if "rx" in modules[m]:
            connectsToRX = m
            break

    for m in modules:
        if connectsToRX in modules[m]:
            highs[m] = []

    for i in range(1, 10001):
        pushButton()

    diffs = []
    for h in highs.values():
        diffs.append(h[1] - h[0])
    a = diffs[0]
    for i in range(1, len(diffs)):
        a = lcm(a, diffs[i])
    return a


print(day20p2())
