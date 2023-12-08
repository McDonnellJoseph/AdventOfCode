with open("input.txt", "r") as f:
    input = f.read()


results = {}
results["seeds"] = [toto for toto in input.splitlines()[0].split(":")[1].split()]

results["part2"] = []


def convert(seed_range):
    # Intialise the matches with the original seed range
    matches = [seed_range]

    # For each conversion step 
    # We go from val_prev to val_next and record this change in matches
    for i, conversion in enumerate(input.split("\n\n")):
        # At each step we should always the same amount of numbers
        # All we are doing is offsetting
        if i == 0:
            continue
        lines = conversion.splitlines()
        print(lines[0])
        print(len(matches))
        conv_dict = {}
        matches_converted = []
        for match in matches:
            converted = []
            new_matches = []
            print("Working range", match)
            for line in lines[1:]:
                dest_start, origin_start, nb = line.split()
                dest_start, origin_start, nb = (
                    int(dest_start),
                    int(origin_start),
                    int(nb),
                )
                origin_range = range(origin_start, origin_start + nb)
                # Match between input and target
                intersection = range(
                    max(match[0], origin_range[0]),
                    min(match[-1], origin_range[-1]) + 1,
                )
                # If match is true we convert and go to next
                if intersection:
                    # Handle conversion 
                    conversion = dest_start - origin_start 
                    start_point = intersection[0] + conversion
                    end_point = intersection[-1] + conversion + 1
                    converted_range = range(start_point, end_point)
                    conv_dict[intersection] = converted_range
                    new_matches.append(intersection)

            sorted_new_matches = sorted(new_matches, key=lambda k: k[0])
            if not sorted_new_matches:
                print("We found no matches")
                sorted_new_matches =[match]
                converted = [match]
            else:
                print("We found the following matches", sorted_new_matches)
                print("We have the following conversions", conv_dict)
                first_is_identical = False
                if sorted_new_matches[0][0] > match[0]:
                    first_is_identical = True
                    sorted_new_matches.insert(0, range(match[0],sorted_new_matches[0][0]))

                last_is_identical = False
                if sorted_new_matches[-1][-1] < match[-1]:
                    last_is_identical = True
                    sorted_new_matches.append(range(sorted_new_matches[-1][-1]+1, match[-1]+1))

                for index, val in enumerate(sorted_new_matches[:-1]):
                    if index == 0 and first_is_identical:
                        converted.append(val)
                    else:
                        converted.append(conv_dict[val])
                        if val[-1] +1 < sorted_new_matches[index+1][0]:
                            converted.append(range(val[-1]+1, sorted_new_matches[index+1][0]))

                if not last_is_identical:
                    converted.append(conv_dict[sorted_new_matches[-1]])
                else:
                    converted.append(sorted_new_matches[-1])

            
            count_new = sum([len(match) for match in sorted_new_matches])
            count_converted = sum([len(toto) for toto in converted])
            print("Base")
            print(count_new, len(match))
            assert count_new == len(match)
            print("Converted")
            print(count_converted, len(match))
            assert count_converted == len(match)
            matches_converted += converted
        count_matches = sum([len(match) for match in matches])
        count_converted_total = sum([len(toto) for toto in matches_converted])
        assert count_matches == count_converted_total

        matches = matches_converted

    return min([res[0] for res in matches])

# print(convert(range(82,83)))
ranges = []
final_results = []
for i, toto in enumerate(results["seeds"]):
    if i % 2 == 1:
        start, nb = int(results["seeds"][i - 1]), int(toto)
        ranges.append(range(start, start + nb))

for i in range(len(ranges)):
    final_results.append(convert(ranges[i]))

# import concurrent.futures
# futures= []
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     for i in range(10):
#         future = executor.submit(convert, ranges[i])
#         futures.append(future)

# final_results = [future.result() for future in concurrent.futures.as_completed(futures)]

print(final_results)
print(min(final_results))
