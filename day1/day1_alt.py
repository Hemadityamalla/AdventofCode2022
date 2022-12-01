#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().split("\n\n")




#parsed = parseInput(open("test.inp"))
parsed = parseInput(open("day1.inp"))


#Part 1
a2 = [sum(int(y) for y in x.split("\n")) for x in parsed]
#for x in parsed:
#    if x != "":
#        a1+=int(x)
#    else:
#        a2.append(a1)
#        a1=0
#a2.append(a1)
print("Part 1: ",max(a2))



#Part 2
print("Part 2: ", sum(sorted(a2, reverse=True)[0:3]))

