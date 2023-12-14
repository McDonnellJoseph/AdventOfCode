with open("input.txt") as f:
    input = f.read()
import numpy as np

lines = input.splitlines()

mat = np.empty((len(lines), len(lines[0])))

out = mat.copy()

MAP = {"O": -1, ".": 0, "#": np.inf}
for i, line in enumerate(lines):
    mat[i, :] = [MAP[c] for c in line]

for i in range(1):
    out[i, :] = out[i, :] + mat[i + 1, :]
    np.clip(out, -1, np.inf)

print
print(mat[1, :])
print(out[0, :])
