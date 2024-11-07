from functools import lru_cache
with open("full_input.txt") as f:
    input = f.read()

# We want some kind of representation where from any position  
array = []

for i, row in enumerate(input.splitlines()):
    arr_row = []
    for j, el in enumerate(row):
        if el == ".":
            arr_row.append(1)
        elif el == "#":
            arr_row.append(0)
        elif el == "S":
            arr_row.append(1)
            start_pos = (i, j)

    array.append(arr_row)

MAX_POS = i 
# TODO: explore the space of possibilities 
@lru_cache(maxsize=None)
def get_free_tiles(i, j, ns, ew):
    free_tiles = []
    # Go south
    if i > 0:
        if array[i-1][j]:
            free_tiles.append((i-1, j, ns, ew))
    else:
        if array[MAX_POS][j] and ns > -1:
            free_tiles.append((MAX_POS, j, ns - 1, ew))
    # Go north
    if i < MAX_POS:
        if array[i+1][j]:
            free_tiles.append((i+1, j, ns, ew))
    else:
        if array[0][j] and ns < 1:
            free_tiles.append((0, j, ns + 1, ew))
    # Go West
    if j > 0:
        if array[i][j-1]:
            free_tiles.append((i, j-1, ns, ew))
    else:
        if array[i][MAX_POS] and ew > -1:
            free_tiles.append((i, MAX_POS, ns, ew-1))
    # Go east
    if j < MAX_POS:
        if array[i][j+1]:
            free_tiles.append((i, j+1, ns, ew))
    else:
        if array[i][0] and ew < 1:
            free_tiles.append((i, 0, ns, ew+1))
    return free_tiles


# Start at the beginning

def get_visitable_tiles(start_x, start_y):
    """
        From a given tile find all tiles you can reach and with as few steps as
        possible. 
    """
    paths = set(get_free_tiles(start_x, start_y, 0, 0))
    reached_tiles = {(start_x, start_y, 0, 0): 0}
    for path in paths:
        reached_tiles[path] = 1

    i = 2
    while paths and i  <= NB_STEPS:
        new_poses = set()
        for pos_idx, pos in enumerate(paths):
            # print("he", pos)
            possible_tiles = get_free_tiles(pos[0], pos[1], pos[2], pos[3])

            for tile in possible_tiles:
                if tile not in reached_tiles.keys():
                    # number of steps to reach the start tile + 1
                    reached_tiles[tile] =  i
                    new_poses.add(tile)

        paths = new_poses
        i += 1

    return reached_tiles

# For the center tile find each tile we can visit        
NB_STEPS = 26501365
reachable_from_s = get_visitable_tiles(start_pos[0], start_pos[1])

# Goalado Part 2: How many plots can I reach in EXACTLY NB_STEPS
# Max grid 
total = 0
# 0 1 2
# 3   4
# 5 6 7
def what_pos(ns, ew):
    # Upper row
    if ns == 1:
        if ew == -1:
            return 0
    if ns == 1:
        if ew == 0:
            return 1
    # Middle 
    if ns ==0:
        if ew == -1:
            return 3
        if ew == 1:
            return 4
        if ew == 0:
            return 8
    #Lower row
    if ns == -1:
        if ew == -1:
            return 5
        if ew == 0:
            return 6
        if ew == 1:
            return 7

    # Upper right triangle
    if ns == 1 and ew == 1:
        return 2

MEM, res = {}, 0
def solve(d,v):
    L=NB_STEPS
    M = (L-d)//131
    MEM[(d, v)] = MEM.get((d,v)) or sum(1 + x * (v == 2) for x in range((d+L)%2,M+1, 2))
    return MEM[(d, v)]
MAX_POS = 131
assert MAX_POS == 131
for point, n_steps_from_s in reachable_from_s.items():
    steps_to_consume = NB_STEPS - n_steps_from_s 
    manhattan_furtherst = steps_to_consume // MAX_POS

    # furthest can be lower that NB_STEPS
    # steps_left = NB_STEPS  - (manhattan_furtherst * MAX_POS + n_steps_from_s )

    # We can circle back if missing_steps is pair
    # shape = what_pos(point[2], point[3])
    pos = abs(point[2]) + abs(point[3])

    # If is in triangle
    if pos == 2:
        reachable_grids = (( manhattan_furtherst * ( manhattan_furtherst + 1)) // 2)
        # total += reachable_grids // 2 + 1
        total += solve(n_steps_from_s, 2)
    if pos == 1:
        reachable_grids = manhattan_furtherst 
        total += solve(n_steps_from_s, 1)
        # total += reachable_grids // 2

    if pos == 0:
        if n_steps_from_s % 2 == NB_STEPS % 2:
            # reachable_grids = (( manhattan_furtherst * ( manhattan_furtherst + 1)))
            total += 1


print(total)
    
"""
                100 steps -> 8909
                500 steps -> 217 777
    Full input 1000 steps -> 869 453
               2000 steps -> 3 471 921
"""        

            
        

