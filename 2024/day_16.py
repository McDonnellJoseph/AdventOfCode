with open("input.txt") as f:
    input = f.read().splitlines()

maze = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "S":
            start_pos = (i, j)
            print("Tis is the start pos", start_pos)
            input[i] = input[i][:j] + "." + input[i][j + 1 :]
        if input[i][j] == "E":
            end_pos = (i, j)
            print("This is the end pos", end_pos)
            input[i] = input[i][:j] + "." + input[i][j + 1 :]

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == ".":
            if i > 0 and input[i - 1][j] == ".":
                maze[((i - 1, j), (-1, 0))] = 1
            if i < len(input) and input[i + 1][j] == ".":
                maze[((i + 1, j), (1, 0))] = 1

            if j > 0 and input[i][j - 1] == ".":
                maze[((i, j - 1), (0, -1))] = 1

            if j < len(input[0]) and input[i][j + 1] == ".":
                maze[((i, j + 1), (0, 1))] = 1
            maze[((i, j), (0, 0))] = 1000


def get_nodes(G, node_dir, preds):
    node, dir = node_dir

    candidates = []
    if dir == (0, 0):
        # fetch last dir

        for last_node_dir in preds[node_dir]:
            assert last_node_dir is not None
            last_node, last_dir = last_node_dir
            assert last_dir != (0, 0)
            if last_dir[0] != 0:
                if ((node[0], node[1] + 1), (0, 1)) in G:
                    candidates.append(((node[0], node[1] + 1), (0, 1)))
                if ((node[0], node[1] - 1), (0, -1)) in G:
                    candidates.append(((node[0], node[1] - 1), (0, -1)))
            else:
                if ((node[0] + 1, node[1]), (1, 0)) in G:
                    candidates.append(((node[0] + 1, node[1]), (1, 0)))
                if ((node[0] - 1, node[1]), (-1, 0)) in G:
                    candidates.append(((node[0] - 1, node[1]), (-1, 0)))
    else:
        if ((node[0] + dir[0], node[1] + dir[1]), dir) in G:
            candidates.append(((node[0] + dir[0], node[1] + dir[1]), dir))
        candidates.append((node, (0, 0)))
    
    return candidates


def min_dict(d, Q):
    filtered_dict = {k: d[k] for k in Q if k in d}
    return min(filtered_dict, key=filtered_dict.get)


def djikstra(G, start_pos, end_pos):
    Q = list(G)
    Q.append((start_pos, (0, 1)))
    dist = {g: float("inf") for g in G}
    prev = {g: [] for g in G}
    print("THis is the start pos")
    print(start_pos)
    shortest_paths = [prev]
    if (start_pos, (0, 1)) not in Q:
        assert False
    dist[(start_pos, (0, 1))] = 0
    prev[(start_pos, (0, 1))] = [((start_pos[0], start_pos[1]), (None, None))]

    while Q:
        u = min_dict(dist, Q)
        #print("Min", u, "COst", dist[u])
        Q.remove(u)
        if u[0] == end_pos:
            print("Ending dist", dist[u])
            return dist, prev
        for candidate in get_nodes(G, u, prev):
            alt = dist[u] + G[candidate]
            if alt < dist[candidate]:
                dist[candidate] = alt
                prev[candidate] = [u]
            elif alt == dist[candidate]:
                prev[candidate].append(u)
    return dist, prev
 

def get_path(preds, start_pos, end_pos):
    path = {end_pos[0]}
    node = end_pos
    while node != start_pos:
        node = preds[node][0]
        path.add(node[0])
        for i in range(1, len(preds[node])):
            path = path.union(get_path(preds, start_pos, preds[node][i]))

    return path


def get_cost(path):
    dir = (0, 1)
    turn = 0
    not_turn = 0
    for i in range(1, len(path)):
        next_dir = (path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])
        if next_dir != dir:
            turn += 1
        else:
            not_turn += 1
        dir = next_dir
    return (turn, not_turn)


dist, prev = djikstra(maze, start_pos, end_pos)


path = get_path(prev, (start_pos,(0, 1)), (end_pos, (0,1)))
print(len(path))
