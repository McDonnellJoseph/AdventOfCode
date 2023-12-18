with open("input.txt") as f:
    input = f.read()

total = 0
for line in input.splitlines():
    for val in line.split(","):
        sub = 0
        print(val)
        for i in range(len(val)):
            sub += ord(val[i])
            sub *= 17
            sub = sub % 256
        print(sub)
        total += sub
print(total)


box_labels = [[] for i in range(256)]
box_focals = [[] for i in range(256)]


def get_hash(val):
    sub = 0
    for i in range(len(val)):
        sub += ord(val[i])
        sub *= 17
        sub = sub % 256
    return sub


lens_to_box = {}

for line in input.splitlines():
    for val in line.split(","):
        # go to relevant box and remove lens with label
        if "-" in val:
            toto = val.split("-")[0]
            box_nb = get_hash(toto)

            if toto in box_labels[box_nb]:
                index = box_labels[box_nb].index(toto)
                box_labels[box_nb].pop(index)
                box_focals[box_nb].pop(index)

        elif "=" in val:
            split = val.split("=")
            focal_length = split[-1]
            label = split[0]
            box_nb = get_hash(label)
            if label in box_labels[box_nb]:
                # remove with correct label
                index = box_labels[box_nb].index(label)
                box_labels[box_nb][index] = label
                box_focals[box_nb][index] = focal_length
            else:
                box_labels[box_nb].insert(0, label)
                box_focals[box_nb].insert(0, focal_length)

        else:
            assert False
focusing_power = 0

print("powers")
for i, box in enumerate(box_focals):
    box.reverse()
    if box:
        print(f"box {i}", box)
    for j, focal in enumerate(box):
        power = (1 + i) * (j + 1) * int(focal)
        print(power)
        focusing_power += power
print(focusing_power)
# print(box_labels, box_focals)
