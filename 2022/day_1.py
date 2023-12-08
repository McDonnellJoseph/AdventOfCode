with open("input.txt", "rb") as f:
    input = f.read()
    text = input.decode(encoding="utf-8")

calories = []
for el in text.split("\n\n")[:-1]:
    total = 0
    for e in el.split("\n"):
        total += int(e)

    calories.append(total)

sorted_cal = sorted(calories)

print(sum(sorted_cal[-3:]))
