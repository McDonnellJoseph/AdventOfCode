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
            hit_obstacles.append((guard_pos[1]+next_move[0], guard_pos[2]+next_move[1]))
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


from itertools import combinations
# Part 2: We want to identify all obstacles that may cause an infinite loop 
# Ie: in this a rectangle or a square
count_possible = 0
blocker_set = set()
for b1, b2, b3 in combinations(hit_obstacles, 3):
    print(b1, b2, b3)

    A = (int(pow((b2[0] - b1[0]), 2)) +
         int(pow((b2[1] - b1[1]), 2)))
    B = (int(pow((b3[0] - b2[0]), 2)) +
         int(pow((b3[1] - b2[1]), 2)))
    C = (int(pow((b3[0] - b1[0]), 2)) +
         int(pow((b3[1] - b1[1]), 2)))
     
    # Check Pythagoras Formula 
    if (A > 0 and B > 0 and C > 0):
        if A == (B+C):
            count_possible += 1
            ...
            # Opposite coordinate is C
            # Add 
        if B == (A +C):
            count_possible += 1

            ...
        if C == (A+B):
            count_possible += 1

            ...
        print("Yes")
    else:
        print("No")
print(count_possible)
print(len(blocker_set))