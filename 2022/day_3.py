import string

with open("input.txt", "rb") as f:
    input = f.read().decode("utf-8")

rucksacks = input.split("\n")

score = 0

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
scores = {letter: i + 1 for i, letter in enumerate(letters)}
score = 0
# Part 1
for sack in rucksacks[:-1]:
    assert len(sack) % 2 == 0
    middle = len(sack) // 2
    assert len(sack[:middle]) == len(sack[middle:])
    sack_1 = set(sack[:middle])
    sack_2 = set(sack[middle:])
    union = sack_1.intersection(sack_2)
    score += scores[union.pop()]

print(score)

# Part 2
score = 0
assert (len(rucksacks) - 1) % 3 == 0
for i in range((len(rucksacks) - 1) // 3):
    sacks = rucksacks[(i * 3) : (i + 1) * 3]
    union = set(sacks[0]).intersection(set(sacks[1])).intersection(set(sacks[2]))
    assert union
    score += scores[union.pop()]
print(score)
