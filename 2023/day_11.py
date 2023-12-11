with open("input.txt") as f:
    input = f.read()

import numpy as np

# 1. Find rows and lines that are empty
array = []
galaxy_count = 1
for line in input.splitlines():
    chars = list(line)
    for i in range(len(chars)):
        if chars[i] == "#":
            chars[i] = galaxy_count
            galaxy_count += 1
        else:
            chars[i] = 0

    array.append(chars)


mat = np.array(array)
for i in range(mat.shape[0]):
    print(mat[i, :])
# Row wise
to_expand_row = []
for i in range(mat.shape[0]):
    if sum(mat[i, :]) == 0:
        to_expand_row.append(i)
# Col wise
to_expand_col = []
for i in range(mat.shape[1]):
    if sum(mat[:, i]) == 0:
        to_expand_col.append(i)

# prev_shape = mat.shape
# for col in to_expand_col:
#     mat = np.insert(mat, col, 0, axis=1)

# for row in to_expand_row:
#     mat = np.insert(mat, row, 0, axis=0)
# # print("Col", to_expand_col)
# print(prev_shape, mat.shape, to_expand_row)
# print(prev_shape, mat.shape, to_expand_col)
# assert prev_shape[0] + len(to_expand_row) == mat.shape[0]
# assert prev_shape[1] + len(to_expand_col) == mat.shape[1]

for i in range(mat.shape[0]):
    print(mat[i, :])
pos = np.transpose(np.nonzero(mat))

results = {}
for elem0 in pos:
    val0 = mat[elem0[0], elem0[1]]
    for elem1 in pos:
        val1 = mat[elem1[0], elem1[1]]
        pair = tuple(sorted([val0, val1]))
        if pair not in results:
            # Count the number of expanded rows it will cross
            max_x, min_x = max(elem0[0], elem1[0]), min(elem0[0], elem1[0])
            count_x = sum(
                [1 for elem in to_expand_row if elem > min_x and elem < max_x]
            )

            max_y, min_y = max(elem0[1], elem1[1]), min(elem0[1], elem1[1])
            count_y = sum(
                [1 for elem in to_expand_col if elem > min_y and elem < max_y]
            )
            x = max(elem0[0], elem1[0]) - min(elem0[0], elem1[0]) + (999999 * count_x)
            y = max(elem0[1], elem1[1]) - min(elem0[1], elem1[1]) + (999999 * count_y)
            # print(pair)
            # print(elem0[0], elem1[0])
            # print(x, y)
            results[pair] = x + y

print(results)
print(sum(results.values()))
