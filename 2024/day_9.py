with open("input.txt") as f:
    input = f.read()


def to_sparse(dense):
    fs = []
    block_sizes = []
    empty_blocks = []
    idx_pointer = 0
    block_pointer = 0
    for i in range(len(dense)):
        if i % 2 == 0:
            to_add = [i//2] * int(dense[i])
            block_sizes.append((block_pointer, block_pointer+int(dense[i])))

            idx_pointer += int(dense[i])
            block_pointer += int(dense[i])

            fs.extend(to_add)

        else:
            #to_add = [-1] * int(dense[i])
            # (start index, end_index)
            empty_blocks.append((idx_pointer, idx_pointer+int(dense[i])))
            #fs.extend(to_add)
            idx_pointer += int(dense[i])
    return fs,empty_blocks, block_sizes

def move_blocks(sparse, empty_blocks):
    for start, end in empty_blocks:
        size = end - start 
        for i in range(size):
            last = sparse[-1]
            sparse.insert(start+i, last)
            del sparse[-1]
    return sparse

def update_blocks(block_list, update_size):
    ...

def move_blocksp2(sparse, empty_blocks, block_sizes):
    sparse_size = len(sparse)
    print(sparse[27])
    print(sparse[26])
    for i in range(len(block_sizes)):
        block_start, block_end = block_sizes[-1 - i]
        block_size = block_end - block_start
        print(block_start, block_end)
        print(sparse)
        for k, (start, end) in enumerate(empty_blocks):
            size = end - start 
            if size >= block_size:
                print("Block start end", start, end)
                for j in range(block_size):
                    print("block end",block_end, j)
                    print(len(sparse))
                    print(len(sparse))
                    #print(sparse[len(sparse)])
                    last = sparse[block_end - 1 - j ]
                    print("last", last)
                    sparse.insert(start+1+j, last)
                    block_end += 1
                    del sparse[-1]
                # update empty block with remaining space 
                
                empty_blocks[k] = (start + block_size, end)
        return sparse


fs, empty_blocks, block_sizes = to_sparse(input)
#arranged_blocks = move_blocks(fs, empty_blocks)

#print(sum([i * arranged_blocks[i] for i in range(len(arranged_blocks))]))
"00992111777.44.333....5555.6666.....8888.."
print(fs, len(fs))
print(move_blocksp2(fs, empty_blocks, block_sizes))