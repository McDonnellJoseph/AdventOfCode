with open("full_input.txt") as f:
    ipt = f.read()

list_left, list_right = [], []

for line in ipt.splitlines():
    line_vals = line.split("   ")
    list_left.append(int(line_vals[0]))
    list_right.append(int(line_vals[1]))

list_left = sorted(list_left)
list_right = sorted(list_right)

diff_total = 0
for left, right in zip(list_left, list_right):
    diff_total += abs(left - right)

print("Part 1:")
print(diff_total)

right_count = {}

for val in list_right:
    if val in right_count:
        right_count[val] += 1
    else:
        right_count[val] = 1

score_part2 = 0
for val in list_left:
    if val  in right_count:
        score_part2 += val * right_count[val]
print("Part 2")
print(score_part2)


