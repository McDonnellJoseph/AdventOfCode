import numpy as np 
import re 
from z3 import Ints, Solver, sat, ToInt
with open("input.txt") as f:
    input = f.read()

machines = input.split("\n\n")
total_p1 = 0
x, y = Ints('x y')
for machine in machines:
    lines = machine.splitlines()
    ax, ay = [int(_) for _ in re.findall(r'\d+',lines[0])]
    bx, by = [int(n) for n in re.findall(r'\d+',lines[1])]
    ans_a, ans_b = [int(n) for n in re.findall(r'\d+',lines[2])]
    solver = Solver()
    solver.add(*[ax * x + bx * y == ans_a+10000000000000, ay * x + by * y== ans_b+10000000000000, x > 0, y > 0])
    # Test if it works
    if solver.check() == sat:
        print("here")
        model = solver.model()
        print("model x ", model[x])
        total_p1 += 3 * model[x].as_long() + model[y].as_long()

print(total_p1)
