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


PATTERN = re.compile(r"#+")
from functools import lru_cache


@lru_cache(maxsize=None)
def enumerate_condition(string, conditions):
    groups = list(PATTERN.finditer(string))

    # print("Starting with", string, conditions)
    # print("These are the groups", groups)
    # breaking condition no more ? in string and the count matches the conditions
    if "?" not in string:
        if len(groups) == len(conditions):
            truths = [
                (groups[i].span()[1] - groups[i].span()[0]) == conditions[i]
                for i in range(len(conditions))
            ]
            if sum(truths) == len(conditions):
                return 1
        return 0

    to_replace = string.index("?")
    left = string[:to_replace] + "." + string[to_replace + 1 :]
    right = string[:to_replace] + "#" + string[to_replace + 1 :]
    # Find all groups before our ?
    preceed = [group for group in groups if group.span()[1] - 1 < to_replace]

    if len(preceed) == 0:
        # look ahead
        # if string[to_replace+1] == "#":

        return enumerate_condition(left[to_replace:], conditions) + enumerate_condition(
            right[to_replace:], conditions
        )

    if len(preceed) > len(conditions):
        return 0

    for i in range(len(preceed) - 1):
        # For the first n - 1 groups
        if preceed[i].span()[1] - preceed[i].span()[0] != conditions[i]:
            return 0

    # For group n
    # Case where the block has correct size
    last = preceed[-1]
    size_last = last.span()[-1] - last.span()[0]
    pos = len(preceed)
    if size_last == conditions[pos - 1]:
        # If it ends just before the ?
        if to_replace == last.span()[1]:
            return enumerate_condition(left[to_replace + 1 :], conditions[pos:])
        # If it ends way before search both ways
        else:
            return enumerate_condition(
                left[to_replace:], conditions[pos:]
            ) + enumerate_condition(right[to_replace:], conditions[pos:])

    # Case last group is smaller than required length and ends next to ?
    elif size_last < conditions[pos - 1] and last.span()[1] == (to_replace):
        return enumerate_condition(right[last.span()[0] :], conditions[pos - 1 :])
    # Too small and can't be saved
    else:
        return 0


# assert enumerate_condition("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 0) == 1
# assert enumerate_condition("???.###", [1, 1, 3], 0) == 1
# assert enumerate_condition(".??..??...?##.", [1, 1, 3], 0) == 4
# assert enumerate_condition("?###????????", [3, 2, 1], 0) == 10
# assert enumerate_condition("?#?????.?..??.#??.", [1, 2, 1, 2, 1, 1], 0) == 4
# assert (
#     enumerate_condition(
#         "???.###????.###????.###????.###????.###",
#         [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3],
#         0,
#     )
#     == 1
# )


def brute_force(string, conditions):
    groups = list(PATTERN.finditer(string))
    if "?" not in string:
        if len(groups) == len(conditions):
            truths = [
                (groups[i].span()[1] - groups[i].span()[0]) == conditions[i]
                for i in range(len(conditions))
            ]
            if sum(truths) == len(conditions):
                return 1
        return 0
    else:
        to_replace = string.index("?")
        left = string[:to_replace] + "." + string[to_replace + 1 :]
        right = string[:to_replace] + "#" + string[to_replace + 1 :]
        return brute_force(left, conditions) + brute_force(right, conditions)


count = 0
count_force = 0
with open("input.txt") as f:
    input = f.read()
    lines = input.splitlines()
    for line_nb in range(len(lines)):
        print(line_nb)
        full_text, full_numbers = [], []
        for j in range(5):
            text, numbers = lines[line_nb].split()
            full_text.append(text + "?")
            full_numbers += [int(nb) for nb in numbers.split(",")]

        text = "".join(full_text)
        text = text[:-1]
        count += enumerate_condition(text, tuple(full_numbers))
print(count)
