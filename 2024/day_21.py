from functools import lru_cache
from math import copysign
from frozendict import frozendict

NUM = frozendict({(0, 0): 7, (0, 1): 8, (0, 2): 9, 
        (1, 0):4, (1,1):5, (1,2):6, 
        (2, 0):1, (2,1):2, (2,2):3, 
            (3,1):0, (3, 2):"A"})


NUM_INV = frozendict({"7":(0, 0), "8":(0, 1), "9":(0, 2), 
        "4":(1, 0), "5":(1,1), "6":(1,2), 
        "1":(2, 0), "2":(2,1), "3":(2,2), 
            "0":(3,1), "A":(3, 2)})



DIR = frozendict({(0, 1): "^", (0, 2): "A", 
        (1, 0):"<", (1,1):"v", (1,2):">"})

DIR_INV = frozendict({"^":(0, 1), "A":(0, 2), "<":(1, 0), "v":(1, 1), ">":(1, 2)})

MVS = {}
KEY_ROBOT_START = (3, 2)
DIR_ROBOT_START = (0, 2)


TUPS_DIR = {(0, 1): ">", (0, -1): "<", 
        (-1, 0):"^", (1, 0): "v"}

def manhattan_routes(start, end, dirs):
    def helper(current, path):
        if current == end:
            results.append(path)
            return
        y, x = current
        ey = end[0]-y
        ex = end[1] - x
        if ex != 0 and (y, x+int(copysign(1, ex))) in dirs:
            helper((y, x+copysign(1, ex)), path + [TUPS_DIR[(0, int(copysign(1, ex)))]])

        if ey !=0  and (y+int(copysign(1, ey)), x) in dirs:
            helper((y+copysign(1,ey), x), path + [TUPS_DIR[(int(copysign(1, ey)), 0)]])
    results = []
    helper(start, [])

    results = [route for route in results if len(route)==len(min(results))]
    return results

MEM_ROUTES = {}
#@lru_cache(maxsize=None)
def bfs_digi_routes(start, end):
    def helper(current, path):
        if current == end:
            results.append(path)
            return
        y, x = current
        ey = end[0]-y
        ex = end[1] - x
        if ex != 0 and (y, x+int(copysign(1, ex))) in DIR:
            helper((y, x+copysign(1, ex)), path + [TUPS_DIR[(0, int(copysign(1, ex)))]])

        if ey !=0  and (y+int(copysign(1, ey)), x) in DIR:
            helper((y+copysign(1,ey), x), path + [TUPS_DIR[(int(copysign(1, ey)), 0)]])
    results = []
    helper(start, [])

    results = [route for route in results if len(route)==len(min(results))]
    # Prune Zig Zags
    final_results = []
    for res in results:
        do_append = True 
        last_indices ={}
        for i, el in enumerate(res):
            if el not in last_indices:
                last_indices[el] = i
            else:
                if i - last_indices[el] != 1:
                    do_append = False  
                    break
                else:
                    last_indices[el] = i
        if do_append:
            final_results.append(res)
    return final_results

def create_digi_routes():
    ans = {}
    for key1 in DIR:
        for key2 in DIR:
            ans[(key1, key2)] = bfs_digi_routes(key1, key2)
    return ans

def bfs_key_routes(start, end):
    def helper(current, path):
        if current == end:
            results.append(path)
            return
        y, x = current
        ey = end[0]-y
        ex = end[1] - x
        if ex != 0 and (y, x+int(copysign(1, ex))) in NUM:
            helper((y, x+copysign(1, ex)), path + [TUPS_DIR[(0, int(copysign(1, ex)))]])

        if ey !=0  and (y+int(copysign(1, ey)), x) in NUM:
            helper((y+copysign(1,ey), x), path + [TUPS_DIR[(int(copysign(1, ey)), 0)]])
    results = []
    helper(start, [])

    results = [route for route in results if len(route)==len(min(results))]
    # Prune Zig Zags
    final_results = []
    for res in results:
        do_append = True 
        last_indices ={}
        for i, el in enumerate(res):
            if el not in last_indices:
                last_indices[el] = i
            else:
                if i - last_indices[el] != 1:
                    do_append = False  
                    break
                else:
                    last_indices[el] = i
        if do_append:
            final_results.append(res)
    return results

def create_key_routes():
    ans = {}
    for key1 in NUM:
        for key2 in NUM:
            ans[(key1, key2)] = bfs_key_routes(key1, key2)
    return ans

#80786362258
#102616647696
MEM = {}
# For any route on the direction digicode find the cost on the next digicode
@lru_cache
def digicode_cost(a, b, level):
    """
        Given 2 posititions on the direction digicode.
        Return the smallest route on the next digicode and it's cost.
    """
    if level == 24:
        possible_routes = digi_cache[DIR_INV[a], DIR_INV[b]]
        return len(min(possible_routes))

    possible_routes = digi_cache[DIR_INV[a], DIR_INV[b]]
    min_cost = float("inf")
    for route in possible_routes:
        cost = 0
        route = ["A"] + route + ["A"]
        for i in range(1, len(route)):
            smallest_cost = digicode_cost(route[i-1], route[i], level+1)
            cost += smallest_cost 
        cost += len(route) - (1 + int(bool(level)))
        if cost < min_cost:
            min_cost = cost 
    return min_cost

def bfs(a, b):
    #routes = key_cache[a, b]
    routes = manhattan_routes(a, b, NUM)
    # For each route from A to B:
    min_route = None
    min_cost = float("inf")
    for route in routes:
        total_route = []
        total_cost = 0
        
        route.insert(0, "A")
        route.append("A")
        for i in range(1, len(route)):
            dir_cost = digicode_cost(route[i-1],route[i], 0)
            total_cost += dir_cost
        if total_cost < min_cost:
            min_cost = total_cost

    return min_cost




def get_instructions(robot_start, goal, dirs, dirs_inv):
    instructions = 0
    current_pos = robot_start
    for elem in goal:
        print(f"{elem}:")
        
        # distance to the key
        #print(current_pos, elem, dirs[elem])
        next_key_pos = dirs[elem]

        best_route = bfs(current_pos, next_key_pos)
       
        #print("This is the best route", best_route)
        instructions += best_route
        #instructions.append("A")
        #print(instructions[-(abs(mv_x)+abs(mv_y))-1:])
        current_pos = next_key_pos
    print()
    #print("Instructions", instructions)
    return instructions

def get_key_seq(keys, index, prev_key, current_path, result):
    if index == len(keys):
        result.append(current_path)
        return result
    for path in key_cache[(keys[index-1], keys[index])]:
        get_key_seq(keys, index+1, keys[index], current_path+path+["A"], result)

    return result

def get_digi_seq(keys, index, prev_key, current_path, result):
    if index == len(keys):
        result.append(current_path)
        return result
    for path in digi_cache[(keys[index-1], keys[index])]:
        get_digi_seq(keys, index+1, keys[index], current_path+path+["A"], result)

    return result


key_cache = create_key_routes()
digi_cache = create_digi_routes()

print(digi_cache)
def part_1():
    with open("input.txt") as f:
        input = f.read()
    part1 = 0
    for el in input.splitlines():
        seq = get_instructions(KEY_ROBOT_START, el, NUM_INV, None)
        print(seq, int(el[:len(el)-1]))
        part1 += seq * int(el[:len(el)-1])
        print(part1)
    return part1


print("Part 2", part_1())