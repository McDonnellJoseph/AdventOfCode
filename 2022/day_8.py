with open("input.txt") as f:
    input = f.read()

import numpy as np

rows = input.split("\n")[:-1]
n_rows = len(rows)
n_cols = len(list(rows[0]))

forest = np.empty((n_rows, n_cols))

for i in range(n_rows):
    row = rows[i]
    for j in range(n_cols):
        forest[i, j] = int(row[j])
count = 0
max_score = 0
for i in range(n_rows):
    for j in range(n_cols):
        mem = False
        elem = forest[i, j]
        # dir 1
        score_dir1 = 0
        for i_dir1 in range(1, i + 1):
            if forest[i - i_dir1, j] < elem:
                score_dir1 += 1
            else:
                score_dir1 += 1
                break

        # dir 1
        score_dir2 = 0
        for i_dir2 in range(1, n_rows - i):
            if forest[i + i_dir2, j] < elem:
                score_dir2 += 1
            else:
                score_dir2 += 1
                break

        # dir 1
        score_dir3 = 0
        for i_dir3 in range(1, j + 1):
            if forest[i, j - i_dir3] < elem:
                score_dir3 += 1
            else:
                score_dir3 += 1
                break
        # dir 1
        score_dir4 = 0
        for i_dir4 in range(1, n_rows - j):
            if forest[i, j + i_dir4] < elem:
                score_dir4 += 1
            else:
                score_dir4 += 1
                break
        # dir1 = max(forest[:i, j])
        # dir2 = max(forest[i + 1 :, j])
        # dir3 = max(forest[i, :j])
        # dir4 = max(forest[i, j + 1 :])

        # if elem > dir1 or elem > dir2 or elem > dir3 or elem > dir4:
        #     count += 1
        print(elem, score_dir1, score_dir2, score_dir3, score_dir4)
        score = score_dir1 * score_dir2 * score_dir3 * score_dir4
        if max_score < score:
            max_score = score
print(max_score)
NEIGH = {complex(0,1)**i for i in range(4)}
ipt = open("day_08.txt").read().split("\n")
STATE = {complex(i, j): int(ipt[i][j]) for i in range(len(ipt)) for j in range(len(ipt[i]))}
get_properties= lambda z, dz, N, n:(True,n-1)*(z not in STATE) or (False, n)*(STATE[z] >= N) or get_properties(z+dz, dz, N, n+1)
​
res = [[get_properties(z+dz, dz, STATE[z], 1) for dz in NEIGH] for z in STATE]
print("the answer 1 is : ", sum( any(t[0] for t in _l) for _l in res))
print("the answer 2 is : ", max( _l[0][1]*_l[1][1]*_l[2][1]*_l[3][1] for _l in res))