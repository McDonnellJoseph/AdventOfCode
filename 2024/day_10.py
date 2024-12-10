with open("input.txt") as f:
    input = f.read().splitlines()


topo = {}
trailheads = []

for i in range(len(input)):
    for j in range(len(input[0])):
        topo[(i,j)] = int(input[i][j])
        if topo[(i,j)] == 0:
            trailheads.append((i,j))

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def step(pos, reached_set):
    current_val = topo[pos]
    for move in moves:
        next_pos = (pos[0] + move[0], pos[1] + move[1])
        if next_pos in topo:
            if topo[next_pos] - current_val == 1:
                if topo[next_pos] == 9:
                    reached_set.add(next_pos)
                else:
                    reached_count = step(next_pos, reached_set)
    return reached_set
# for each trailhead
total = 0 
for trailhead in trailheads:
    total += len(step(trailhead, set()))


print(total)
