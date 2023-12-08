with open("input.txt", "rb") as f:
    input = f.read()
    text = input.decode(encoding="utf-8")


def get_score(pl1, pl2):
    points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    if pl2 == "X":
        if pl1 == "A":
            plays = "Z"
        if pl1 == "B":
            plays = "X"
        if pl1 == "C":
            plays = "Y"
        result = 0
    elif pl2 == "Y":
        if pl1 == "A":
            plays = "X"
        if pl1 == "B":
            plays = "Y"
        if pl1 == "C":
            plays = "Z"
        result = 3
    elif pl2 == "Z":
        if pl1 == "A":
            plays = "Y"
        if pl1 == "B":
            plays = "Z"
        if pl1 == "C":
            plays = "X"
        result = 6

    score_selected_shape = points[plays]
    return score_selected_shape + result


score = 0
for el in text.split("\n")[:-1]:
    player1, player2 = el.split()

    score += get_score(player1, player2)

print(score)
