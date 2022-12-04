#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().split("\n")



#pairs = parseInput(open("test.inp"))
pairs = parseInput(open("day4.inp"))

cnt = 0
sepsets = 0
for i,pair in enumerate(pairs):
    p1, p2 = [list(map(int, x.split("-"))) for x in pair.split(",")]
    s1 = set([x for x in range(p1[0],p1[1]+1)])
    s2 = set([x for x in range(p2[0],p2[1]+1)])
    if s1.issubset(s2) or s2.issubset(s1):
        cnt+=1
    if len(s1 & s2) == 0:
        sepsets+=1


#Part 1
print("Part 1: ", cnt)



#Part 2
print("Part 2: ", len(pairs)-sepsets)

