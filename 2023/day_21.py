from functools import lru_cache
with open("input.txt") as f:
    input = f.read()

# We want some kind of representation where from any position  
array = []

for i_crotte, row in enumerate(input.splitlines()):
    arr_row = []
    for j, el in enumerate(row):
        if el == ".":
            arr_row.append(1)
        elif el == "#":
            arr_row.append(0)
        elif el == "S":
            arr_row.append(1)
            start_pos = (i_crotte, j)

    array.append(arr_row)

MAX_POS = i_crotte 
# TODO: explore the space of possibilities 
@lru_cache(maxsize=None)
def get_free_tiles(i, j, ns, ew):
    free_tiles = []
    # Go south
    if i > 0:
        if array[i-1][j]:
            free_tiles.append((i-1, j, ns, ew))
    else:
        if array[MAX_POS][j]:
            free_tiles.append((MAX_POS, j, ns - 1, ew))
    # Go north
    if i < MAX_POS:
        if array[i+1][j]:
            free_tiles.append((i+1, j, ns, ew))
    else:
        if array[0][j]:
            free_tiles.append((0, j, ns + 1, ew))
    # Go West
    if j > 0:
        if array[i][j-1]:
            free_tiles.append((i, j-1, ns, ew))
    else:
        if array[i][MAX_POS]:
            free_tiles.append((i, MAX_POS, ns, ew-1))
    # Go east
    if j < MAX_POS:
        if array[i][j+1]:
            free_tiles.append((i, j+1, ns, ew))
    else:
        if array[i][0]:
            free_tiles.append((i, 0, ns, ew+1))
    return free_tiles


# Start at the beginning
NB_STEPS = 100
paths = set(get_free_tiles(start_pos[0], start_pos[1], 0, 0))
success = 0

# OPTIM IDEA 1
# There may be some squares which always lead to dead-end
# OPTIME IDEA 2
# We want our updates to be independant of which part of the world we may be on
HISTORY = []
for i_crotte in range(NB_STEPS - 1):
    new_poses = set()
    for pos_idx, pos in enumerate(paths):
        possible_tiles = get_free_tiles(pos[0], pos[1], pos[2], pos[3])
        for tile in possible_tiles:
            new_poses.add(tile)
    paths = new_poses



print(len(paths))


            
        

        

            
        

