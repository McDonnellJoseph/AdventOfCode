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


def enumerate_condition(string, conditions, count):
    print("we are here")
    print(string)
    groups = list(PATTERN.finditer(string))
    # breaking condition no more ? in string and the count matches the conditions we increase the count by one
    if "?" not in string:
        print("not here")
        if len(groups) == len(conditions):
            truths = [
                len(groups[i].span()) == conditions[i] for i in range(len(conditions))
            ]
            if sum(truths) == len(conditions):
                print("true")
                return 1
        return 0
    to_replace = string.index("?")
    left = string[:to_replace] + "." + string[to_replace + 1 :]
    right = string[:to_replace] + "#" + string[to_replace + 1 :]
    # If there are groups
    preceed = [group for group in groups if group.span()[1] < to_replace]
    for i in range(len(preceed)):
        if i < len(preceed) and len(preceed[i].span()) != conditions[i]:
            return 0
        else:
            print("toto")
            if len(preceed[i]) == conditions[i]:
                count += enumerate_condition(
                    left[to_replace + 1 :], conditions[i + 1 :], count
                )
            elif len(preceed[i]) < conditions[i] and preceed[i].span()[1] == (
                to_replace - 1
            ):
                count += enumerate_condition(
                    right[preceed[i].span()[0] :], conditions[i:], count
                )
            else:
                return 0
    if len(preceed) == 0:
        count += enumerate_condition(left[to_replace:], conditions, count)
        count += enumerate_condition(right[to_replace:], conditions, count)

    return count


print(enumerate_condition("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 0))


"""

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
"""
