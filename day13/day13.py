#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().replace("\n\n", "\n").split("\n")



if input("test/real?") == "test":
    parsed = parseInput(open("test.inp"))
else:
    parsed = parseInput(open("day13.inp"))


def bubblesort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            res = compare(arr[i], arr[i+1])
            if res > 0:
                #Swap the elements here
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


def compare(a,b):
    aint = type(a) is int
    bint = type(b) is int
    if aint and bint:
        return a-b #If this is negative then the signal is correct


    if aint != bint:
        if aint:
            return compare([a], b)
        else:
            return compare(a,[b])

    for i,j in zip(a,b):
        res = compare(i,j)
        if res != 0:
            return res
    return len(a) - len(b)

paired = [(eval(parsed[i]), eval(parsed[i+1])) for i in range(0,len(parsed), 2)]
right = []
for i,p in enumerate(paired):
    check = compare(p[0], p[1])
    if check < 0:
        right.append(i+1)

#Part 1
print("Part 1: ", sum(right))
parsed.extend(("[[2]]", "[[6]]"))
parsed = bubblesort([eval(x) for x in parsed])
divpackets = [[[2]], [[6]]]


x,y = parsed.index(divpackets[0])+1, parsed.index(divpackets[1])+1
#Part 2
print("Part 2: ", x*y)

