with open("input.txt", "r") as f:
    input = f.read()

# # part 1
# final = []
# for line in input.split("\n"):
#     cal_values = []
#     for c in line:
#         if c.isdigit():
#             cal_values.append(c)
#     final.append(int(cal_values[0] + cal_values[-1]))

# part 2
valid_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
result = []
for line in input.split("\n"):
    print(line)
    cal_values = ["-1" for i in range(len(line))]
    final_line = []
    low_pos = 1000
    max_pos = -1000
    for i, dig in enumerate(valid_digits):
        toto = line.find(dig)
        if toto > -1:
            cal_values[toto] = str(i + 1)
        lala = line.rfind(dig)
        if toto > -1:
            cal_values[lala] = str(i + 1)
    for j, c in enumerate(line):
        if c.isdigit():
            cal_values[j] = c
    print(cal_values)
    for val in cal_values:
        if val.isdigit():
            final_line.append(val)
    print(final_line[0] + final_line[-1])
    result.append(int(final_line[0] + final_line[-1]))


print(sum(result))
D = {str(i): i for i in range(1, 10)} | {
    i: idx + 1
    for idx, i in enumerate(
        [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
    )
}
for part in (1, 2):
    print(
        f"the answer {part} is : ",
        sum(
            _l[0] * 10 + _l[-1]
            for _l in (
                [
                    D[n]
                    for idx in range(len(line))
                    for n in D
                    if line[idx:].startswith(n) and (part == 2 or len(n) == 1)
                ]
                for line in open("input.txt").read().split("\n")
            )
        ),
    )
