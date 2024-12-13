import numpy as np 
import re 
with open("input.txt") as f:
    input = f.read()

machines = input.split("\n\n")
total_p1 = 0
for machine in machines:
    lines = machine.splitlines()
    ax, ay = [int(_) for _ in re.findall(r'\d+',lines[0])]
    bx, by = [int(n) for n in re.findall(r'\d+',lines[1])]
    x, y = [int(n) for n in re.findall(r'\d+',lines[2])]

    a_arr = np.array([[ax, bx], [ay, by]])
    b_arr = np.array([x,y])
    sol = np.linalg.solve(a_arr, b_arr)
    # Test if it works
    answ_a, answ_b = int(sol[0]), int(sol[1])

    if ax *answ_a + bx * answ_b == x and ay * answ_a + by *answ_b == y:
        total_p1 += 3 * int(answ_a) + int(answ_b)
print(total_p1)