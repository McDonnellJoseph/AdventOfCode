with open("input.txt") as f:
    input = f.read()
input = input.splitlines()

moves = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
rotations = {"^": ">", "v": "<", ">": "v", "<": "^"}
guard_pos = ("", 0, 0)
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] in ["^","<", ">","v"]:
            guard_pos = (input[i][j], i,j)

visited_tiles = set()
visited_tile_list = []
hit_obstacles = []
hit_heading = []
hit_count = 0
obs_set = set()
path_with_pos = []
to_check = []


# Part 1
try:
    while input[guard_pos[1]][guard_pos[2]]:
        next_move = moves[guard_pos[0]]
        # Case 1: we go on to a path already traveled surely it must be a loop
        test_rot = rotations[guard_pos[0]]
        if (test_rot,guard_pos[1]+moves[test_rot][0], guard_pos[2]+moves[test_rot][1]) in path_with_pos:
            obs_set.add((guard_pos[1]+next_move[0],guard_pos[2]+next_move[1]))
        # Case 2: it moves us on to the final path so it is not a loop
        else:
            to_check.append(((test_rot,guard_pos[1]+moves[test_rot][0], guard_pos[2]+moves[test_rot][1]),(guard_pos[1]+next_move[0], guard_pos[2] + next_move[1])))
            # obs_set.add((guard_pos[1],guard_pos[2]))

        while input[guard_pos[1]+next_move[0]][guard_pos[2]+next_move[1]] == "#":
            hit_obstacles.append((guard_pos[1], guard_pos[2]))
            hit_heading.append(rotations[guard_pos[0]])
            guard_pos = (rotations[guard_pos[0]],guard_pos[1], guard_pos[2])
            next_move = moves[guard_pos[0]]
        # update his path 
        guard_pos = (guard_pos[0], guard_pos[1]+next_move[0], guard_pos[2]+next_move[1])

        visited_tiles.add((guard_pos[1], guard_pos[2]))
        visited_tile_list.append((guard_pos[1], guard_pos[2]))
        path_with_pos.append(guard_pos)
except IndexError:
    # print("part 1")
    # print(len(visited_tiles))
    import copy
    for check, blocker in to_check:
        test = (check[0], check[1], check[2])
        test_path = set()
        input_test = copy.deepcopy(input)
        try:
            input_test[blocker[0]] = input[blocker[0]][:blocker[1]] + "#" +input[blocker[0]][blocker[1]+1:]
        except IndexError:
            continue
        # Check we can find a way
        try:
            while test[1] >= 0 and test[2] >= 0 and input_test[test[1]][test[2]]:
                next_move = moves[test[0]]
                while input_test[test[1]+next_move[0]][test[2]+next_move[1]] == "#":
                    test = (rotations[test[0]], test[1], test[2])
                    next_move = moves[test[0]]
                test = (test[0], test[1]+next_move[0], test[2]+next_move[1])

                if test in test_path:
                    obs_set.add(blocker)
                    break
                test_path.add(test)
        except IndexError:
            ...
    print("part 2")
    print(len(obs_set))
