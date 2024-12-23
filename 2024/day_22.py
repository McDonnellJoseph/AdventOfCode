import numpy as np 

with open("input.txt") as f:
    input = f.read().splitlines()


def step(arr):
    # Multiply by 64
    res = arr * 64
    # Mix
    arr = np.bitwise_xor(arr, res)
    # Prune 
    arr = arr % 16777216
    # Divide by 32 and round 
    res = arr // 32
    # Mix
    arr = np.bitwise_xor(arr, res)
    # Prune
    arr = arr % 16777216
    # Multiply by 2048 and round 
    res = arr * 2048
    # Mix
    arr = np.bitwise_xor(arr, res)
    # Prune
    arr = arr % 16777216

    return arr

def part_1(input):
    arr = np.array([int(i) for i in input])

    for i in range(2000):
        arr = step(arr)
    return arr.sum()

def part_2(input):
    arr = np.array([int(i) for i in input])
    changes = np.zeros((2000, len(input)))

    values = np.zeros((2000, len(input)))
    print("Values shape", values.shape)
    # Record all changes
    for i in range(2000):
        next_arr = step(arr)
        changes[i] = next_arr % 10- arr % 10
        values[i,:] = next_arr % 10
        arr = next_arr

    MEM = {}
    # Get set of unique sequences
    for i in range(3, 2000):
        sequences = changes[i-3:i+1, :]
        assert sequences.shape[0] == 4
        values_slice = values[i]
        for j in range(sequences.shape[1]):
            seq = sequences[:, j]

            if tuple(seq) not in MEM:
                MEM[tuple(seq)] = {j:values_slice[j]}
            else:
                if j not in MEM[tuple(seq)]:
                    MEM[tuple(seq)][j] = values_slice[j]
    
    best = 0

    for s in MEM:
        maybe_best = 0
        for key in MEM[s]:
            maybe_best += MEM[s][key]
        if maybe_best > best:
            best = maybe_best

    print(MEM[-2, 1, -1, 3])


    return best
print(part_1(input))

    
print(part_2(input))