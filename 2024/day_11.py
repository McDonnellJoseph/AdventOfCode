with open("input.txt") as f:
    input = f.read()


line = [int(number) for number in input.split()]



def blink(line):
    # For each 0 
    index_offset = 0
    for i in range(len(line)):
        i += index_offset
        elem = line[i]

        # If stone is zero it turns to 1
        if elem == 0:
            line[i] = 1

        elif len(str(elem)) % 2 == 0:
            elem_str = str(elem)
            left, right = int(elem_str[:len(elem_str)//2]), int(elem_str[len(elem_str)//2:])

            line.insert(i, left)
            line.insert(i+1, right)
            del line[i+2]
            index_offset += 1

        else:
            line[i] = elem * 2024

    return line 

from functools import lru_cache

# For each 0 
@lru_cache(maxsize=None)
def digit_transform(digit, n_transformations):
    while len(str(digit)) % 2 != 0:
        if digit == 0:
            digit = 1
        else:
            digit = digit * 2024
        n_transformations += 1
    elem_str = str(digit)
    left, right = int(elem_str[:len(elem_str)//2]), int(elem_str[len(elem_str)//2:])
    return left, right, n_transformations + 1


for l in line:
    n_transformations = 0
    to_transform = [l]
    while n_transformations < 75:
        index_offset = 0
        for i, d in enumerate(to_transform):
            i += index_offset
            print(i,d)
            left, right, n_transformations = digit_transform(d, n_transformations) 
            to_transform.insert(i, left)
            to_transform.insert(i+1, right)
            print(to_transform)
            del to_transform[i+2]
            index_offset += 1
