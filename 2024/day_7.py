with open("input.txt") as f:
    input = f.read()

from itertools import product, combinations_with_replacement, permutations

def compute(factors, operators):
    result = factors[0]

    for i in range(1, len(factors)):
        if operators[i-1] == "+":
            result += factors[i]
        elif operators[i-1] == "*":
            result *= factors[i]
        elif operators[i-1] == "||":
            result = int(str(result) + str(factors[i]))
    return result

part1 = 0

part2 = 0

for operation in input.splitlines():
    # Parse input
    result, factors = operation.split(":")
    result = int(result)
    factors = [int(factor) for factor in factors.strip().split(" ")]
    op_set = set()
    # We have n - 1 slots available for an operator

    for operators in list(product(["*", "+"], repeat=len(factors) -1)):
        if result == compute(factors, operators):
            part1 += result
            break
    for operators in list(product(["*", "+", "||"], repeat=len(factors) -1)):
            if result == compute(factors, operators):
                part2 += result
                break


print(part1)
print(part2)