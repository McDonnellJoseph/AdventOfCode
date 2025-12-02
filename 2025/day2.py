with open("input.txt") as f:
    ipt = f.read().strip("\n")

ranges = ipt.split(",")

total_p1 = 0
total_p2 = 0
p2_elms = []
for eg in ranges:
    range_start, range_end = eg.split("-")
    print("############")
    print(eg)
    for elem in range(int(range_start), int(range_end) + 1):
        str_elem = str(elem)

        if len(str_elem) % 2 == 0:
            middle = len(str_elem) // 2

            if str_elem[:middle] == str_elem[middle:]:
                # print("Part 1")
                # print(str_elem)
                total_p1 += int(str_elem)

        digits = list(str_elem)
        candidates = []
        for i in range(1, len(str_elem)):
            if len(str_elem) % i != 0:
                pass

            else:
                step = len(str_elem) // i
                elems = ["".join(digits[j * i : (j + 1) * i]) for j in range(step)]
                # print("ELEME", elem)
                # print("elems", elems, "elems set", set(elems))
                if len(set(elems)) == 1:
                    # print("Part 2")
                    # print("str", str_elem, "elems", elems)
                    # total_p2 += int(str_elem)
                    candidates.append(str_elem)
                    # p2_elms.append(str_elem)
        total_p2 += sum(int(el) for el in set(candidates))


print(total_p1)
print(total_p2)
print(p2_elms)
