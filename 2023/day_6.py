with open("input.txt", "r") as f:
    input = f.read()


text_time, text_distance = input.splitlines()

times, distances = [], []

counts = []


def compute_distances(time, distance):
    return [t * (time - t) for t in range(time + 1) if t * (time - t) > distance]


final_time, final_distance = "", ""
for time, distance in zip(
    text_time.split(":")[1].split(), text_distance.split(":")[1].split()
):
    final_time += time
    final_distance += distance

counts.append(len(compute_distances(int(final_time), int(final_distance))))


print(counts)
