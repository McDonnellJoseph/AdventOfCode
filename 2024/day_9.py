from typing import List


with open("input.txt") as f:
    input = f.read().strip("\n")


def to_sparse(dense):
    fs = []
    block_sizes = []
    empty_blocks = []
    p2 = []
    idx_pointer = 0
    block_pointer = 0
    for i in range(len(dense)):
        if i % 2 == 0:
            to_add = [i // 2] * int(dense[i])
            block_sizes.append((block_pointer, block_pointer + int(dense[i])))
            idx_pointer += int(dense[i])
            block_pointer += int(dense[i])
            fs.extend(to_add)
            p2.append((idx_pointer, idx_pointer + int(dense[i]), i // 2, 0))
        else:
            empty_blocks.append((idx_pointer, idx_pointer + int(dense[i])))
            empty_blocks.append((idx_pointer, idx_pointer + int(dense[i])))
            p2.append((idx_pointer, idx_pointer + int(dense[i]), -1))
            idx_pointer += int(dense[i])

    return fs, empty_blocks, block_sizes, p2


def move_blocks(sparse, empty_blocks):
    for start, end in empty_blocks:
        size = end - start
        for i in range(size):
            last = sparse[-1]
            sparse.insert(start + i, last)
            del sparse[-1]
    return sparse


def print_state(state):
    to_print = ""
    for i in range(len(state)):
        if state[i][2] < 0:
            to_print += "." * (state[i][1] - state[i][0])
        else:
            to_print += str(state[i][2]) * (state[i][1] - state[i][0])
    return to_print


def part22(fs):
    index_offset = 0
    # Rebuild the array
    for i in reversed(range(len(fs))):
        i += index_offset
        # if block skip
        if fs[i][2] < 0 or fs[i][3]:
            continue
        # Iterate starting from end
        block_start, block_end = fs[i][0], fs[i][1]
        block_size = block_end - block_start

        made_move = False

        for k in range(i):
            if fs[k][2] != -1:
                continue
            empty_start, empty_end = fs[k][0], fs[k][1]
            empty_size = empty_end - empty_start
            # If the empty block is big enough to fit the file block
            if empty_size >= block_size:
                dist = fs[i][0] - fs[k][0]
                # Insert the block
                fs.insert(k, (fs[i][0] - dist, fs[i][1] - dist, fs[i][2], 1))
                # Insert Empty space where the block used to be
                fs.insert(i + 1, (fs[i + 1][0], fs[i + 1][1], -1))
                # Update the space
                if empty_size > block_size:
                    fs[k + 1] = (
                        fs[k + 1][0] + block_size,
                        fs[k + 1][1],
                        -1,
                    )
                    del fs[i + 2]
                    index_offset += 1
                else:
                    del fs[k + 1]
                    del fs[i + 1]
                made_move = True
                break
            if not made_move:
                fs[i] = (fs[i][0], fs[i][1], fs[i][2], 1)

    return fs


fs, empty_blocks, block_sizes, p2 = to_sparse(input)

fs = part22(p2)
fs = part22(p2)
fs = part22(p2)
count = 0
index = 0
for block in fs:
    if block[2] >= 0:
        count += block[2] * sum(range(index, index + (block[1] - block[0])))
    index += block[1] - block[0]
print(count)
