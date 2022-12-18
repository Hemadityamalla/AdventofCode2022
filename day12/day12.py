#Add import libs below
from collections import deque
from math import inf as INFINITY

def parseInput(fin):
    #Different because we are reading in a binary format
    lines = fin.read().splitlines()
    grid = list(map(list, lines))
    return grid


def bfs(grid, src, dst, get_neighbors):
    h,w = len(grid), len(grid[0])
    #List of coordinates to visit are made as a queue
    queue = deque([(0,src)])#a queue of tuples- dist from src, coords
    visited = set()
    #While there are coordinates to visit
    while queue:
        dist,rc = queue.popleft()
        #If we reach the destination return the distance
        if rc == dst or grid[rc[0]][rc[1]] == dst:
            return dist

        #Skip visited nodes
        if rc not in visited:
            visited.add(rc)


            for n in get_neighbors(grid,rc[0],rc[1],h,w):
                if n in visited:
                    continue
                #Add the neighbor to the queue with the current distance+1
                queue.append((dist+1, n))
        print(queue)
    return INFINITY

def neighbors4(grid, r,c,h,w):
    for nr,nc in ((r+1, c), (r-1,c), (r, c+1), (r,c-1)):
        if 0 <= nr<h and 0<=nc<w:
            yield nr, nc
def neighbors_forward(grid, r,c,h,w):
    max_el = grid[r][c]+1
    neigh = neighbors4(grid, r,c,h,w)
    yield from ((nr,nc) for nr,nc in neigh if grid[nr][nc]<=max_el)
def neighbors_backward(grid, r,c,h,w):
    min_el = grid[r][c]-1
    neigh = neighbors4(grid, r,c,h,w)
    yield from ((nr,nc) for nr,nc in neigh if grid[nr][nc]>=min_el)

if input("test/real?") == "test":
    grid = parseInput(open("test.inp", "rb"))
else:
    grid = parseInput(open("day12.inp", "rb"))


#Predefining some constants in binary
START, END, LOWEST, HIGHEST = b'SEaz'


#Finding the source and destination
src = dst = None
for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col == START:
            src = r,c
            grid[r][c] = LOWEST
        elif col == END:
            dst=r,c
            grid[r][c] = HIGHEST
    if src and dst:
        break

#Part 1
print("Part 1: ", bfs(grid, src, dst, neighbors_forward))



#Part 2
print("Part 2: ", bfs(grid, dst, LOWEST, neighbors_backward))

