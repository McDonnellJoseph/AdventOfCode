with open("input.txt", "r") as f:
    input = f.read()


MAX_COLS = {"red": 12, "green": 13, "blue": 14}
ids = set()
too_big = set()

powers = []
for line in input.split("\n"):
    game, colors = line.split(":")
    game_id = int(game.split()[1])
    ids.add(game_id)
    val_line = {"red": 0, "blue": 0, "green": 0}
    for tirage in colors.split(";"):
        for val in tirage.split(","):
            _, nb, color = val.split(" ")
            val_line[color] = max(int(nb), val_line[color])
    powers.append(val_line["blue"] * val_line["green"] * val_line["red"])
    for col in val_line.keys():
        if val_line[col] > MAX_COLS[col]:
            print(val_line)
            too_big.add(game_id)
            break

print(len(too_big))
print(sum(ids.difference(too_big)))
print(sum(powers))
