import re
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy
import sys
import scipy as sp
sys.setrecursionlimit(2000)

alreadyDone = set()
connections = {}
cutConnections = {}
group1 = set()
group2 = set()
edges = set()
cuts = []
comps = []
possCuts = []


def getCuts(c1, c2, c3):
    global cutConnections
    cutConnections = copy.deepcopy(connections)
    group1.clear()
    group2.clear()

    cutConnections[c1[0]].discard(c1[1])
    cutConnections[c1[1]].discard(c1[0])
    cutConnections[c2[0]].discard(c2[1])
    cutConnections[c2[1]].discard(c2[0])
    cutConnections[c3[0]].discard(c3[1])
    cutConnections[c3[1]].discard(c3[0])

    group1.add(c1[0])
    group2.add(c1[1])

    getConnections(c1[0], group1)
    getConnections(c1[1], group2)

    if len(group1) + len(group2) == len(comps) and len(group1.intersection(group2)) == 0:
        return len(group1) * len(group2)

    return -1


def getConnections(component, group):
    for c in cutConnections[component]:
        if c not in group:
            group.add(c)
            getConnections(c, group)


def getVisualisation():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    for line in lines:
        components = re.findall(r"\b\w+\b", line)

        if components[0] not in connections:
            connections[components[0]] = set()
            comps.append(components[0])

        for i in range(1, len(components)):
            connections[components[0]].add(components[i])
            if components[i] not in connections:
                connections[components[i]] = {components[0]}
                comps.append(components[i])
            else:
                connections[components[i]].add(components[0])
            if components[0] < components[i]:
                edges.add((components[0], components[i]))
            else:
                edges.add((components[i], components[0]))

    G = nx.Graph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, scale=2)

    plt.figure(figsize=(18, 9))
    d = dict(G.degree)
    nx.draw(G, pos=pos, with_labels=False)
    for node, (x, y) in pos.items():
        plt.text(x, y, node, fontsize=d[node], ha='center', va='center')

    nodes = nx.draw_networkx_nodes(G, pos)
    nodes.set_edgecolor('black')

    plt.savefig("graph.svg", dpi=1000)


def day25():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

    ines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    for line in lines:
        components = re.findall(r"\b\w+\b", line)

        if components[0] not in connections:
            connections[components[0]] = set()
            comps.append(components[0])

        for i in range(1, len(components)):
            connections[components[0]].add(components[i])
            if components[i] not in connections:
                connections[components[i]] = {components[0]}
                comps.append(components[i])
            else:
                connections[components[i]].add(components[0])
            if components[0] < components[i]:
                edges.add((components[0], components[i]))
            else:
                edges.add((components[i], components[0]))

    return getCuts(('kzh', 'rks'), ('dgt', 'tnz'), ('ddc', 'gqm'))


print(getVisualisation())
