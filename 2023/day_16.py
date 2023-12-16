import numpy as np

with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()

mirrors = np.empty((len(lines), len(lines[0])))
visited = np.zeros_like(mirrors)

MAP = {".": 0, "|": 1, "\\": 2, "/": 3, "-": 4}

VIS_MAP = {(0, 1): ">", (0, -1): "<", (1, 0): "^", (-1, 0): "v"}
for i, line in enumerate(input.splitlines()):
    for j, c in enumerate(line):
        mirrors[i, j] = MAP[c]


from collections import Counter

CALL_HIST = {}


def detect_cycle(path):
    # get index of all occurences most common element
    count = Counter(path)
    most_common = count.most_common(1)
    if most_common[0][1] > 3:
        return True
    return False


def beam_travel(mirrors, visited, inc_x=1, inc_y=0, beam_pos=(0, 0)):
    path = []
    while (
        beam_pos[0] < mirrors.shape[0]
        and beam_pos[1] < mirrors.shape[1]
        and beam_pos[0] >= 0
        and beam_pos[1] >= 0
    ):
        path.append(beam_pos)
        if detect_cycle(path):
            return visited
        visited[beam_pos[0], beam_pos[1]] += 1
        if beam_pos[0] >= mirrors.shape[0] or beam_pos[1] >= mirrors.shape[1]:
            assert False
        tile = mirrors[beam_pos[0], beam_pos[1]]
        if tile == 2:
            if inc_x == 1 and inc_y == 0:
                inc_x = 0
                inc_y = 1
            elif inc_x == -1 and inc_y == 0:
                inc_x = 0
                inc_y = -1
            elif inc_y == 1 and inc_x == 0:
                inc_x = 1
                inc_y = 0
            elif inc_y == -1 and inc_x == 0:
                inc_x = -1
                inc_y = 0
            else:
                assert False
        elif tile == 3:
            if inc_x == 1 and inc_y == 0:
                inc_x = 0
                inc_y = -1
            elif inc_x == -1 and inc_y == 0:
                inc_x = 0
                inc_y = 1
            elif inc_y == 1 and inc_x == 0:
                inc_x = -1
                inc_y = 0
            elif inc_y == -1 and inc_x == 0:
                inc_x = 1
                inc_y = 0
            else:
                assert False
        elif tile == 1 and inc_y == 0:
            if beam_pos not in CALL_HIST.keys() or path not in CALL_HIST[beam_pos]:
                if beam_pos not in CALL_HIST.keys():
                    CALL_HIST[beam_pos] = [path]
                else:
                    CALL_HIST[beam_pos].append(path)
                # print("callint split up")
                # print("history", CALL_HIST[beam_pos])
                # print(path)
                # go up
                up = (beam_pos[0] - 1, beam_pos[1])
                visited = beam_travel(mirrors, visited, inc_x=0, inc_y=-1, beam_pos=up)
                # go down
                down = (beam_pos[0] + 1, beam_pos[1])
                visited = beam_travel(mirrors, visited, inc_x=0, inc_y=1, beam_pos=down)
                return visited
            else:
                return visited
        elif tile == 4 and inc_x == 0:
            if beam_pos not in CALL_HIST.keys() or path not in CALL_HIST[beam_pos]:
                if beam_pos not in CALL_HIST.keys():
                    CALL_HIST[beam_pos] = [path]
                else:
                    CALL_HIST[beam_pos].append(path)
                # print("spliting left and right")
                # print("history", CALL_HIST[beam_pos])
                # print(path)
                # go left
                left = (beam_pos[0], beam_pos[1] - 1)
                visited = beam_travel(
                    mirrors, visited, inc_x=-1, inc_y=0, beam_pos=left
                )
                # go right
                right = (beam_pos[0], beam_pos[1] + 1)
                visited = beam_travel(
                    mirrors, visited, inc_x=1, inc_y=0, beam_pos=right
                )
                return visited
            else:
                return visited
        # increment step
        beam_pos = (beam_pos[0] + inc_y, beam_pos[1] + inc_x)
    # print("Exiting travel")
    return visited


max_energy = 0
energies = []
for i in range(mirrors.shape[0]):
    print(i)
    energised = beam_travel(mirrors, visited, inc_x=1, inc_y=0, beam_pos=(i, 0))
    energies.append(np.count_nonzero(energised))
    if np.count_nonzero(energised) > max_energy:
        max_energy = np.count_nonzero(energised)
    visited = np.zeros_like(mirrors)
    CALL_HIST = {}


for i in range(mirrors.shape[0]):
    print(i)
    energised = beam_travel(
        mirrors, visited, inc_x=-1, inc_y=0, beam_pos=(i, mirrors.shape[1] - 1)
    )
    energies.append(np.count_nonzero(energised))

    if np.count_nonzero(energised) > max_energy:
        max_energy = np.count_nonzero(energised)
    visited = np.zeros_like(mirrors)
    CALL_HIST = {}


for j in range(mirrors.shape[1]):
    print(j)
    energised = beam_travel(mirrors, visited, inc_x=0, inc_y=1, beam_pos=(0, j))
    energies.append(np.count_nonzero(energised))
    print(j, energised)
    if np.count_nonzero(energised) > max_energy:
        max_energy = np.count_nonzero(energised)
    visited = np.zeros_like(mirrors)
    CALL_HIST = {}

for j in range(mirrors.shape[1]):
    print(j)
    energised = beam_travel(
        mirrors, visited, inc_x=0, inc_y=-1, beam_pos=(mirrors.shape[0] - 1, j)
    )
    energies.append(np.count_nonzero(energised))

    if np.count_nonzero(energised) > max_energy:
        max_energy = np.count_nonzero(energised)
    visited = np.zeros_like(mirrors)
    CALL_HIST = {}


for y_ax in range(mirrors.shape[1]):
    # visited = np.zeros_like(mirrors)
    energised = beam_travel(
        mirrors, np.zeros_like(mirrors), inc_x=0, inc_y=1, beam_pos=(0, y_ax)
    )
    energies.append(np.count_nonzero(energised))
    CALL_HIST = {}
print(max(energies))
