with open("input.txt", "rb") as f:
    data_stream = f.read().decode("utf-8")

pos = 14
last_chars = list(data_stream[:14])

# Part 1
for c in data_stream[14:]:
    if len(set(last_chars)) == 14:
        print(pos)
        break
    del last_chars[0]
    last_chars.append(c)
    pos += 1
