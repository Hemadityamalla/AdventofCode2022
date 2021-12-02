import numpy as np
def parseInput(fin):
    d = fin.read().rstrip().split("\n")
    d = [x.split() for x in d]
    
    return d

def part1(dirs, position):
    for i in dirs:
        if i[0] == "forward":
            position[0] += int(i[1])
        elif i[0] == "down":
            position[1] -= int(i[1])
        else:
            position[1] += int(i[1])
    return position

def part2(dirs, position):
    aim = 0
    for i in dirs:
        mag = int(i[1])
        if i[0] == "forward":
            position[0] += mag
            position[1] -= aim*mag
        elif i[0] == "down":
            aim += mag
        else:
            aim -= mag
        print(i, position, aim)
    return position



#dirs = parseInput(open("test.inp"))
dirs = parseInput(open("day2.inp"))

#Part 1
pos = [0,0]
pos = part1(dirs, pos)
print("Part 1:", abs(pos[0])*abs(pos[1]), " position: ", pos)

#Part 2
pos = [0,0]
pos = part2(dirs, pos)
print("Part 2:", abs(pos[0])*abs(pos[1]), " position: ", pos)



















