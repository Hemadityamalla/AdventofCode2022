#Add import libs below
from collections import defaultdict
from collections import deque

def parseInput(fin):
    G = defaultdict(list)
    for edge in fin:
        a, b = edge.rstrip().split("-")
        if b != "start":
            G[a].append(b)
        if a != "start":
            G[b].append(a)
    return G



#G = parseInput(open("test.inp"))
G = parseInput(open("day12.inp"))

def n_paths(G, src, dst):
    #In the format
    # (node to visit, set of nodes visited to get there)
    stack = deque([(src, {src})])
    total = 0
    while stack:
        node, visited = stack.pop()
        if node == dst:
            total += 1
            continue
        for n in G[node]:
            if n in visited and n.islower():
                continue
            # The | operator performs a union of two sets
            stack.append((n, visited | {n}))
    return total
def n_paths2(G, src, dst):
    stack = deque([(src, {src}, False)])
    total = 0

    while stack:
        node, visited, double = stack.pop()
        if node == dst:
            total += 1
            continue

        for n in G[node]:
            if n not in visited or n.isupper():
                stack.append((n, visited | {n}, double))
                continue

            if double:
                continue

            stack.append((n, visited, True))

    return total


#Part 1
print("Part 1: ", n_paths(G, "start", "end"))



#Part 2
print("Part 2: ", n_paths2(G, "start", "end"))

