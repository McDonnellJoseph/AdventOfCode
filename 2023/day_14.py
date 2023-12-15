with open("input.txt") as f:
    input = f.read()
import numpy as np

lines = input.splitlines()

mat = np.empty((len(lines), len(lines[0])))

start_mat = mat.copy()
out = mat.copy()

MAP = {"O": -1, ".": 0, "#": 1}
for i, line in enumerate(lines):
    mat[i, :] = [MAP[c] for c in line]


COUNT = [0 for i in range(mat.shape[0])]


def move_north(mat):
    new_mat = mat.copy()
    new_mat[new_mat == -1] = 0
    for i in range(mat.shape[0]):
        # take each column
        col = mat[:, i]
        new_col = new_mat[:, i]
        # split it on the boulder
        boulders = np.where(col == 1)[0]

        # print(col, boulders)

        # At least one boulder
        if boulders.any():
            # all 0 at the top before any boulder
            # print("This is the first count")
            first_split = col[: boulders[0]]
            count_first = len(np.where(first_split == -1)[0])
            # print(count_first)
            for i in range(count_first):
                new_col[i] = -1
                COUNT[i] += 1

            # Do the middle boulders
            if len(boulders) > 1:
                for i in range(1, len(boulders)):
                    # print(f"middle count {i}")
                    split = col[boulders[i - 1] + 1 : boulders[i]]
                    count_split = len(np.where(split == -1)[0])
                    # print(count_split)
                    for j in range(count_split):
                        new_col[boulders[i - 1] + 1 + j] = -1
                        COUNT[boulders[i - 1] + 1 + j] += 1

            # Do the last row
            # print("Last split")
            last_split = col[boulders[-1] + 1 :]
            count_last = len(np.where(last_split == -1)[0])
            # print(count_last)
            for i in range(count_last):
                new_col[boulders[-1] + 1 + i] = -1
                COUNT[boulders[-1] + 1 + i] += 1

        else:
            # print("No boulder")
            # Everything rolls forward
            points = len(np.where(col == -1)[0])
            # print(points)
            for i in range(points):
                new_col[i] = -1
                COUNT[i] += 1
        # print("end")
        # print(COUNT)
    return new_mat


from scipy.ndimage import rotate


def cycle(mat):
    for i in range(4):
        mat = move_north(mat)
        for _ in range(3):
            mat = np.rot90(mat)
    return mat


start = int(1e9 // 22) * 22

toto = 0
start_mat = np.zeros_like(mat)
while (start_mat != mat).any():
    if toto % 50 == 0:
        toto = 0
        start_mat = mat.copy()
    mat = cycle(mat)
    print("here")
    toto += 1
    # if (start_mat == mat).all():
    #     print("equality")
    #     print(toto)
    #     break
print(toto)
print("breaking")
print(1e9 - start)
# for _ in range(start, int(1e9)):
#     final_mat = cycle(mat)
final_mat = mat

points = [i + 1 for i in range(mat.shape[0])]
points.reverse()
print("points")
sum = 0
for i in range(mat.shape[0]):
    row = final_mat[i, :]
    total = np.count_nonzero(row == -1)
    sum += total * points[i]
print(sum)
