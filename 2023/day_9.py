with open("input.txt", "r") as f:
    input = f.read()


def build_predictions(value):
    predictions = [value]
    while sum(predictions[-1]) != 0:
        next_line = []
        for i in range(len(predictions[-1]) - 1):
            next_line.append(predictions[-1][i + 1] - predictions[-1][i])
        predictions.append(next_line)
    return predictions


def next_prediction(predictions):
    for i in range(1, len(predictions)):
        to_add = predictions[-i][-1] + predictions[-i - 1][-1]
        predictions[-i - 1].append(to_add)

    return to_add


def next_prediction_back(predictions):
    for i in range(1, len(predictions)):
        print(predictions[-i - 1])
        to_add = predictions[-i - 1][0] + (-1 * predictions[-i][0])
        predictions[-i - 1].insert(0, to_add)
        print(predictions[-i - 1])
    return to_add


result_part1 = 0
result_part2 = 0
for value in input.splitlines():
    predictions = build_predictions([int(v) for v in value.split()])
    result_part1 += next_prediction(predictions)
    result_part2 += next_prediction_back(predictions)

print(result_part1)
print(result_part2)
