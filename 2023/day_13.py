with open("input.txt") as f:
    input = f.read()
import numpy as np

games = input.split("\n\n")


def find_vertical(game):
    # look right
    for row in range(1, game.shape[1]):
        if row < game.shape[1] - row:
            left, right = game[:, :row], game[:, row : 2 * row]
        if row > game.shape[1] - row:
            max_size = game.shape[1] - row
            left, right = game[:, row - max_size : row], game[:, row:]

        if row == game.shape[1] - row:
            # perfect case
            left, right = game[:, :row], game[:, row:]

        assert left.shape == right.shape
        equalities = np.invert(np.flip(left, axis=1) == right)
        print(equalities)
        if equalities.sum() == 1:
            return row


def find_horizontal(game):
    for col in range(1, game.shape[0]):
        if col < game.shape[0] - col:
            left, right = game[:col, :], game[col : 2 * col, :]
        if col > game.shape[0] - col:
            max_size = game.shape[0] - col
            left, right = game[col - max_size : col, :], game[col:, :]

        if col == game.shape[0] - col:
            # perfect case
            left, right = game[:col, :], game[col:, :]

        assert left.shape == right.shape
        equalities = np.invert(np.flip(left, axis=0) == right)
        if equalities.sum() == 1:
            return col


horizontal_count = 0
vertical_count = 0
for game in games:
    print(game)
    lines = game.splitlines()
    size_v, size_h = len(lines), len(lines[0])
    game = np.empty((size_v, size_h))
    for i, line in enumerate(lines):
        game[i, :] = [c == "#" for c in line]

    vertical = find_vertical(game)

    if vertical:
        vertical_count += vertical
    else:
        horizontal_count += 100 * find_horizontal(game)
    # total += find_vertical(game) + 100 * find_horizontal(game)

print(horizontal_count + vertical_count)
