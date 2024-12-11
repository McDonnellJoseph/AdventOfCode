with open("input.txt") as f:
    input = f.read()


# line = [int(number) for number in input.split()]
line = {int(number): 1 for number in input.split()}


def blink(line):
    # For each 0
    next_line = {}
    for elem in line:
        # If stone is zero it turns to 1
        if elem == 0:
            if 1 in next_line:
                next_line[1] += line[0]
            else:
                next_line[1] = line[0]
        # size can be divided by 2
        elif len(str(elem)) % 2 == 0:
            elem_str = str(elem)
            left, right = (
                int(elem_str[: len(elem_str) // 2]),
                int(elem_str[len(elem_str) // 2 :]),
            )
            # Could we colide
            if left in next_line:
                next_line[left] += line[elem]
            else:
                next_line[left] = line[elem]
            if right in next_line:
                next_line[right] += line[elem]
            else:
                next_line[right] = line[elem]
        else:
            mult = elem * 2024
            if mult in next_line:
                next_line[mult] += line[elem]
            else:
                next_line[mult] = line[elem]
    return next_line


for i in range(75):
    line = blink(line)

print("Total :", sum([line[e] for e in line]))
