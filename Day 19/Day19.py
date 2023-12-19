import re

workflows = {}
parts = []


def createWorkflow(line):
    workflowName, rules = tuple(re.findall(r"(.*){(.*)}", line)[0])
    workflows[workflowName] = []
    rules = re.findall(r"(([xmas])(.)(\d+).(\w+))|(\w+)", rules)
    for rule in rules:
        if rule[0] != '':
            workflows[workflowName].append((rule[1], rule[2], int(rule[3]), rule[4]))
        else:
            workflows[workflowName].append((rule[-1]))


def createPart(line):
    nums = [int(num) for num in re.findall(r"\d+", line)]
    parts.append({'x': nums[0], 'm': nums[1], 'a': nums[2], 's': nums[3]})


def getProduct(part):
    prod = 1
    for r in part.values():
        prod *= (r[1] - r[0] + 1)
    return prod


def checkAccepted(part, wf):
    rules = workflows[wf]
    for i in range(len(rules) - 1):
        category, op, num, result = rules[i]
        categoryVal = part[category]
        if (op == '<' and categoryVal < num) or (op == '>' and categoryVal > num):
            if result == 'R':
                return False
            elif result == 'A':
                return True
            else:
                return checkAccepted(part, result)

    other = rules[-1]
    if other == 'R':
        return False
    elif other == 'A':
        return True
    else:
        return checkAccepted(part, other)


def rangeAcceptCount(part, wf):
    rules = workflows[wf]
    tot = 0
    for i in range(len(rules) - 1):
        category, op, num, result = rules[i]
        categoryValMin = part[category][0]
        categoryValMax = part[category][1]

        if (op == '<' and categoryValMax < num) or (op == '>' and categoryValMin > num):
            if result == 'A':
                tot += getProduct(part)
            elif result != 'R':
                tot += rangeAcceptCount(part, result)
            return tot

        elif (op == '<' and categoryValMin < num) or (op == '>' and categoryValMax > num):
            cutPart = part.copy()

            if op == '<':
                cutPart[category] = (categoryValMin, num - 1)
                part[category] = (num, categoryValMax)
            else:
                cutPart[category] = (num + 1, categoryValMax)
                part[category] = (categoryValMin, num)

            if result == 'A':
                tot += getProduct(cutPart)
            elif result != 'R':
                tot += rangeAcceptCount(cutPart, result)

    other = rules[-1]
    if other == 'A':
        tot += getProduct(part)
    elif other != 'R':
        tot += rangeAcceptCount(part, other)

    return tot


def day19p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    work = True
    for line in lines:
        if line == "":
            work = False
            continue
        if work:
            createWorkflow(line)
        else:
            createPart(line)

    tot = 0
    for part in parts:
        if checkAccepted(part, "in"):
            for val in part.values():
                tot += val
    return tot


def day19p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    for line in lines:
        if line == "":
            break
        createWorkflow(line)

    return rangeAcceptCount({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, "in")


print(day19p2())
