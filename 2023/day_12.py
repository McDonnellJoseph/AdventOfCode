with open("input.txt") as f:
    input = f.read()

# # = operation / . = damaged
import re


def parse_group(record, cond):
    groups = re.split(r"\.{1,}", record)

    for i in range(len(cond)):
        if len(groups[i]) != cond[i]:
            return False
    return True


def backtrack(obj, cond):
    if reject(obj, cond):
        return
    elif accept(obj, cond):
        return obj, cond


PATTERN = re.compile(r"#+")


def enumerate_condition(string, conditions):
    to_replace = string.index("?")
    groups = list(PATTERN.finditer(string))

    if len(groups) > conditions:
        return False


def resolve_tree(record, cond):
    # Breaking condition: We have only # and ?
    if len(record) == 1:
        obj = record[0]
        # Minimal number of true objects + minimal number of dots
        if len(obj) < sum(cond) + len(cond):
            return False
        else:
            backtrack(obj, cond)

    # Enumerate Possible Splits
    for i in range(0, len(cond), N):
        sol_left = resolve_tree(record[:i], cond[:i])
        sol_right = resolve_tree(record[i:], cond[i, :])


for line in input.splitlines():
    record, cond = line.split()
    cond = [int(c) for c in cond.split(",")]
    if parse_group(record, cond):
        pass
    else:
        pass
