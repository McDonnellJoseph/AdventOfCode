from itertools import product
from math import copysign


NUM = {(0, 0): 7, (0, 1): 8, (0, 2): 9, 
        (1, 0):4, (1,1):5, (1,2):6, 
        (2, 0):1, (2,1):2, (2,2):3, 
            (3,1):0, (3, 2):"A"}


NUM_INV = {7:(0, 0), 8:(0, 1), 9:(0, 2), 
        4:(1, 0), 5:(1,1), 6:(1,2), 
        1:(2, 0), 2:(2,1), 3:(2,2), 
            0:(3,1), "A":(3, 2)}



DIR = {(0, 1): "^", (0, 2): "A", 
        (1, 0):"<", (1,1):"v", (1,2):">"}

DIR_INV = {"^":(0, 1), "A":(0, 2), "<":(1, 0), "v":(1, 1), ">":(1, 2)}

MVS = {}
KEY_ROBOT_START = (3, 2)
DIR_ROBOT_START = (0, 2)

def manhattan_routes(start, end, inv_dir):
    def helper(current, path):
        if current == end:
            results.append(path)
            return
        y, x = current
        ey = end[0]-y
        ex = end[1] - x
        if ex != 0 and (y, x+copysign(1, ex)) in inv_dir:
            helper((y, x+copysign(1, ex)), path + [(y, x+copysign(1, ex))])

        if ey !=0  and (y+copysign(1, ey), x) inv_dir:
            helper((y+copysign(1,ey), x), path + [(y + copysign(1, ey), x)])

    results = []
    helper(start, [start])
    return results


def get_instructions(robot_start, goal, dirs, dirs_inv):
    instructions = []
    current_pos = robot_start
    for elem in goal:
        print(f"{elem}:")
        if elem.isdigit():
            elem = int(elem)
        # distance to the key
        #print(current_pos, elem, dirs[elem])
        next_key_pos = dirs[elem]
        mv_y = next_key_pos[0] - current_pos[0]
        mv_x = next_key_pos[1] - current_pos[1]
        actual_x = 0
        actual_y = 0
        through = []
        if (next_key_pos[0], current_pos[1]) not in dirs_inv:
            #print("current",current_pos)
            #print("next",next_key_pos)
            #print(dirs.keys())
            #print((current_pos[0], next_key_pos[1]))
            assert (current_pos[0], next_key_pos[1]) in dirs_inv

            if mv_x > 0:
                # Go right 
                actual_x += mv_x
                instructions.extend([">"]* mv_x)
            elif mv_x < 0:
                 # Go left  
                actual_x += -1 * abs(mv_x)
                instructions.extend(["<"] * abs(mv_x))

            if mv_y > 0:
                # Go down 
                actual_y += mv_y
                instructions.extend(["v"]* mv_y)
            elif mv_y < 0:
                # Go Up  
                actual_y += -1 * abs(mv_y)
                instructions.extend(["^"] * abs(mv_y))
        else:
            assert (next_key_pos[0],current_pos[1]) in dirs_inv
            if mv_y > 0:
                # Go down 
                actual_y += mv_y
                instructions.extend(["v"]* mv_y)
            elif mv_y < 0:
                # Go Up  
                actual_y += -1 * abs(mv_y)
                instructions.extend(["^"] * abs(mv_y))
            if mv_x > 0:
                # Go right 
                actual_x += mv_x
                instructions.extend([">"]* mv_x)
            elif mv_x < 0:
                 # Go left  
                actual_x += -1 * abs(mv_x)
                instructions.extend(["<"] * abs(mv_x))
        instructions.append("A")
        print(instructions[-(abs(mv_x)+abs(mv_y))-1:])

        assert dirs_inv[(current_pos[0]+actual_y, current_pos[1]+actual_x)] == elem

        current_pos = next_key_pos
    return instructions

def get_shortest_sequence(goal):
    # TODO: Some kind of search
    #print("GOAL", goal)
    robot_ins = get_instructions(KEY_ROBOT_START, goal, NUM_INV, NUM)
    #print("First Instructions", robot_ins)
    dir_1 = get_instructions(DIR_ROBOT_START, robot_ins, DIR_INV, DIR)
    print("Second Instructions", dir_1)
    dir_2 = get_instructions(DIR_ROBOT_START, dir_1, DIR_INV, DIR)
    return dir_2


def part_1():
    with open("input.txt") as f:
        input = f.read()
    part1 = 0
    for el in input.splitlines():
        seq = get_shortest_sequence(el)
        print(len(seq), int(el[:len(el)-1]))
        part1 += len(seq) * int(el[:len(el)-1])
        print(part1)

#assert "".join(get_instructions(KEY_ROBOT_START, "029A", NUM_INV)) == "<A^A>^^AvvvA"
#<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A
#assert part_1() == 126384

print("".join(get_shortest_sequence("379A")))
assert len(get_shortest_sequence("379A")) == 64
assert "".join(get_instructions(DIR_ROBOT_START, "<A^A>^^AvvvA", DIR_INV,DIR)) == "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"

print(get_shortest_sequence("029A"))
assert get_shortest_sequence("029A") == "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
assert len(get_shortest_sequence("379A")) == 64

assert part_1() == 126384

#<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
