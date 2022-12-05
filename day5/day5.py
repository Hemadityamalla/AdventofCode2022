#Add import libs below

def parseInput(fin):
    t = fin.read().rstrip().split("\n")
    idx = 0
    nstacks = 0
    instr = []
    for i,x in enumerate(t):
        if x.strip().startswith("1"):
            idx = i
            nstacks = int(x.strip()[-1])
        if x.strip().startswith("move"):
            xx = x.split()
            instr.append([int(xx[1]), int(xx[3]), int(xx[5])])
    st = list()
    for i in range(int(nstacks)):
        st.append(list())
    
    boxidx = [x for x in range(1,nstacks+2+3*(nstacks-1), 4)]
    for x in t[:idx]:
        for j in range(nstacks):
            if x[boxidx[j]] != " ":
                st[j].append(x[boxidx[j]])
    [x.reverse() for x in st]
    return st,instr




#stack, instr = parseInput(open("test.inp"))
stack, instr = parseInput(open("day5.inp"))

print(stack)
for ins in instr:
    numbox,st,end = ins
    for _ in range(numbox):
        stack[end-1].append(stack[st-1].pop())

#Part 1
print("Part 1: ", "".join(x[-1] for x in stack))

#stack, instr = parseInput(open("test.inp"))
stack, instr = parseInput(open("day5.inp"))
print(stack)
for ins in instr:
    numbox,st,end = ins
    combine = stack[st-1][-numbox:]
    for _ in range(numbox):
        stack[st-1].pop()
    
    for x in combine:
        stack[end-1].append(x)
    print(stack)

#Part 2
print("Part 2: ", "".join(x[-1] for x in stack))

