with open("input.txt") as f:
    input = f.read()

factory_map, moves_string = input.split("\n\n")
factory_map = factory_map.splitlines()
moves_string = moves_string.splitlines()

factory_arr = [[0]*len(factory_map[0])*2 for _ in range(len(factory_map))]
# 0 > Wall
# 1 > Box
# 2 > Empty
for i in range(len(factory_map)):
    for j in range(len(factory_map[0])):
        if factory_map[i][j] == "#":
            factory_arr[i][2*j] = 0
            factory_arr[i][2*j + 1] = 0 
        if factory_map[i][j] == "O":
            factory_arr[i][2*j] = 6
            factory_arr[i][2*j +1] = 7
        if factory_map[i][j] == ".":
            factory_arr[i][2*j] = 2
            factory_arr[i][2*j + 1] = 2

        if factory_map[i][j] == "@":
            robot_pos = (i, 2*j)
            factory_arr[i][2*j] =2
            factory_arr[i][2*j+1] =2


def print_map(world, robot_pos):
    print_dic = {6: "[", 7:"]", 2:".", 0:"#"}
    for i in range(len(world)):   
        row = []    
        for j in range(len(world[i])):
            if (i, j) == robot_pos:
                row.append("@")
            
            else:
                row.append(print_dic[world[i][j]])
        print("".join(row))

def can_move_up(start_pos, dir:int):
    assert factory_arr[start_pos[0]][start_pos[1]] == 6
    next_box_left = factory_arr[start_pos[0]+dir][start_pos[1]]
    next_box_right = factory_arr[start_pos[0]+dir][start_pos[1] + 1]

    if next_box_left == 0 or next_box_right == 0:
        return False

    elif next_box_left == 2 and next_box_right == 2:
        return True

    # We have Either one or two blocks above
    else:
        can_move_left = False
        can_move_right = False
        if next_box_left == 7:
            can_move_left = can_move_up((start_pos[0]+dir, start_pos[1]-1), dir)
        if next_box_left == 6 and next_box_right == 7:
            can_move_left = can_move_up((start_pos[0]+dir, start_pos[1]), dir)
            can_move_right = can_move_left
        if next_box_left == 2:
            can_move_left = True
        if next_box_right == 6:
            can_move_right = can_move_up((start_pos[0]+dir, start_pos[1]+1), dir)
        if next_box_right == 2:
            can_move_right = True
        return can_move_left and can_move_right



def move_boxes(start_pos, dir):
    """
        We always call with the leftmost coord
    """
    assert factory_arr[start_pos[0]][start_pos[1]] == 6
    # Case where we move box along width:
    if dir[0] == 0:
        if dir[1] ==1:
            next_box = factory_arr[start_pos[0]][start_pos[1]+2]
            if next_box == 0:
                return False
            elif next_box == 7:
                assert False
            elif next_box == 6:
                if move_boxes((start_pos[0],start_pos[1]+2), dir):
                    factory_arr[start_pos[0]][start_pos[1]+1] = 6
                    factory_arr[start_pos[0]][start_pos[1]+2] = 7
                    return True
                else:
                    return False
            elif next_box == 2:
                factory_arr[start_pos[0]][start_pos[1]+1] = 6
                factory_arr[start_pos[0]][start_pos[1]+2] = 7
                return True        
        if dir[1] == -1:
            next_box = factory_arr[start_pos[0]][start_pos[1] - 1]
            if next_box == 0:
                return False
            elif next_box == 6:
                assert False
            elif next_box == 7:
                if move_boxes((start_pos[0],start_pos[1] - 2), dir):
                    factory_arr[start_pos[0]][start_pos[1]-1] = 6
                    factory_arr[start_pos[0]][start_pos[1]] = 7
                    return True
                else:
                    return False
            elif next_box == 2:
                factory_arr[start_pos[0]][start_pos[1]- 1] = 6
                factory_arr[start_pos[0]][start_pos[1]] = 7
                return True

    # If moving up
    elif dir[1] == 0:
        next_box_left = factory_arr[start_pos[0]+dir[0]][start_pos[1]]
        next_box_right = factory_arr[start_pos[0]+dir[0]][start_pos[1] + 1]
        # If either hit a wall no-one moves
        if next_box_left == 0 or next_box_right == 0:
            return False
        # If both are empty we can move 
        elif next_box_left == 2 and next_box_right == 2:
            factory_arr[start_pos[0]+dir[0]][start_pos[1]] = 6
            factory_arr[start_pos[0]+dir[0]][start_pos[1] + 1] = 7
            return True

        # We have Either one or two blocks above
        elif can_move_up(start_pos, dir[0]):    
            if next_box_left == 6 or next_box_right == 7:
                move_boxes((start_pos[0]+dir[0], start_pos[1]), dir)
            if next_box_left == 7:
                move_boxes((start_pos[0]+dir[0], start_pos[1]-1), dir)
                # Set to zero the empty square
                factory_arr[start_pos[0]+dir[0]][start_pos[1]-1]= 2
            if next_box_right == 6:
                move_boxes((start_pos[0]+dir[0], start_pos[1]+1), dir)
                factory_arr[start_pos[0]+dir[0]][start_pos[1]+2]= 2

            factory_arr[start_pos[0]+dir[0]][start_pos[1]]=6
            factory_arr[start_pos[0]+dir[0]][start_pos[1]+1]=7
            return True
        else:
            return False
    assert False

# Main Problem given input
# Difficulty -> move all boxes along the same axis 
move_map = {"^":(-1, 0), "v":(1,0), ">": (0, 1), "<":  (0, -1)}
for move_line in moves_string:
    for mv in move_line:
        
        #print_map(factory_arr, robot_pos)
        #print(mv)
        next_move = (robot_pos[0] + move_map[mv][0], robot_pos[1] + move_map[mv][1])
        # Check if wall or immovable box 
        if factory_arr[next_move[0]][next_move[1]] == 0:
            continue
        elif factory_arr[next_move[0]][next_move[1]] == 2:
            robot_pos = next_move
            continue
        # Check if box 
        elif factory_arr[next_move[0]][next_move[1]] == 6:
            print()
            print_map(factory_arr, robot_pos)
            print(mv)

            if move_boxes((next_move[0], next_move[1]), move_map[mv]):
                factory_arr[next_move[0]][next_move[1]] = 2
                if move_map[mv][0] != 0:
                    factory_arr[next_move[0]][next_move[1]+1] = 2
                robot_pos = next_move
            print_map(factory_arr, robot_pos)
        elif factory_arr[next_move[0]][next_move[1]] == 7:
            print()
            print_map(factory_arr, robot_pos)
            print(mv)
            if move_boxes((next_move[0], next_move[1]-1), move_map[mv]):
                factory_arr[next_move[0]][next_move[1]] = 2
                if move_map[mv][0] != 0:
                    factory_arr[next_move[0]][next_move[1]-1] = 2
                robot_pos = next_move
            print_map(factory_arr, robot_pos)
        
print_map(factory_arr,robot_pos)
part1 = 0

for i in range(len(factory_arr)):
    for j in range(len(factory_arr[0])):
        if factory_arr[i][j] == 6:
            assert factory_arr[i][j+1] == 7
            print(i,j)
            part1 += i *100 +j

print(part1)