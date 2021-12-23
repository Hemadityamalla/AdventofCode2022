#Add import libs below
from collections import deque

def parseInput(fin):
    lines = map(str.rstrip, fin)
    grid = tuple(tuple(map(int, row)) for row in lines)
    return grid

def neighbors4(h, w, r, c):
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        rr, cc = (r+dr, c+dc)
        if 0 <= rr <  h and 0 <= cc < w:
            yield (rr, cc)
def component_size(grid, src,h,w):
    queue = deque([src])
    visited = set()
    while queue:
        rc = queue.popleft()
        if rc in visited:
            continue
        visited.add(rc)
        for nr, nc in neighbors4(h,w ,*rc):
            #print(nc,nr)
            if grid[nr][nc] != 9 and (nc,nr) not in visited:
                queue.append((nr,nc))
    return len(visited)



#grid = parseInput(open("test.inp"))
grid = parseInput(open("day9.inp"))


h,w = len(grid), len(grid[0])
print(h,w)
total = 0
sinks = list()
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        #ok = True
        #for nr, nc in neighbors4(h,w,r,c):
        #    print(nr,nc)
        #    if grid[nr][nc] <= cell:
        #        ok = False
        #        break
        #if ok:
        #    total += cell + 1

        #The above commented part can be easily done in a single line using "all":
        if all(grid[nr][nc] > cell for nr, nc in neighbors4(h,w,r,c)):
            sinks.append((r,c))
            total += cell + 1
#Part 1
print("Part 1: ", total)


sizes = map(lambda s: component_size(grid, s, h, w), sinks)
sizes = sorted(sizes, reverse=True)

#Part 2
print("Part 2: ", sizes[0]*sizes[1]*sizes[2])

