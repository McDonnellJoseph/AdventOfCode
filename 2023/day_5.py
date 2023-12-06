with open("input.txt", "r") as f:
    input = f.read()


results = {}
results["seeds"] = [toto for toto in input.splitlines()[0].split(":")[1].split()]

results["part2"] = []


def convert(seed_range):
    matches = [seed_range]
    for i, conversion in enumerate(input.split("\n\n")):
        if i == 0:
            continue
        lines = conversion.splitlines()
        print(lines[0])
        new_matches = []
        for match in matches:
            print("Working range", match)
            to_add = [match]
            for line in lines[1:]:
                dest_start, origin_start, nb = line.split()
                dest_start, origin_start, nb = (
                    int(dest_start),
                    int(origin_start),
                    int(nb),
                )

                origin_range = range(origin_start, origin_start + nb)
                print("origin_range")
                print(origin_range)
                # Match between input and target

                intersection = range(
                    max(match[0], origin_range[0]),
                    min(match[-1], origin_range[-1]) + 1,
                )
                print("This is the intersection")
                print(intersection)
                # If match is true we convert and go to next
                if intersection:
                    print("We reached a conversion")
                    conversion = origin_start - dest_start
                    start_point = intersection[0] + conversion
                    end_point = intersection[-1] + conversion + 1
                    converted_range = range(start_point, end_point)
                    print(converted_range)
                    # Append intersection
                    new_matches.append(converted_range)
                    to_del = []
                    for cnt, add in enumerate(to_add):
                        if intersection in add:
                            # Append beginning
                            if intersection[0] > add[0]:
                                to_add.append(range(match[0], add[0]))
                            # Append end
                            if intersection[-1] < match[-1]:
                                to_add.append(range(intersection[-1] + 1, add[-1] + 1))
                            to_del.append(cnt)
                    for td in to_del:
                        del to_add[td]
            for match in to_add:
                new_matches.append(match)
        matches = new_matches

    return matches


ranges = []
final_results = []
for i, toto in enumerate(results["seeds"]):
    if i % 2 == 1:
        start, nb = int(results["seeds"][i - 1]), int(toto)
        ranges.append(range(start, start + nb))
        working_range = range(start, start + nb)
        print("\n\n This is the working range")
        print(working_range)
        result = convert(working_range)
        """
        for j in range(nb):
            result = convert(start + j)
            if min and result < min:
                min = result
        """
        print(result)
        final_results.append(min([res[0] for res in result if res]))


print(final_results)
