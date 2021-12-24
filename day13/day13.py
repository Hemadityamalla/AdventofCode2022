#Add import libs below

def parseInput(fin):
    sheet = set()
    for line in fin:
        if line == "\n":
            break
        coords = tuple(map(int, line.split(",")))
        sheet.add(coords)
    return sheet

def fold(sheet, axis, vertical=False):
    folded = set()

    for x, y in sheet:
        if vertical:
            if x > axis:
                x = axis - (x - axis)
        elif y > axis:
            y = axis - (y - axis)
        folded.add((x,y))
    return folded

def print_sheet(sheet):
    maxx = max(p[0] for p in sheet)
    maxy = max(p[1] for p in sheet)

    out = ""
    for y in range(maxy+1):
        for x in range(maxx+1):
            out += "#" if (x,y) in sheet else " "
        out += "\n"
    print(out, end="")



#fin = open("test.inp")
fin = open("day13.inp")
sheet = parseInput(fin)
#sheet = parseInput(fin)
line = next(fin)
axis = int(line[line.index("=")+1:])
vertical = "x" in line
sheet = fold(sheet, axis, vertical)

#Part 1
print("Part 1: ", len(sheet))

for line in fin:
    axis = int(line[line.index("=")+1:])
    sheet = fold(sheet, axis, "x" in line)



#Part 2
print("Part 2: ")
print_sheet(sheet)

