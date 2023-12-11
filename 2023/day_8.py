from collections import OrderedDict

with open("input.txt", "r") as f:
    input = f.read()

lines = input.splitlines()
import random


directions, network = lines[0], lines[2:]

nodes = {}


for node in network:
    origin, left_right = node.split("=")
    nodes[origin.strip()] = tuple((left_right.strip()[1:4], left_right.strip()[6:9]))
    node_a, node_b = nodes[origin.strip()]


# Start Nodes
current_nodes = []
start_pos = []
for key in nodes.keys():
    if key[-1] == "A":
        current_nodes.append(key)
        start_pos.append(key)
current_nodes = tuple(current_nodes)
assert len(nodes) == len(network)

# End Node
end_node = "ZZZ"
counter = 0
combins = {node: [] for node in start_pos}
n_steps = {node: [0] for node in start_pos}

# Visited state tracker
visited_combinations = {"L": {}, "R": {}}
for i in range(15):
    # print(counter)
    for c in directions:
        counter += 1
        # if current_nodes not in visited_combinations[c].keys():
        next_nodes = []
        for i, current_node in enumerate(current_nodes):
            if c == "L":
                next_nodes.append(nodes[current_node][0])
            elif c == "R":
                next_nodes.append(nodes[current_node][1])
            if next_nodes[-1][-1] == "Z":
                print("Number of steps", counter)
                print("Starting Position", start_pos[i])
                print("End node", next_nodes[-1])
                n_steps[start_pos[i]].append(counter - n_steps[start_pos[i]][-1])

                if next_nodes[-1] not in combins[start_pos[i]]:
                    combins[start_pos[i]].append(next_nodes[-1])
            # visited_combinations[c][current_nodes] = tuple(next_nodes)
        current_nodes = tuple(next_nodes)
        if sum([node[-1] == "Z" for node in current_nodes]) == len(current_nodes):
            print(counter)
            assert False
        # else:
        #     current_nodes = visited_combinations[c][current_nodes]
# Find the lcm
import math

smallest_factor = []

lcm = 1
for k in n_steps:
    print(n_steps[k])
    smallest_factor.append(n_steps[k][1])
for el in smallest_factor:
    lcm = math.lcm(lcm, el)

print(lcm)

# {'SLA': ['RPZ'], 'AAA': ['ZZZ'], 'LVA': ['SFZ'], 'NPA': ['HKZ'], 'GDA': ['STZ'], 'RCA': ['CMZ']}
