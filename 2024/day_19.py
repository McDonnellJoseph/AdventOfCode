from functools import lru_cache
with open("input.txt") as f:
    input = f.read()

patterns, targets = input.split("\n\n")

targets = targets.splitlines()

patterns = tuple([p.strip() for p in patterns.split(",")])

@lru_cache(maxsize=None)
def is_possible(goal, patterns):
    if goal in patterns:
        return True
    elif len(goal) == 1:
        return False
    else:
        for i in range(1, len(goal)):
            left= False
            rigth = False

            left = is_possible(goal[:i], patterns)
            if left:
                right = is_possible(goal[i:], patterns)
            if left and right:
              return True
        return False
count_p1 = 0
for i, goal in enumerate(targets):
    print(i)
    if is_possible(goal, patterns):
        count_p1 += 1
print("Part1", count_p1)
