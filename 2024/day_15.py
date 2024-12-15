with open("input.txt") as f:
    input = f.read()

factory_map, moves_string = input.split("\n\n")
factory_map = factory_map.splitlines()
moves_string = moves_string.splitlines()

factory_arr = [[0]*len(factory_map[0]) for _ in factory_map]
# 0 > Wall
# 1 > Box
# 2 > Empty
for i in range(len(factory_map)):
    for j in range(len(factory_map[0])):
        if factory_map[i][j] == "#":
            factory_arr[i][j] = 0
        if factory_map[i][j] == "O":
            factory_arr[i][j] = 1
        if factory_map[i][j] == ".":
            factory_arr[i][j] = 2
        if factory_map[i][j] == "@":
            robot_pos = (i, j)
            factory_arr[i][j] =2

def move_boxes(start_pos, dir):
    """
        We know previous position is a box
    """
    next_box = factory_arr[start_pos[0]+dir[0]][start_pos[1]+dir[1]]
    if next_box == 0:
        return False
    if next_box == 1:
        if move_boxes((start_pos[0]+dir[0],start_pos[1]+dir[1]), dir):
            factory_arr[start_pos[0]+dir[0]][start_pos[1]+dir[1]] = 1
            return True
        else:
            return False
    if next_box == 2:
        factory_arr[start_pos[0]+dir[0]][start_pos[1]+dir[1]] = 1
        return True

# Main Problem given input
# Difficulty -> move all boxes along the same axis 
move_map = {"^":(-1, 0), "v":(1,0), ">": (0, 1), "<":  (0, -1)}
for move_line in moves_string:
    for mv in move_line:
        print(robot_pos)
        next_move = (robot_pos[0] + move_map[mv][0], robot_pos[1] + move_map[mv][1])
        # Check if wall or immovable box 
        if factory_arr[next_move[0]][next_move[1]] == 0:
            continue
        elif factory_arr[next_move[0]][next_move[1]] == 2:
            robot_pos = next_move
            continue
        # Check if box 
        elif move_boxes(next_move, move_map[mv]):
            factory_arr[next_move[0]][next_move[1]] = 2
            robot_pos = next_move
        

part1 = 0

for i in range(len(factory_arr)):
    for j in range(len(factory_arr[0])):
        if factory_arr[i][j] == 1:
            print(i,j)
            part1 += i *100 +j

print(part1)