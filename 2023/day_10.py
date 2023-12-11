import sys

sys.setrecursionlimit(15000)
with open("input.txt") as f:
    input = f.read()

FIELD = []

START_ELEM = "|"
# 0. Parse input
for i, elem in enumerate(input.splitlines()):
    if "S" in elem:
        starting_pos = (i, elem.index("S"))
        elem = elem.replace("S", START_ELEM)
    FIELD.append(list(elem))

print(starting_pos)
# We notice the input is square
# assert len(field) == len(field[0])
assert FIELD[starting_pos[0]][starting_pos[1]] == START_ELEM

COMPATS = {
    "|": {(-1, 0): ["|", "F", "7"], (1, 0): ["|", "L", "J"]},
    "-": {(0, 1): ["-", "7", "J"], (0, -1): ["-", "L", "F"]},
    "L": {(-1, 0): ["|", "F", "7"], (0, 1): ["-", "7", "J"]},
    "J": {(-1, 0): ["|", "F", "7"], (0, -1): ["-", "L", "F"]},
    "7": {(0, -1): ["-", "L", "F"], (1, 0): ["|", "L", "J"]},
    "F": {(0, 1): ["-", "7", "J"], (1, 0): ["|", "L", "J"]},
    ".": {},
}


# 1. Create a function given a cube centered around a position can
# Return the list of available paths
def get_children(field, position):
    children = []
    x, y = position[0], position[1]
    possibilities = COMPATS[field[x][y]]
    for k, v in possibilities.items():
        if position[0] == len(field) and k[0] > 0:
            continue
        if position[0] == 0 and k[0] < 0:
            continue
        if position[1] == len(field[0]) and k[1] > 0:
            continue
        if position[1] == 0 and k[0] < 0:
            continue
        print(x + k[0], y + k[1])
        print(field[x + k[0]][y + k[1]], v)
        if field[x + k[0]][y + k[1]] in v:
            children.append((x + k[0], y + k[1]))
    print("Inside get children")
    print(position)
    print(children)
    return children


# 2. Recursively traverse the graph breaking when we reach the end of a path
# We need to make a modification to travel the graph in a direction.
def build_graph(graph, field, start_pos):
    # Stopping condition: We reach a node without any children or we already visited node.
    if start_pos in graph.keys():
        return {}
    children = get_children(field, start_pos)
    graph[start_pos] = children

    for child in children:
        graph = graph | build_graph(graph, field, child)
    return graph


import heapq


# 3. Dumb version for each node we find the shortest path to starting node
def shortest_path(graph, start, end):
    priority_queue = [(0, start)]
    distances = {node: float("inf") for node in graph.keys()}
    distances[start] = 0

    previous = {node: None for node in graph.keys()}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            while previous[current_node] is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.append(start)
            return path[::-1], distances[end]

        for neighbor in graph[current_node]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return [], float("inf")


graph = build_graph({}, FIELD, starting_pos)

# Part 1
"""
distances = []
for node in graph.keys():
    distances.append(shortest_path(graph, starting_pos, node)[1])
"""

# Part 2
# For each tile not in the loop
print("PAART2")
tiles_per_row = []
count_included = 0
for i in range(len(FIELD)):
    row = []
    to_add = 0
    for node in graph.keys():
        if node[0] == i:
            row.append(node[1])
    row = sorted(row)
    for i, tile in enumerate(row):
        if i % 2 == 1:
            to_add += (row[i] - row[i - 1]) - 1
    count_included += to_add
    tiles_per_row.append(row)

# print(count_included)
# print(graph)
# We want to travel through the loop
# Registering the min_x study (current_x -min_x)


# 1. Travel through graph in a directed way
# To do this we can keep in memory the visited nodes
# The travel direction doesn't matter
from scipy.spatial import ConvexHull


def travel_graph(graph, starting_pos):
    prev_node = starting_pos
    current_node = graph[starting_pos][0]
    next_node = None
    count = 0
    corners = [starting_pos]
    # We need to find the squares or rectangles with sufficient area
    # When it's empty set values appropriatly
    # Otherwise increase as needed
    while current_node != starting_pos:
        # Get our current row
        y_axis = current_node[0]
        # Make sure we don't go back
        if prev_node in graph[current_node]:
            graph[current_node].remove(prev_node)
        next_node = graph[current_node][0]
        # Update positions
        if FIELD[current_node[0]][current_node[1]] in ["L", "7", "J", "F"]:
            count += 1
            corners.append(current_node)

        # Check is set of corners is closed
        print("Current Node")
        print(FIELD[current_node[0]][current_node[1]])
        print(current_node)
        prev_node = current_node
        current_node = graph[current_node][0]
    print(count)
    return corners


print("This is the starting pos")
print(starting_pos)
corners = travel_graph(graph, starting_pos)

from matplotlib.path import Path

hull_path = Path(corners)

to_check = []
for i in range(len(FIELD[0])):
    for j in range(len(FIELD[1])):
        if (i, j) not in graph.keys():
            to_check.append((i, j))

print(sum(hull_path.contains_points(to_check)))
