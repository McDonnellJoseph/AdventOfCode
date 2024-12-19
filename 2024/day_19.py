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

@lru_cache(maxsize=None)
def count_possible(goal, patterns):
    counts = 0
    if goal in patterns:
        print("Reached goal")
        return 1
    elif len(goal) == 1:
        return 0
    else:
        for i in range(1, len(goal)//2+1):
            left_counts = 0 
            rigth_counts = 0
            left_counts = count_possible(goal[:i], patterns)
            print("left", goal[:i], "patterns", patterns)
            print("Left count", left_counts)
            if left_counts > 0:
                rigth_counts = count_possible(goal[i:], patterns)
                print("right", goal[i:], "patterns", patterns)
                print("right count", rigth_counts)
            if left_counts > 0 and rigth_counts > 0:
                print("Left + Right")
                counts += left_counts * rigth_counts
                print(counts)
                
        return counts

count_p1 = 0
count_p2 = 0
for i, goal in enumerate(targets):
    print(i)
    if is_possible(goal, patterns):
        count_p1 += 1
    count_p2 += count_possible(goal, patterns)

print("Part1", count_p1)
print("Part2", count_p2)
