with open("input.txt") as f:
    input = f.read()

input = input.splitlines()

moves = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
rotations = {"^": ">", "v": "<", ">": "v", "<": "^"}
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] in ["^","<", ">","v"]:
            guard_pos = (input[i][j], i,j)

visited_tiles = set()
visited_tile_list = []
hit_obstacles = []
# Part 1
try:
    while input[guard_pos[1]][guard_pos[1]]:
        next_move = moves[guard_pos[0]]
        # do rotate
        while input[guard_pos[1]+next_move[0]][guard_pos[2]+next_move[1]] == "#":
            guard_pos = (rotations[guard_pos[0]],guard_pos[1], guard_pos[2])
            next_move = moves[guard_pos[0]]
        print(guard_pos)
        # update his path 
        guard_pos = (guard_pos[0], guard_pos[1]+next_move[0], guard_pos[2]+next_move[1])
        

        visited_tiles.add((guard_pos[1], guard_pos[2]))
        visited_tile_list.append((guard_pos[1], guard_pos[2]))
except IndexError:
    print("part 1")
    print(len(visited_tiles))

# Part 2: We want to identify all obstacles that may cause an infinite loop 
# Ie: in this a rectangle or a square