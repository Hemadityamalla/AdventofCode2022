#Add import libs below

def parse_cave(cave):
    xcoords = [x for x,_ in cave]
    xmin, xmax = min(xcoords), max(xcoords)
    ymax = max([y for _,y in cave])+1
    for y in range(ymax):
        m = ""
        for x in range(xmin, xmax+1):
            if (x,y) in cave:
                m+="#"
            else:
                m+="."
        print(m)
    return True


def updatecavefloor(cave, ymax):
    #Add a horizontal line  for ymax
    xcoords = [x for x,_ in cave]
    xmin, xmax = min(xcoords), max(xcoords)
    for x in range(xmin, xmax+1):
        cave.add((x,ymax))
    return cave

def range2d(a,b):
    ax,ay = a
    bx,by = b


    if ax == bx: #Vertical line
        for y in range(min(ay,by), max(ay,by)+1):
            yield ax,y
    else: #Horizontal line
        for x in range(min(ax,bx), max(ax,bx)+1):
            yield x,ay
def parseInput(fin):
    cave = set() #Here we only keep track of the rock-coordinates
    for line in fin:
        points = line.split(" -> ")
        points = map(lambda p:p.split(","), points)
        points = map(lambda p:(int(p[0]), int(p[1])), points)


        prev = next(points) #This pops the first point in the generator
        for cur in points: #This loop starts with the second point
            cave.update(range2d(cur, prev))
            prev = cur
    return cave




if input("test/real?") == "test":
    cave = parseInput(open("test.inp"))
else:
    cave = parseInput(open("day14.inp"))
parse_cave(cave)
#Getting the edge of the cave (y coordinate) -- there was a oneliner usingoperator.itemgetter
maxy = max([x[1] for x in cave])
#Simulating the pouring of a single unit of sand
def pour_sand(cave, maxy):
    x,y = 500,0 #Origin of the sand
    while y< maxy:
        if (x,y+1) not in cave:
            y+=1
            continue
        if (x-1, y+1) not in cave:
            x,y = x-1, y+1
            continue
        if (x+1,y+1) not in cave:
            x,y = x+1, y+1
            continue
        cave.add((x,y))
        return True
    return False
sand = 0
cave1 = cave.copy()
while pour_sand(cave1, maxy):
    sand+=1
parse_cave(cave1)
#Part 1
print("Part 1: ", sand)

maxy+=2
cave = updatecavefloor(cave, maxy)
parse_cave(cave)

def pour_sand2(cave, maxy):
    x,y = 500,0 #Origin of the sand
    i = 0
    while y< maxy:
        i+=1
        #xcoords = [x for x,_ in cave]
        #xmin, xmax = min(xcoords), max(xcoords)
        if (x,y+1) not in cave:
            y+=1
            continue
        elif  (x-1, y+1) not in cave:
            x,y = x-1, y+1
            continue
        elif (x+1,y+1) not in cave:
            x,y = x+1, y+1
            continue
        cave.add((x,y))
        return True
    return False
#sand = 0
#while pour_sand2(cave, maxy):
#    sand+=1
#parse_cave(cave)

xcoords = [x for x,_ in cave]
xmin, xmax = min(xcoords), max(xcoords)
tol = 5
cave.update(range2d((xmin-tol, maxy), (xmax+tol, maxy)))
parse_cave(cave)
sand = 0
while pour_sand2(cave, maxy):
    sand+=1
    print(sand)
    if (500,0) in cave:
        break
    else:
        xcoords = [x for x,_ in cave]
        xmin, xmax = min(xcoords), max(xcoords)
        tol = 1
        cave.update(range2d((xmin-tol, maxy), (xmax+tol, maxy)))

parse_cave(cave)
#Part 2
print("Part 2: ", sand)

