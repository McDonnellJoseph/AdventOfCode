with open("input.txt") as f:
    ipt = f.readlines()


def largest_joltage(line, n):
    maxes = ["0" for _ in range(n)]
    for c in line[: len(line) - n]:
        for i in range(n):
            if c > maxes[i]:
                maxes[i] = c
                maxes[i + 1 :] = ["0"] * (n - (i + 1))
                break
    # For each remaining char
    for j in range(n):
        for k in range(j, n):
            if maxes[k] == "0" or line[len(line) - n + j] > maxes[k]:
                maxes[k] = line[len(line) - n + j]
                maxes[k + 1 :] = ["0"] * (n - (k + 1))
                break
    return int("".join(maxes))


part_1 = 0
part_2 = 0
for line in ipt:
    line = line.strip()

    if not line:
        continue
    part_1 += largest_joltage(line, 2)
    part_2 += largest_joltage(line, 12)

print("Total Part 1")
print(part_1)

print("Total Part 2")
print(part_2)
