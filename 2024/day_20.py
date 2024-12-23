with open("input.txt") as f:
    input = f.read().splitlines()


def make_map(input):
    graph_map = {}

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(len(input[0])):
        for j in range(len(input[1])):
            if input[i][j] == "S":
                start = (i, j)
            if input[i][j] == "E":
                end = (i, j)
            if input[i][j] in [".", "S", "E"]:
                graph_map[(i, j)] = []
    
    for k in graph_map:
        level = []
        for d in dirs:
            next_d = (k[0]+d[0], k[1]+d[1])
            if next_d in graph_map:
                graph_map[k].append(next_d)
            
    return graph_map, start, end

def bfs_normal_path(graph, start, end):
    path = [start]
    assert len(graph[start]) == 1
    next_el = graph[start][0]
    prev_el = start
    while next_el != end:
        path.append(next_el)    

        maybe_next = graph[next_el]
        if prev_el in maybe_next:
            maybe_next.remove(prev_el)
        assert len(maybe_next) ==1
        prev_el = next_el

        next_el = maybe_next[0]
    path.append(end)

    return path

def count_cheats(path, graph):
    cheat_dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    time_dir = {}
    for i, step in enumerate(path):
        for c_dir in cheat_dirs:
            c_next = (step[0]+c_dir[0], step[1]+c_dir[1])
            if c_next in path:
                time_saved = path.index(c_next) - i - 2

                if time_saved in time_dir and time_saved > 0:
                    time_dir[time_saved] += 1
                elif time_saved > 0:
                    time_dir[time_saved] = 1
    return time_dir

def count_cheats_p2(path, graph):
    
    time_dir = {}
    lookup_dict = {p:i for i, p in enumerate(path)}
    #lookup_path = set(path)
    for i, step in enumerate(path):
        #print(i, len(path))
        for j, next_step in enumerate(path[i+1:]):
            dist = abs(step[0]- next_step[0]) + abs(step[1] -next_step[1])
            if dist < 21:
                time_saved = j + 1- dist
                if time_saved in time_dir and time_saved > 0:
                    time_dir[time_saved] += 1
                elif time_saved > 0:
                    time_dir[time_saved] = 1
     
    return time_dir


def part_1(input):
    graph, start, end = make_map(input)

    path = bfs_normal_path(graph, start, end)
    print(len(path))

    time_saved = count_cheats(path, graph)
    print(time_saved)
    p1= 0
    for t in time_saved:
        if t >= 100:
            p1 += time_saved[t]

    print("part 1", p1)


def part_2(input):
    graph, start, end = make_map(input)

    path = bfs_normal_path(graph, start, end)
    print(len(path))

    time_saved = count_cheats_p2(path, graph)
    
    #print(time_saved)
    p2= 0

    for t in time_saved:
        if t >= 100:
            p2 += time_saved[t]
            print(t, time_saved[t])

 
    print("part 2", p2)
    

part_2(input)