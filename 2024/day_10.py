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

def step_p2(pos, reached_count):
    current_val = topo[pos]
    for move in moves:
        next_pos = (pos[0] + move[0], pos[1] + move[1])
        if next_pos in topo:
            if topo[next_pos] - current_val == 1:
                if topo[next_pos] == 9:
                    reached_count += 1
                else:
                    reached_count = step_p2(next_pos, reached_count)
    return reached_count

def step_p1(pos, reached_set):
    current_val = topo[pos]
    for move in moves:
        next_pos = (pos[0] + move[0], pos[1] + move[1])
        if next_pos in topo:
            if topo[next_pos] - current_val == 1:
                if topo[next_pos] == 9:
                    reached_set.add(next_pos)
                else:
                    reached_set = step_p1(next_pos, reached_set)
    return reached_set
# for each trailhead
total_p1 = 0 
total_p2 = 0
for trailhead in trailheads:
    total_p1 += len(step_p1(trailhead, set()))
    total_p2 += step_p2(trailhead, 0)


print("part 1", total_p1)
print("part 2", total_p2)
