with open("input.txt") as f:
    input = f.read().splitlines()

garden = {}

for i in range(len(input)):
    for j in range(len(input[0])):
        garden[(i, j)] = input[i][j]


moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# Create groups
def make_group(letter, coords, visited):
    group = [coords]
    for dy, dx in moves:
        next_pos = (coords[0] + dy, coords[1] + dx)
        if next_pos not in visited and next_pos in garden:
            visited.append(next_pos)
            if garden[next_pos] == letter:
                group.extend(make_group(letter, next_pos, visited))
    return group


groups = []
already_seen = []
for g in garden:
    if g not in already_seen:
        new_group = make_group(garden[g], g, [g])
        already_seen.extend(new_group)
        groups.append(new_group)


total_p1 = 0
total_p2 = 0
# Get Perimeter for each group
for group in groups:
    perimeter = 0
    ongoing_x = None
    ongoing_y = None
    for el in group:
        # Part 1
        el_total = 4
        for m in moves:
            if (el[0] + m[0], el[1] + m[1]) in group:
                el_total -= 1
        perimeter += el_total

    total_p1 += len(group) * perimeter

    # Part 2:
    # Count each straight section of fence
    # Eclude from group any element inside
    filtered_out_group = []
    for g in group:
        for move in [(1, 0), (-1, 0)]:
            if (g[0] + move[0], g[1] + move[1]) not in group:
                filtered_out_group.append(g)
                break

    bins = {g[0]: [] for g in group}
    [bins[g[0]].append(g[1]) for g in sorted(filtered_out_group, key=lambda x: x[0])]
    perimeter = 0
    # Count horizontal
    for b in bins:
        if not bins[b]:
            continue
        sort_xs = sorted(bins[b])
        line_groups = [[sort_xs[0]]]
        # Make Bins
        for j in range(1, len(sort_xs)):
            if sort_xs[j] - sort_xs[j - 1] > 1:
                line_groups.append([sort_xs[j]])
            else:
                line_groups[-1].append(sort_xs[j])
        for lg in line_groups:
            last_added = False
            for el in lg:
                if (b - 1, el) not in group and not last_added:
                    last_added = True
                    perimeter += 1
                elif (b - 1, el) in group:
                    last_added = False
            last_added = False
            for el in lg:
                if (b + 1, el) not in group and not last_added:
                    perimeter += 1
                    last_added = True
                elif (b + 1, el) in group:
                    last_added = False

    filtered_out_group = []
    for g in group:
        for move in [(0, 1), (0, -1)]:
            if (g[0] + move[0], g[1] + move[1]) not in group:
                filtered_out_group.append(g)
                break
    # Count vertical
    bins = {g[1]: [] for g in sorted(group, key=lambda x: x[1])}
    [bins[g[1]].append(g[0]) for g in sorted(filtered_out_group, key=lambda x: x[1])]
    old_perim = perimeter
    for b in bins:
        if not bins[b]:
            continue
        sort_xs = sorted(bins[b])
        line_groups = [[sort_xs[0]]]
        # Make Bins
        for j in range(1, len(sort_xs)):
            if sort_xs[j] - sort_xs[j - 1] > 1:
                line_groups.append([sort_xs[j]])
            else:
                line_groups[-1].append(sort_xs[j])
        for lg in line_groups:
            last_added = False
            for el in lg:
                if (el, b - 1) not in group and not last_added:
                    perimeter += 1
                    last_added = True
                elif (el, b - 1) in group:
                    last_added = False
            last_added = False
            for el in lg:
                if (el, b + 1) not in group and not last_added:
                    perimeter += 1
                    last_added = True
                elif (el, b + 1) in group:
                    last_added = False
        old_perim = perimeter
    total_p2 += len(group) * perimeter


print(total_p1)
print(total_p2)
