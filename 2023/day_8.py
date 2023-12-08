with open("input.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

directions, network = lines[0], lines[2:]

nodes = {}

for node in network:
    origin, left_right = node.split("=")
    nodes[origin.strip()] = tuple((left_right.strip()[1:4], left_right.strip()[6:9]))

current_nodes = []
for key in nodes.keys():
    print(key[-1])
    if key[-1] == "A":
        current_nodes.append(key)

assert len(nodes) == len(network)
end_node = "ZZZ"
counter = 0
print(len(current_nodes))
print([node[-1] == "Z" for node in current_nodes])
while sum([node[-1] == "Z" for node in current_nodes]) < len(current_nodes):
    # for i in range(1):
    print(counter)
    for c in directions:
        counter += 1
        for i, current_node in enumerate(current_nodes):
            if c == "L":
                current_nodes[i] = nodes[current_node][0]
            elif c == "R":
                current_nodes[i] = nodes[current_node][1]

        if sum([node[-1] == "Z" for node in current_nodes]) == len(current_nodes):
            break


print(counter)
