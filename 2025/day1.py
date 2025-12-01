with open("input.txt") as f:
    input = f.readlines()


start_pos = 50
count = 0

def move_left(start_pos, amount):
    n_clicks = 0
    while amount > start_pos:
        amount -= start_pos
        if n_clicks == 0 and start_pos == 0:
            pass
        else:
            n_clicks += 1

        start_pos = 100

    return start_pos - amount, n_clicks

def move_right(start_pos, amount):
    n_clicks = 0
    while amount >= 100 - start_pos:
        print(start_pos, amount)
        amount -= 100 - start_pos
        if amount == 0:
            pass
        else:
            n_clicks += 1
        start_pos = 0


    return start_pos + amount, n_clicks

count_2 = 0

for i, line in enumerate(input):
    dirr = line[0]
    nb = int(line[1:])

    if dirr == "L":
        start_pos, n_clicks = move_left(start_pos, nb)
    if dirr == "R":
        start_pos, n_clicks = move_right(start_pos, nb)

    if start_pos == 100:
        assert False
    if start_pos == 0:
        count += 1

    if n_clicks > 0:
        print(line)
    count_2 += n_clicks
 

print("#########")
print(count)
print(count_2 + count)
