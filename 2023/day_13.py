with open("input.txt") as f:
    input = f.read()
import numpy as np

games = input.split("\n\n")


def find_vertical(game):
    middle = game.shape[0] // 2
    print(middle)
    for row in range(middle, game.shape[0]):
        print(row)
        size = game.shape[0] - row
        print(middle - size)
        left, right = game[middle - size : middle, :], game[middle:, :]
        if np.array_equal(left, right):
            return row


for game in games:
    print(game)
    lines = game.splitlines()
    size_v, size_h = len(lines), len(lines[0])
    game = np.empty((size_v, size_h))
    for i, line in enumerate(lines):
        game[i, :] = [c == "#" for c in line]

    print(game)
    print(find_vertical(game))

    # total += find_vertical(game) + 100 * find_horizontal(game)
