#Add import libs below
from collections import defaultdict

def parseInput(fin):
    return fin.read().rstrip().split("\n")



#instrlist = parseInput(open("test.inp"))
instrlist = parseInput(open("day10.inp"))

crt = []
row = ""
x,cycle = 1,1
total = 0
for instr in instrlist:
    #Check if sprite is within the cycle and draw
    row+="#" if x<=cycle %40<=x+2 else " "
    cycle+=1
    if instr.startswith("addx"):
        if cycle % 40 == 20:
            total+= cycle*x
        #Check for new line and reset row 
        elif cycle%40 == 1:
            crt.append(row)
            row = " "
        row+="#" if x<=cycle %40<=x+2 else " "
        cycle+=1
        x+=int(instr.split()[-1])
    # This is the noop instruction
    if cycle%40==20:
        total+= cycle*x
    elif cycle %40 == 1:
        crt.append(row)
        row = " "

#Part 1
print("Part 1: ", total)


#Part 2
print("Part 2: \n", "\n".join(x for x in crt))

