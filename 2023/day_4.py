with open("input.txt", "r") as f:
    input = f.read()

final_score = 0
nb_cards = [1 for _ in range(len(input.splitlines()))]
for i, line in enumerate(input.splitlines()):
    game_id, values = line.split(":")
    winning, played = values.split("|")
    winning_set = set(winning.split())
    played_set = set(played.split())
    is_win = winning_set.intersection(played_set)

    if len(is_win) > 0:
        score = 2 ** (len(is_win) - 1)
        final_score += score
        # Part 2
        for j in range(len(is_win)):
            nb_cards[i + j + 1] += nb_cards[i]

print("Part 1")
print(final_score)

print("Part 2")
print(sum(nb_cards))
