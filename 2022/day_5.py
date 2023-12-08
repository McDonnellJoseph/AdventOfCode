with open("input.txt", "rb") as f:
    input = f.read().decode("utf-8")


stacks, moves = input.split("\n\n")

hash_stack = {i + 1: [] for i in range(9)}


# Set 1: Represent stack
for row in stacks.split("\n")[:-1]:
    for i in range(9):
        container = row[i * 4 + 1]

        if container.strip():
            hash_stack[i + 1].insert(0, container)

# Step 2: Move containers around
for row in moves.split("\n")[:-1]:
    toto = row.split()
    nb, start, to = int(toto[1]), int(toto[3]), int(toto[5])

    # take the nb last elements of start
    hash_stack[to] += hash_stack[start][-nb:]
    del hash_stack[start][-nb:]

result = []

for i in range(1, 10):
    if hash_stack[i]:
        result.append(hash_stack[i][-1])

print("".join(result))
