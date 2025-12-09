with open("input.txt") as f:
    ipt = f.read().splitlines()


start_pos = list(ipt[0]).index("S")
beam_map = [0 for _ in range(len(ipt[0]))]
beam_map[start_pos] = 1

def pretty_print(line):
    to_print = ""

    for c in line:
        if c:
            to_print += "|"
        else:
            to_print += "."
    return to_print

paths = [set() for _ in range(len(ipt[0]))]
paths[start_pos] = {((0, start_pos),)}

path_counter = [0 for _ in range(len(ipt[0]))]
path_counter[start_pos] = 1
# For each line 
part_1 = 0
for j, line in enumerate(ipt[1:]):
    new_map = [0 for _ in range(len(ipt[0]))]
    new_path_counter = [0 for _ in range(len(ipt[0]))]

    new_paths = [set() for _ in range(len(ipt[0]))]
    # For each char in the line
    assert len(line) == len(new_map)
    for i, c in enumerate(line):
        if c == "." and new_map[i] !=1:
            new_map[i] = beam_map[i]
        
        if c == ".":
            new_path_counter[i] += path_counter[i]

        elif c == "^" and beam_map[i]:
            part_1 += 1
            if i > 0:
                new_map[i-1] = 1
                new_path_counter[i-1] += path_counter[i]

            if i < len(beam_map):
                new_map[i+1] = 1
                new_path_counter[i+1] += path_counter[i]

    paths = new_paths
    beam_map = new_map
    path_counter = new_path_counter
path_set = set()
for arrival in paths:
    for path in arrival:
        path_set.add(tuple(path))

print(part_1)

print(len(paths))
print(len(path_set))
print(sum([len(path) for path in paths]))
print(sum(path_counter))