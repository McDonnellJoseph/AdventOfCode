with open("input.txt") as f:
    input = f.read()
    input = input.splitlines()

antenas = {}
antinode_map = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        antinode_map[(i,j)] = []
        if input[i][j].isalnum():
            antena = input[i][j]
            if antena in antenas:
                antenas[antena].append((i,j))
            else:
                antenas[antena] = [(i,j)]


from itertools import combinations

def find_antinodes(coords, antena):
    print("##")
    # For each pair of two coordinates
    for coordA, coordB in combinations(coords, 2):
        print(coordA, coordB)
        # we place an antinode at 
        for i in range(len(input)):
            antinode1 = (coordA[0] - (i+1) * (coordA[0] - coordB[0]), coordA[1] - (i+1) * (coordA[1] - coordB[1]))
            antinode2 = (coordA[0] + i *(coordA[0] - coordB[0]), coordA[1] + i *(coordA[1] - coordB[1]))
        

            if antinode1 in antinode_map:
                antinode_map[antinode1].append(antena)
            
            if antinode2 in antinode_map:
                antinode_map[antinode2].append(antena)

        print(antinode1, antinode2)
        #antinode2 = (coordB[0] + 2 *(coordB[0] - coordA[0]), coordB[1] - (coordB[1] - coordA[1]))


        if antinode1 in antinode_map:
            antinode_map[antinode1].append(antena)
        
        if antinode2 in antinode_map:
            antinode_map[antinode2].append(antena)

for antena in antenas:
    find_antinodes(antenas[antena], antena)
    ...
#find_antinodes(antenas["A"], "A")


for i in range(len(input)):
    print("".join(["#" if antinode_map[(i,j)] else "." for j in range(len(input[0]))]))

print(sum([True if antinode_map[antinode] else False for antinode in antinode_map]))
