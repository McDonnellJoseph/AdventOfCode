with open("input.txt") as f:
    input = f.read().splitlines()

maze = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "S":
            start_pos = (i, j)
            print("THis is the start pos", start_pos)
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
    print(node_dir)
    if dir == (0, 0):
        # fetch last dir

        last_node_dir = preds[node_dir]
        print(last_node_dir)
        last_node, last_dir = last_node_dir
        assert last_dir != (0, 0)
        print("Hello")
        if last_dir[0] != 0:
            print("here")
            if ((node[0], node[1] + 1), (0, 1)) in G:
                print("Appending")
                candidates.append(((node[0], node[1] + 1), (0, 1)))
            if ((node[0], node[1] - 1), (0, -1)) in G:
                print("Appending")
                candidates.append(((node[0], node[1] - 1), (0, -1)))
        else:
            if ((node[0] + 1, node[1]), (1, 0)) in G:
                print("Appending")
                candidates.append(((node[0] + 1, node[1]), (1, 0)))
            if ((node[0] - 1, node[1]), (0, -1)) in G:
                print("Appending")
                candidates.append(((node[0] - 1, node[1]), (-1, 0)))
    else:
        print("here")
        if ((node[0] + dir[0], node[1] + dir[1]), dir) in G:
            candidates.append(((node[0] + dir[0], node[1] + dir[1]), dir))
        candidates.append((node, (0, 0)))
        print("candidates", candidates)
    return candidates


def min_dict(d, Q):
    filtered_dict = {k: d[k] for k in Q if k in d}
    return min(filtered_dict, key=filtered_dict.get)


def djikstra(G, start_pos, end_pos):
    Q = list(G).append((start_pos, (0, 1)))
    dist = {g: float("inf") for g in G}
    prev = {g: None for g in G}
    for g in G:
        print(g)
    print(Q)
    if (start_pos, (0, 1)) not in Q:
        assert False
    dist[(start_pos, (0, 1))] = 0
    prev[(start_pos, (0, 1))] = (start_pos[0], start_pos[1]), (None, None)

    while Q:
        u = min_dict(dist, Q)
        print("Min", u, "COst", dist[u])
        Q.remove(u)
        if u[0] == end_pos:
            return dist, prev
        for candidate in get_nodes(G, u, prev):
            alt = dist[u] + G[candidate]
            if alt < dist[candidate]:
                dist[candidate] = alt
                prev[candidate] = u
    return dist, prev


def get_path(preds, start_pos, end_pos):
    path = [end_pos]
    while path[-1] != start_pos:
        prev = preds[path[-1]]
        path.append(prev)
    return list(reversed(path))


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
path = get_path(prev, start_pos, end_pos)
print(path)
next_dir_map = {(-1, 0): "^", (1, 0): "v", (0, 1): ">", (0, -1): "<"}
output = input.copy()
dir = (0, 1)
sy, sx = start_pos
turn_count = 0
output[sy] = output[sy][:sx] + "S" + output[sy][sx + 1 :]
for i in range(len(path) - 1):
    y, x = path[i]
    next_dir = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
    if next_dir != dir:
        turn_count += 1001
    else:
        turn_count += 1
    output[y] = output[y][:x] + next_dir_map[next_dir] + output[y][x + 1 :]
    dir = next_dir
for _ in output:
    print(_)
# print(output)
print(turn_count)
