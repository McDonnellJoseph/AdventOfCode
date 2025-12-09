import re 
import math
with open("input.txt") as f:
    ipt = f.read().splitlines()


matches = re.findall("\d+", ipt[0])
arr = [[] for i in range(len(matches))]

for line in ipt[:-1]:
    for i, c in enumerate(re.findall("\d+", line)):
        arr[i].append(int(c))

arr_2 = [[] for i in range(len(matches))]


operators = []
for ops in ipt[-1]:
    for i, op in enumerate(re.findall("(\*)|(\+)", ops)):
        if op[0] == "*":
            operators.append("*")
        elif op[1] == "+":
            operators.append("+")
        else:
            assert False
part_1 = 0
for i in range(len(operators)):
    column_nums = arr[i]
    op = operators[i]

    if op == "*":
        part_1 += math.prod(column_nums)
    elif op == "+":
        part_1 += sum(column_nums)

part_2 = 0

# For each operator
# Get the max 
col_start_idx = 0
for i in range(len(operators)):
    column_nums = arr[i]
    longest_len = len(str(max(column_nums)))

    str_columns = []
    final_columns = ["" for _ in range(longest_len)]
    # For each line
    for line in ipt[:-1]:
        str_columns.append(line[col_start_idx:col_start_idx+longest_len])

    for _, str_num in enumerate(str_columns):
        for j, c in enumerate(str_num):
            if c != " ":

                final_columns[j] += c
    
    final = [int(c) for c in final_columns]
    op = operators[i]
    print(final, op)

    if op == "*":
        part_2 += math.prod(final)
        print(math.prod(final))
    elif op == "+":
        part_2 += sum(final)
        print(sum(final))

    col_start_idx += longest_len +1
  


print("PART 1", part_1)
print("PART 2", part_2)
