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


TUPS_DIR = {(0, 1): ">", (0, -1): "<", 
        (-1, 0):"^", (1, 0): "v"}


def manhattan_routes(start, end, inv_dir):
    def helper(current, path):
        if current == end:
            results.append(path)
            return
        y, x = current
        ey = end[0]-y
        ex = end[1] - x
        if ex != 0 and (y, x+int(copysign(1, ex))) in inv_dir:
            helper((y, x+copysign(1, ex)), path + [TUPS_DIR[(0, int(copysign(1, ex)))]])

        if ey !=0  and (y+int(copysign(1, ey)), x) in inv_dir:
            helper((y+copysign(1,ey), x), path + [TUPS_DIR[(int(copysign(1, ey)), 0)]])
 
    
    results = []
    helper(start, [])
    
    return results

# For any route on the direction digicode find the cost on the next digicode
def digicode_cost(a, b, level):
    """
        Given 2 posititions on the direction digicode.
        Return the smallest route on the next digicode and it's cost.
    """
    if level == 2:
        possible_routes = manhattan_routes(a, b, DIR_INV)
        return min(possible_routes), len(min(possible_routes))

    possible_routes = manhattan_routes(a, b, DIR_INV)
    min_route = None
    min_cost = float("inf")
    for route in possible_routes:
        total_route = []
        cost = 0
        for i in range(1, len(route)):
            smallest_route, smallest_cost = digicode_cost(route[i-1], route[i], level+1)
            cost += smallest_cost
            total_route.extend(smallest_route)
        if cost < min_cost:
            min_route = total_route
            min_cost = cost

    return min_route, min_cost

def get_route_cost(route, is_final):

    cost = 0
    # For each step 
    for i in range(1, len(route)):
        print(DIR_INV[route[i-1]], DIR_INV[route[i]])
        # Possible routes to make the move
        possible_routes = manhattan_routes(DIR_INV[route[i-1]], DIR_INV[route[i]], DIR)

        if is_final:
            cost += len(min(possible_routes))
        else:
            for pos_route in possible_routes:
                cost += get_best_route(pos_route, is_final)

    return cost


def bfs(a, b):
    # Get all routes on keypad from A to B
    routes = manhattan_routes(current_pos, next_key_pos, NUM_INV)
    # For each route from A to B:
    min_route = None
    min_cost = float("inf")
    for route in routes:
    #   - For each step on this route:
        total_route = []
        cost = 0
        for i in range(1, len(route)):
    #       - Get smallest route 




def get_instructions(robot_start, goal, dirs, dirs_inv):
    instructions = []
    current_pos = robot_start
    for elem in goal:
        print(f"{elem}:")
        if elem.isdigit():
            elem = int(elem)
        # distance to the key
        print(current_pos, elem, dirs[elem])
        next_key_pos = dirs[elem]
        mv_y = next_key_pos[0] - current_pos[0]
        mv_x = next_key_pos[1] - current_pos[1]
        actual_x = 0e
        actual_y = 0
        through = []

        routes = manhattan_routes(current_pos, next_key_pos, dirs_inv)
        print(routes)
        best_route = None
        best_cost = float("inf")
        for route in routes:
            route_cost = get_route_cost(route)
            if route_cost < best_cost:
                best_route = route
                best_cost = route_cost
        print(routes)
        instructions.extend(best_route)
        instructions.append("A")
        #print(instructions[-(abs(mv_x)+abs(mv_y))-1:])
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
    return part1

print("".join(get_shortest_sequence("379A")))
assert len(get_shortest_sequence("379A")) == 64
assert "".join(get_instructions(DIR_ROBOT_START, "<A^A>^^AvvvA", DIR_INV,DIR)) == "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"

print(get_shortest_sequence("029A"))
assert len(get_shortest_sequence("029A")) == 68
assert len(get_shortest_sequence("379A")) == 64

assert part_1() == 126384

