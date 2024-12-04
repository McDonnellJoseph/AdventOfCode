import itertools

with open("input.txt") as f:
    input = f.read()

input = input.splitlines()

letter_dict = {(i,j):input[i][j] for i in range(len(input)) for j in range(len(input[0]))}

total = 0
for x in range(len(input)):
    for y in range(len(input[0])):

        if input[x][y] == "X":
            print("#####")
            possible_paths = []
            sanity_check = []
            for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                try:
                    if input[x + dx][y+ dy] == "M":
                        possible_paths.append((dx, dy))
                        sanity_check.append([input[x][y], input[x+dx][y+dy]])
                except IndexError:
                    continue
            
            invalid_count = 0
            for dx, dy in possible_paths:
                for n, letter in zip([2, 3], ["A", "S"]):
                    try:
                        if input[x+ dx * n][y + dy * n] != letter:
                            invalid_count += 1
                            break
                    except IndexError:
                        invalid_count += 1
                        break
            print("x,y", x, y)
            print("paths we keep",possible_paths)

            total += len(possible_paths) - invalid_count

print(total)