with open("input.txt") as f:
    input = f.read()
import numpy as np

lines = input.splitlines()

mat = np.empty((len(lines), len(lines[0])))


MAP = {"O": 1, ".": 0, "#": 2}

truths = np.ones_like(mat)
for i, line in enumerate(lines):
    for j in range(len(line)):
        mat[i, j] = MAP[line[j]]
        if line[j] == "#":
            truths[i, j] = 0

    mat[i, :] = [MAP[c] for c in line]

# next = max(i, i-1) # (1, 0) -> 1 (2, 0) -> 2 (0, 1) -> (2, 1) -> 2
# current = min(i, i-1) # (1, 0) -> 0 (2, 0) -> 0 (0, 1) -> 0, (2, 1) -> 1

from functools import lru_cache


# reverse throught the array
@lru_cache(maxsize=None)
def move_mat(mat):
    mat = np.array(mat)
    for i in range(mat.shape[1]):
        for j in range(mat.shape[0]):
            if mat[j, i] == 0:
                if mat[j + 1 :, i].any():
                    next_elem = (mat[j + 1 :, i] != 0).argmax()
                    if mat[j + 1 + next_elem, i] == 1:
                        mat[j, i] = 1
                        mat[j + 1 + next_elem, i] = 0
    return mat


start_mat = mat.copy()


def compute_load(mat):
    counts = [(i + 1) * 10 for i in range(mat.shape[0])]
    counts.reverse()
    total = 0
    for i in range(mat.shape[0]):
        total += sum(mat[i, :] == 1) * counts[i]

    return total


from scipy.ndimage import rotate

for toto in range(1000000000):
    for _ in range(4):
        mat = move_mat(tuple(tuple(mat[i, :]) for i in range(mat.shape[0])))
        mat = rotate(mat, angle=-90)

    if np.array_equal(mat, start_mat):
        print(toto)

print(compute_load(mat))
