#Add import libs below
from collections import defaultdict

def parseInput(fin):
    return [x.split() for x in fin.read().rstrip().split("\n")]






parsed = parseInput(open("test.inp"))
parsed = parseInput(open("day9.inp"))
head_pos,tail_pos = (0,0),(0,0)
headmarkers = defaultdict(int) #Counts how many times the head visits a position
headmarkers[head_pos]+=1
tailmarkers = defaultdict(int) #Counts how many times the tail visits a position
tailmarkers[tail_pos]+=1



dirupdate = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}
#surroundings = [(0,0), (0,1), (-1,1), (-1, 0), (-1,-1), (0, -1), (1,-1), (1,0)]
#for direction,steps in parsed:
#    print(direction, steps, head_pos, tail_pos)
#    
#    for i in range(int(steps)):
#        #Update headpos based on the direction
#        head_pos = tuple(i+j for i,j in zip(head_pos, dirupdate[direction]))
#        headmarkers[head_pos]+=1
#
#        #Compute the difference in the positions to move tail
#        diff = tuple(i-j for i,j in zip(head_pos, tail_pos))
#        #Update tailpos based on the position of head
#        if diff not in surroundings:
#            tail_pos = tuple(i+j for i,j in zip(tail_pos, diff)) 
#            tail_pos = tuple(i-j for i,j in zip(tail_pos, dirupdate[direction])) 
#            tailmarkers[tail_pos]+=1

def sign(x):
	return (x > 0) - (x < 0)
rope = [(0,0)]*10
seen1 = {(0,0)}
seen9 = {(0,0)}
for direction,steps in parsed:
    steps = int(steps)
    for _ in range(steps):
        hx, hy = rope[0]
        dx,dy = dirupdate[direction]
        rope[0] = hx+dx, hy+dy
        for i in range(9):
            hx, hy = rope[i]
            tx,ty = rope[i+1]
            dx,dy = hx-tx, hy-ty
            if dx**2 + dy**2 >= 4:
                rope[i+1]  = tx + sign(dx), ty + sign(dy)
        seen1.add(tuple(rope[1]))
        seen9.add(tuple(rope[9]))




#Part 1
print("Part 1: ", len(seen1))



#Part 2
print("Part 2: ", len(seen9))

