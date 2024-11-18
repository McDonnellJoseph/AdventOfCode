with open("full_input.txt") as f:
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
    #candidates.remove(path[-1])

    # if we have at least 2 pre-decessors
    if len(path) == 3:
        # compute difference
        diff = (path[-1][0] - path[-3][0], path[-1][1] - path[-3][1])
        # Moving horizontally
        if abs(diff[0]) == 2:
            # Moving right
            if diff[0] < 0 and node[0] < len(lines)-1:
                candidates.remove((node[0]+1, node[1]))
            # Moving left
            elif diff[0] > 0:
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


def min_dict(d, Q):
    filtered_dict = {k: d[k] for k in Q if k in d}
    return min(filtered_dict, key=filtered_dict.get)

def djikstra(G):
    Q  = [g for g in G]
    dist = {g: float("inf") for g in G}
    prev = {g: None for g in G}

    dist[(0,0)] = 0

    while Q:
        u = min_dict(dist, Q)
        Q.remove(u)
        if u == (len(lines)-1, len(lines)-1):
            return dist, prev
        for neighbor in get_nodes(G, u, prev):
            alt = dist[u] + G[u][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
    return dist, prev

dist, previously = djikstra(G)

def compute_weight(preds):
    total_weight = 0 
    node = (len(lines)-1, len(lines)-1)

    while node != (0, 0):
        print(node)
        prev = preds[node]
        total_weight += G[node][prev]
        node = prev
    return total_weight

print(compute_weight(previously))