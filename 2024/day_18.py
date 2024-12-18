import heapq
with open("input.txt") as f:
    input = f.read().splitlines()

DIM = 70

def load_grid(n_bytes):
    with open("input.txt") as f:
        input = f.read().splitlines()
    Bytes = []

    for byte in input[:n_bytes]:
        x, y = byte.split(",")
        Bytes.append((int(y), int(x)))

    grid = {}

    for i in range(DIM+1):
        for j in range(DIM+1):
            if (i, j) not in Bytes:
                grid[(i, j)] = []

                if i > 0 and (i-1, j) not in Bytes:
                    grid[(i, j)].append((i-1, j))

                if i < DIM and (i+1, j) not in Bytes:
                    grid[(i, j)].append((i+1, j))
                
                if j > 0 and (i, j-1) not in Bytes:
                    grid[(i, j)].append((i, j-1))

                if j < DIM and (i, j+1) not in Bytes:
                    grid[(i, j)].append((i, j+1))
    return grid

def min_dict(d, Q):
    filtered_dict = {k: d[k] for k in Q if k in d}
    return min(filtered_dict, key=filtered_dict.get)


def djikstra(G, dim):
    Q = list(G)
    dist = {g: float("inf") for g in G}
    prev = {g: None for g in G}

    dist[(0, 0)] = 0

    while Q:
        u = min_dict(dist, Q)
        Q.remove(u)
        for candidate in G[u]:
            alt = dist[u] + 1
            if alt < dist[candidate]:
                dist[candidate] = alt
                prev[candidate] = [u]
    return dist, prev

start_n_bytes = 0
end_n_bytes = len(input)

grid = load_grid(end_n_bytes)
dist, prev = djikstra(grid, DIM)
is_true = True
while is_true:
 
    test_val = start_n_bytes + ((end_n_bytes - start_n_bytes) // 2)
    
    grid = load_grid(test_val)
    dist, prev = djikstra(grid, DIM)
    print("####",dist[(DIM, DIM)])
    if dist[(DIM, DIM)] == float("inf"):
        print("test_val", test_val)
        end_n_bytes = test_val
    else:
        print("not infinite",dist[(DIM, DIM)])
        start_n_bytes = test_val

    if end_n_bytes - start_n_bytes == 1:
        print("C'est gagné", end_n_bytes)
        print(input[end_n_bytes-1])
        is_true = False

dist, prev = djikstra(grid, DIM)

