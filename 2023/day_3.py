with open("input.txt", "r") as f:
    input = f.read()


lines = input.splitlines()
engine_nb = []
gear_ratios = []
for i, line in enumerate(lines):
    for j, word in enumerate(line):
        # if word != "." and not word.isdigit():
        if word == "*":
            current_ratios = []
            # print(word)
            adjacents = []
            for I in [1, 0, -1]:
                for J in [-1, 0, 1]:
                    try:
                        val = lines[i + I][j + J]
                    except IndexError:
                        continue
                    if val.isdigit():
                        back = -1
                        forward = 1
                        while lines[i + I][j + J + back].isdigit():
                            back -= 1
                        print(j, J, len(line))
                        print(lines[i + I])
                        while (
                            j + J + forward < len(line)
                            and lines[i + I][j + J + forward].isdigit()
                        ):
                            print("THis forward", forward)
                            forward += 1
                        final_val = lines[i + I][j + J + back + 1 : j + J + forward]
                        current_ratios.append(int(final_val))
                        new_string = (
                            lines[i + I][: j + J + back + 1]
                            + "." * len(final_val)
                            + lines[i + I][j + J + forward :]
                        )
                        assert len(new_string) == len(line)

                        lines[i + I] = new_string
                        # print("here")
                        # print(final_val)
            import math

            if len(current_ratios) > 1:
                gear_ratios.append(math.prod(current_ratios))

print(lines)
print(engine_nb)
print(sum(engine_nb))
print(sum(gear_ratios))
