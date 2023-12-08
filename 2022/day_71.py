ALL_DIR, SIZES, pos = set(), {}, tuple()
NEW_POS = {
    "..": lambda pos, cmd: pos[:-1],
    "/": lambda pos, cmd: tuple(),
    "default": lambda pos, cmd: pos + (cmd,),
}
for line in open("input.txt").read().split("\n")[:-1]:
    n, _dir = line.split(" ")[-2:]
    if line.startswith("$ cd"):
        pos = NEW_POS.get(_dir, NEW_POS["default"])(pos, _dir)
        ALL_DIR |= {pos}
    elif "$ ls" not in line and "dir" not in line:
        SIZES[pos + (_dir,)] = int(n)
AVAILABLE = 70000000 - sum(SIZES.values())
ALL_SIZES = [
    sum(SIZES[key] for key in SIZES if key[: len(_dir)] == _dir) for _dir in ALL_DIR
]
print(SIZES)
print("the answer 1 is : ", sum(i * (i < 100000) for i in ALL_SIZES))
print("the answer 2 is : ", min(i for i in ALL_SIZES if AVAILABLE + i >= 30000000))
