with open("input.txt", "rb") as f:
    input = f.read().decode("utf-8")


import numpy as np

visited = set([(0, 0)])

head_pos = np.zeros((2))
tail_pos = np.zeros((2))


def move(head_pos, dir):
    # move head_pos
    if dir == "U":
        head_pos[1] += 1
    if dir == "R":
        head_pos[0] += 1
    if dir == "L":
        head_pos[0] -= 1
    if dir == "D":
        head_pos[1] -= 1

    return head_pos


dir_map = {
    np.arctan2(1, 0): "R",
    np.arctan2(-1, 0): "L",
    np.arctan2(0, 1): "U",
    np.arctan2(0, -1): "D",
    np.arctan2(1, 2): "RU",
    np.arctan2(2, 1): "RU",
    np.arctan2(1, -2): "RD",
    np.arctan2(-2, 1): "LU",  # Verified
    np.arctan2(-1, 2): "LU",
    np.arctan2(2, -1): "DR",  # Verified
    np.arctan2(-1, -2): "LD",
    np.arctan2(-2, -1): "LD",
    np.arctan2(-2, 2): "LU",
    np.arctan2(-2, -2): "LD",
    np.arctan2(2, -2): "RD",
    np.arctan2(2, 2): "RU",
}

# Part 1
for line in input.split("\n")[:-1]:
    dir, step = line.split()
    step = int(step)

    for i in range(step):
        head_pos = move(head_pos, dir)
        dist = head_pos - tail_pos
        if (dist[0] ** 2 + dist[1] ** 2) > 2:
            dir_head = dir_map[np.arctan2(dist[0], dist[1])]
            for d in dir_head:
                tail_pos = move(tail_pos, d)
            visited = visited.union(set([(tail_pos[0], tail_pos[1])]))

print("Part 1", len(visited))
# Part 2
knots = [np.zeros(2) for i in range(10)]
visited = set([(0, 0)])
for line in input.split("\n")[:-1]:
    dir, step = line.split()
    for i in range(int(step)):
        knots[0] = move(knots[0], dir)
        for j in range(9):
            dist = knots[j] - knots[j + 1]
            if (dist[0] ** 2 + dist[1] ** 2) > 2:
                dir_head = dir_map[np.arctan2(dist[0], dist[1])]
                for d in dir_head:
                    knots[j + 1] = move(knots[j + 1], d)
        visited = visited.union(set([(knots[-1][0], knots[-1][1])]))

print("Part 2", len(visited))

DIR = {"U": complex(0, 1), "D": complex(0, -1), "R": 1, "L": -1}
ipt = open("input.txt").read().split("\n")


def sign(x):
    return 0 if not x else x / abs(x)


for part, _len in [(1, 2), (2, 10)]:
    ALL_POS, HIST = [0] * _len, {0}

    for line in ipt[:-1]:
        _dir, val = line.split(" ")
        for i in range(int(val)):
            ALL_POS[0] += DIR[_dir]
            for idx in range(_len - 1):
                z = ALL_POS[idx] - ALL_POS[idx + 1]
                ALL_POS[idx + 1] += (
                    0 if abs(z) < 2 else complex(sign(z.real), sign(z.imag))
                )  # z projection on the unity square
            HIST |= {ALL_POS[-1]}

    print(f"the answer {part} is : ", len(HIST))
