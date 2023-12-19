with open("input.txt") as f:
    input = f.read()

corners = [(0, 0)]
total = 0
for line in input.splitlines():
    dir, amount, color = line.split()
    last = corners[-1]
    if dir == "R":
        new = (last[0] + int(amount), last[1])
        corners.append(new)
    if dir == "D":
        new = (last[0], last[1] + int(amount))
        corners.append(new)
    if dir == "U":
        new = (last[0], last[1] - int(amount))
        corners.append(new)
    if dir == "L":
        new = (last[0] - int(amount), last[1])
        corners.append(new)
    total += int(amount)

corners.reverse()

print(corners)


def Area(corners):
    n = len(corners)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2
    return area


from matplotlib.path import Path

path = Path(corners)

max_x = max(corners, key=lambda x: x[0])[0]
max_y = max(corners, key=lambda x: x[1])[1]
toto = 0
for i in range(max_x + 1):
    for j in range(max_y + 1):
        if path.contains_point((i, j)):
            toto += 1
print(max_x, max_y)
print(toto)
print(sum(path.contains_points(corners)))
