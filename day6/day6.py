#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().split("\n")



#datastream = parseInput(open("test.inp"))
datastream = parseInput(open("day6.inp"))


#Part 1
for stream in datastream:
    i = 0
    while True:
        idx = i+4
        if len(set([x for x in stream[i:idx]])) == 4:
            print(idx)
            break
        else:
            i+=1


print("Part 1: ", idx)

for stream in datastream:
    i = 0
    while True:
        idx = i+14
        if len(set([x for x in stream[i:idx]])) == 14:
            print(idx)
            break
        else:
            i+=1


#Part 2
print("Part 2: ", idx)

