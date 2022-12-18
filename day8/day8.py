#Add import libs below

def parseInput(fin):
    t = fin.read().rstrip().split("\n")
    return [[x for x in y] for y in t]



grid = parseInput(open("test.inp"))
grid = parseInput(open("day8.inp"))


lx,ly = len(grid[0]), len(grid)
dxy = [(x,y) for x,y in zip([1,0,-1,0],[0,1,0,-1])]
def visible_trees(grid, ix, iy):
    right = grid[ix][iy+1:]
    left = grid[ix][:iy]
    top = [x[iy] for x in grid[:ix]]
    bottom = [x[iy] for x in grid[ix+1:]]
    #print("Start check of ",grid[ix][iy], ix,iy)
    if all([grid[ix][iy]>x for x in left]):
        print("left", grid[ix][iy],ix,iy)
        return 1
    if all([grid[ix][iy]>x for x in right]):
        print("right", grid[ix][iy],ix,iy)
        return 1
    if all([grid[ix][iy]>x for x in top]):
        print("top", grid[ix][iy],ix,iy)
        return 1
    if all([grid[ix][iy]>x for x in bottom]):
        print("bottom", grid[ix][iy],ix,iy)
        return 1
    return 0
    

visible = 2*(lx+ly-2)
for i in range(1,lx-1):
    for j in range(1,ly-1):
        print(visible)
        visible+=visible_trees(grid, i,j)
#Part 1
print("Part 1: ", visible)
def calc_scenic_score(grid, ix,iy):
    right = grid[ix][iy+1:]
    left = grid[ix][:iy]
    top = [x[iy] for x in grid[:ix]]
    bottom = [x[iy] for x in grid[ix+1:]]
    left.reverse()
    top.reverse()
    score = 1
    #Right score
    for i,x in enumerate(right):
        if grid[ix][iy]<=x:
            break
    print("Right", i)
    score*=(i+1)
    #Right score
    for i,x in enumerate(left):
        if grid[ix][iy]<=x:
            break
    print("Left", i)
    score*=(i+1)
    for i,x in enumerate(top):
        if grid[ix][iy]<=x:
            break
    print("Top", i)
    score*=(i+1)
    for i,x in enumerate(bottom):
        if grid[ix][iy]<=x:
            break
    print("Botthom", i)
    score*=(i+1)
    print(ix,iy,grid[ix][iy],score)
    print(top, left, bottom, right)
    return score


scenic_score = []
for i in range(1,lx-1):
    for j in range(1,ly-1):
        scenic_score.append(calc_scenic_score(grid, i,j))


#Part 2
print("Part 2: ", max(scenic_score))

