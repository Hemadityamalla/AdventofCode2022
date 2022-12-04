#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().split("\n")



#rucksacks = parseInput(open("test.inp"))
rucksacks = parseInput(open("day3.inp"))


plist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0
for r in rucksacks:
    idx = int(len(r)/2)
    print("".join(set(r[:idx]).intersection(r[idx:])))
    priority += plist.index("".join(set(r[:idx]).intersection(r[idx:])))+1

#Part 1
print("Part 1: ", priority)

priority = 0
for r in range(0, len(rucksacks), 3):
    common ="".join(set(rucksacks[r])&set(rucksacks[r+1])&set(rucksacks[r+2])) 
    print(common)
    priority += plist.index(common)+1

    

#Part 2
print("Part 2: ", priority)

