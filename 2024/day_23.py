with open("input.txt") as f:
    input = f.read().splitlines()

def add_connections(connections, a, b):
        
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = {b}
    if b in connections:
        connections[b].add(a)
    else:
        connections[b] = {a}
    return connections


def get_connections(input):
    connections = {}

    for el in input:
        a, b = el.split("-")

        connections = add_connections(connections, a, b)
    return connections

def part1(input):
    trios = set()
    connections = get_connections(input)

    # In computer A connections
    for el in connections:
        # Get the connections of each connections
        for link in connections[el]:
            for sublink in connections[link]:
                if el in connections[sublink]:
                    if el[0] == "t" or link[0] == "t" or sublink[0] == "t":
                        trios.add(tuple(sorted((el, link, sublink))))
    
    # Filter starting with T
    return trios

import sys
sys.setrecursionlimit(1000000000)

def part2(input):
    trios = set()
    connections = get_connections(input)


    def dfs(conns, node, visited):
        # If we came back to the first node we have a cycle
        if node == start:
            return visited

        #print(visited)
        # If all the elements 
        if visited.issubset(conns[node]):
            visited.add(node)
            for con in conns[node]:
                if con not in visited:
                    visited = dfs(conns, con, visited)
    
        return visited

    largest_lan = None
    largest_lan_size = 0
    for el in connections:
        lan = {el}
        start = el
        for next_el in connections[el]:
            lan = dfs(connections, next_el, lan)
            if len(lan) > largest_lan_size:
                largest_lan_size = len(lan)
                largest_lan = lan

    # Filter starting with T
    return largest_lan
print(len(part1(input)))
print(",".join(sorted(part2(input))))
