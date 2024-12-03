import re 

with open("input.txt") as f:
    ipt = f.read()


regex = r"mul\(\d+,+\d+\)"

total = 0 

for match in re.findall(regex, ipt):
    match = match.strip("mul(")
    match = match.strip(")")
    left, right = match.split(",")
    total += int(left) * int(right)

print("Part 1")
print(total)

regex_part2 = r"(mul\(\d+,+\d+\))|(don't\(\))|(do\(\))"

update = True
total = 0
for match, dont, do in re.findall(regex_part2, ipt):
    print(match, dont, do)
    if dont:
        update = False
        print(update)
        continue
    elif do:
        update = True
        print(update)
        continue
    elif update:
        match = match.strip("mul(")
        match = match.strip(")")
        left, right = match.split(",")
        total += int(left) * int(right)

print("Part 2")
print(total)