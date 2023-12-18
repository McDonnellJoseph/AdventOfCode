with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
G = dict()

# 1. Create Graph
for i in range(len(lines)):
    for j in range(len(lines[0])):
        weight = int(lines[i][j])
        pos = (i, j)
        if pos not in G.keys():
            G[pos] = {}
        if i > 0:
            G[pos][(i - 1, j)] = weight
        if i < len(lines) - 1:
            G[pos][(i + 1, j)] = weight

        if j > 0:
            G[pos][(i, j - 1)] = weight

        if j < len(lines[0]) - 1:
            G[pos][(i, j + 1)] = weight

import sys

sys.setrecursionlimit(int(1e6))


def get_nodes(G, path):
    last = path[-1]
    candidates = list(G[last])
    print("These", candidates)
    # if we have at least 2 pre-decessors
    if len(path) > 2:
        # compute difference
        diff = (last[0] - path[-3][0], last[1] - path[-3][1])

        if abs(diff[0]) > 2 or abs(diff[1]) > 2:
            # Moving right
            if last[0] > path[-3][0]:
                assert last[0] - 3 == path[-3][0]
                caca = (last[0] + 1, last[1])
                candidates.remove(caca)
            # Moving left
            elif last[0] < path[-3][0]:
                assert last[0] + 3 == path[-3][0]
                caca = (last[0] - 1, last[1])
                candidates.remove(caca)
            # Moving up
            elif last[1] < path[-3][1]:
                assert last[1] + 3 == path[-3][1]
                caca = (last[0], last[1] - 1)
                candidates.remove(caca)
            # Moving down
            elif last[1] > path[-3][1]:
                assert last[1] - 3 == path[-3][1]
                caca = (last[0], last[1] + 1)
                candidates.remove(caca)
    if path[-1] in candidates:
        candidates.remove(path[-1])
    return candidates


def brute_force(G, path, total, start, dest):
    # We are visiting a node let's add it to the path
    path.append(start)
    # Stopping condition
    if start == dest:
        return path, total
    elif start in path:
        return None, None

    else:
        # Retreive nodes we can travel to
        allowed = get_nodes(G, path)
        alternatives = []
        totals = []
        for node in allowed:
            total += G[start][node]
            new_p, new_t = brute_force(G, path, total, node, dest)
            alternatives.append(new_p)
            totals.append(total)
        return alternatives, totals


print(brute_force(G, [], 2, (0, 0), (len(lines) - 1, len(lines[0]) - 1)))
