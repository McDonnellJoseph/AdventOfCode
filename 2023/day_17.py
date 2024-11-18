with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
G = dict()

"""
unvisited_nodes = set()
distance_from_start = dict()
# Create graph
for i in range(len(lines)):
    for j in range(len(lines[0])):
        weight = int(lines[i][j])
        G[(i, j)]=weight
        unvisited_nodes.add((i, j))
        if (i, j) == (0, 0):
            distance_from_start[(i, j)] = 0
        else:
            distance_from_start[(i, j)] = float("inf")

assert len(lines) == len(lines[0])
# Attempt with Floyd Warshall
n_vertices = len(lines) * len(lines)
# Set cost of going from one edge to another 
dist = [[float("inf") for i in range(n_vertices)] for j in range(n_vertices)]

for vertice in G:
    weight = G[vertice]
    print(vertice)
    if vertice[0] > 0:
        dist[vertice[0] * len(lines) + vertice[1]][(vertice[0] -1)*len(lines) + vertice[1]] = weight
    if vertice[0] < len(lines) -1:
        dist[vertice[0] * len(lines) + vertice[1]][(vertice[0] +1) * len(lines) + vertice[1]] = weight
    if vertice[1] > 0:
        dist[vertice[0] * len(lines) + vertice[1]][vertice[0] * len(lines) + vertice[1] -1]= weight
    if vertice[1] < len(lines) -1:
        dist[vertice[0] * len(lines) + vertice[1]][vertice[0]  * len(lines)+ vertice[1] + 1] = weight

    dist[vertice[0] * len(lines) + vertice[1]][vertice[0]*len(lines)+vertice[1]] = 0

for k in range(n_vertices):
    for i in range(n_vertices):
        for j in range(n_vertices):
            print("toto")
print("Size of dist ", len(dist) * len(dist[0]))
#dist = [[G[(i, j)] for j in range(len(lines[0]))] for i in range(len(lines))]

print(dist[0])
for i in range(len(lines[0])):
    dist[i][i] = 0
for edge in G:
    pass



"""
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

sys.setrecursionlimit(int(1e9))
from functools import lru_cache

def get_nodes(G, node, predecessors):
    path = [node]

    if predecessors[node]:
        last = predecessors[node]
        path.append(last)    
        
        if predecessors[last]:
            second_last = predecessors[last]
            path.append(second_last)

    candidates = list(G[node])

    # remove candidate that would involve u-turn 
    candidates.remove(path[-1])

    # if we have at least 2 pre-decessors
    if len(path) == 3:
        # compute difference
        diff = (last[0] - predecessors[-3][0], last[1] - predecessors[-3][1])

        # Moving horizontally
        if abs(diff[0]) == 2:
            # Moving right
            if diff[0] > 0 and node[0] < len(lines)-1:
                candidates.remove((node[0]+1, node[1]))
            # Moving left
            elif diff[0] < 0:
                if node[0] > 0:
                    candidates.remove((node[0]-1, node[1]))

        # Moving Vertically
        elif abs(diff[1])==2:
            # Moving down
            if diff[1] > 0 and node[1] < len(lines)-1:
                candidates.remove((node[0], node[1]+1))
            # Moving up
            elif diff[1] < 0 and node[1] > 0:
                candidates.remove((node[0], node[1]-1))           

    return candidates


def min_dict(d):
    return min(d, key=d.get)
def djikstra(G):
    Q  = [g for g in G]
    dist = {g: float("inf") for g in G}
    prev = {g: None for g in G}

    dist[(0,0)] = 0

    while Q:
        u = min_dict(dist)
        Q.remove(u)

        for neighbor in get_nodes(G, node, prev):
            alt = dist[u] + G[neighbor]


def iterative(G, start, dest):
    all_predss = [([start], 0)]
    total_reached = []
    best_total = 140
    
    while all_predss:
        # Explore
        candidate_min_total = {}
        new_predss = []
        for predecessors, total in all_predss:
            candidates = get_nodes(G, predecessors)
            print("candidates", predecessors, candidates)
            for candidate in candidates:
                candidate_total = total + G[predecessors[-1]][candidate]

                if candidate == dest:
                    print("Reached Destination")
                    total_reached.append(candidate_total)
                    print(candidate_total)
                    assert False
                    if best_total > candidate_total:
                        print(candidate_total)
                        best_total = candidate_total

                elif candidate not in candidate_min_total.keys():
                    candidate_min_total[candidate] = (predecessors, candidate_total)
                    new_predss.append((predecessors + [candidate], candidate_total))

                elif candidate_min_total[candidate][1] > candidate_total:
                    print(all_predss)
                    print("This is the candidate", candidate)
                    print(candidate_min_total[candidate])
                    candidate_min_total[candidate] = (predecessors, candidate_total)
                    new_predss.append((predecessors + [candidate], candidate_total))
          
        all_predss = new_predss
        for predecessors in all_predss:
            assert len(predecessors[0]) == len(all_predss[0][0])
    return best_total


print(iterative(G, (0, 0), (13, 13)))
def brute_force(G, predecessors, total, start, dest, best):
    # We are visiting a node let's add it to the predecessors
    
    predecessors.append(start)
    # Stopping condition
    if start == dest:
        print(predecessors)
        print(len(predecessors), total)
        if total < best:
            best = total
            BEST_TOTAL = total
        print(total)
        end_reached.append(total)
        return predecessors, total, best
    else:
        # Retreive nodes we can travel to
        allowed = get_nodes(G, predecessors)
        alternatives = []
        totals = []
        for node in allowed:
            assert max(abs(node[0] - start[0]), abs(node[1] -start[1])) == 1
            new_total = total + G[start][node]
            new_preds = predecessors.copy() 

            if node in predecessors or new_total > best:  
                continue
            if new_total > best:
                assert False
            new_p, new_t, maybe_best = brute_force(G, new_preds, new_total, node, dest, best)
            if maybe_best < best:
                best = maybe_best
            alternatives.append(new_p)
            totals.append(new_t)
        return alternatives, totals, best

#print(brute_force(G, [], 0, (0, 0), (len(lines) - 1, len(lines[0]) - 1), 103) )
#print(brute_force(G, [], 0, (0, 0), (6, 6), 60) )

#print(end_reached)
#print("#################")
