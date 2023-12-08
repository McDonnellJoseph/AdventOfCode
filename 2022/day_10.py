register = 1
cycle = 1

with open("input.txt") as f:
    input = f.read()
memory = []
for command in input.splitlines():
    if command.split()[0] == "noop":
        memory.append(register)
    else:
        amount = int(command.split()[1])
        memory.append(register)
        memory.append(register)
        register += amount

part_1 = 0

for n in [19, 59, 99, 139, 179, 219]:
    part_1 += memory[n] * (n + 1)

print(part_1)

screen_width = 40
screen_height = 6

assert screen_height * screen_width == len(memory)

text = ""
current_row = 0
current_col = 0
for i in range(len(memory)):
    if i % screen_width == 0 and i > 0:
        text += "\n"
        current_row += 1
        current_col = 0
    if (memory[i] - current_col) ** 2 < 2:
        text += "#"
    else:
        text += "."
    current_col += 1

print(text)
