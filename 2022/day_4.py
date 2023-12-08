with open("input.txt", "rb") as f:
    input = f.read().decode("utf-8")

pairs = input.split("\n")[:-1]
import numpy as np

count = 0
# Part 1
for pair in pairs:
    elf1, elf2 = pair.split(",")
    start_elf1, end_elf1 = elf1.split("-")
    start_elf2, end_elf2 = elf2.split("-")
    min = np.argmin([int(start_elf1), int(start_elf2)])
    max = np.argmax([int(end_elf1), int(end_elf2)])
    if int(start_elf1) == int(start_elf2):
        count += 1
    elif int(end_elf1) == int(end_elf2):
        count += 1
    elif min == max:
        count += 1

pairs = input.split("\n")[:-1]
# Part 2
count = 0
for pair in pairs:
    elf1, elf2 = pair.split(",")
    start_elf1, end_elf1 = elf1.split("-")
    start_elf2, end_elf2 = elf2.split("-")
    max_start = np.max([int(start_elf1), int(start_elf2)])
    min_end = np.min([int(end_elf1), int(end_elf2)])

    if max_start <= min_end:
        count += 1

print(count)
