with open("input.txt") as f:
    input = f.read()

ACCEPTED = []
REJECTED = []


def return_lambda_inf(maxval):
    return lambda x: x < maxval


def return_lambda_sup(minval):
    return lambda x: x > minval


def lambda_inf_range(maxval):
    return lambda x: (range(x[0], maxval), range(maxval, x[-1] + 1))


def lambda_sup_range(minval):
    return lambda x: (range(minval + 1, x[-1] + 1), range(x[0], minval + 1))


# Step 1: Create a dictionnary
class Workflow:
    def __init__(self, conditions, name):
        self.name = name
        conditions = conditions.split(",")
        checks = []
        for condition in conditions[:-1]:
            func, workflow = condition.split(":")
            if func[1] == "<":
                # checks.append({func[0]: (return_lambda_inf(int(func[2:])), workflow)})
                checks.append({func[0]: (lambda_inf_range(int(func[2:])), workflow)})

            elif func[1] == ">":
                # checks.append({func[0]: (return_lambda_sup(int(func[2:])), workflow)})
                checks.append({func[0]: (lambda_sup_range(int(func[2:])), workflow)})

            else:
                assert False
        checks.append(conditions[-1])
        self.checks = checks

    def __repr__(self):
        return self.name

    def evaluate_input(self, input_raw):
        # Create input dict
        print("Entering this object", self)
        print("This is the input", input_raw)
        input = input_raw[1:-1]
        input_dict = {}
        print("toto", input.split(","))
        for part in input.split(","):
            label, val = part.split("=")
            input_dict[label] = int(val)

        for cond in self.checks[:-1]:
            letter = list(cond.keys())[0]
            val = input_dict[letter]
            print("This is the cond", cond)
            func, go_to = cond[letter]
            if func(val):
                # if workflow evaluate
                if go_to == "A":
                    ACCEPTED.append(input)
                elif go_to == "R":
                    REJECTED.append(input)
                else:
                    factory[go_to].evaluate_input(input_raw)
                return True
        go_to = self.checks[-1]
        if go_to == "A":
            ACCEPTED.append(input)
        elif go_to == "R":
            REJECTED.append(input)
        else:
            factory[go_to].evaluate_input(input_raw)

    def evaluate_range(self, range_input, accepted=[]):
        for cond in self.checks[:-1]:
            letter = list(cond.keys())[0]
            func, go_to = cond[letter]

            to_evaluate = range_input[letter]
            true_range, false_range = func(to_evaluate)

            if true_range:
                true_output = range_input.copy()
                true_output[letter] = true_range
                if go_to == "A":
                    accepted.append(true_output)
                elif go_to == "R":
                    pass
                else:
                    accepted += factory[go_to].evaluate_range(true_output)

            if false_range:
                range_input[letter] = false_range
            else:
                return accepted
        go_to = self.checks[-1]
        if go_to == "A":
            accepted.append(range_input)
            return accepted
        elif go_to == "R":
            return accepted
        else:
            return accepted + factory[go_to].evaluate_range(range_input)


worfklows, inputs = input.split("\n\n")
factory = {}
for workflow in worfklows.splitlines():
    name = workflow[: workflow.find("{")]
    flow = workflow[workflow.find("{") + 1 : workflow.find("}")]
    factory[name] = Workflow(flow, name)

# Part 1
"""
for toto in inputs.splitlines():
    factory["in"].evaluate_input(toto)


def count_accepted(accepted):
    total = 0
    for acc in accepted:
        vals = acc.split(",")
        for val in vals:
            total += int(val[val.find("=") + 1 :])
    return total


print(ACCEPTED)

print(REJECTED)

print(count_accepted(ACCEPTED))
"""

# Part 2 = Part 1 with intervals
ACCEPTED = []
REJECTED = []
base_input = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001),
}

accepted_ranges = factory["in"].evaluate_range(base_input)
print(accepted_ranges)

import math
from operator import mul
from functools import reduce


print(len(accepted_ranges))
total = 0
for acc in accepted_ranges:
    # check if a set is included in another
    print(acc)
    caca = [len(x) for x in acc.values()]
    fac = reduce(mul, caca, 1)
    total += fac
print(total)
print(167409079868000)

# print(ACCEPTED)
