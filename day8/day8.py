#Add import libs below

#No explicitly parsing input in this problem
    



#fin = open("test.inp")
fin = open("day8.inp")

to_count = [2,4,3,7] #Pattern lengths we want to count
count = 0
for line in fin:
    digits = line.split("|")[1].split()
    for d in digits:
        if len(d) in to_count:
            count += 1

#Part 1
print("Part 1: ", count)


def deduce_mapping(patterns):
    p2d = {}
    for p,plen in patterns:
        if plen == 2:
            p2d[p] = 1
        elif plen == 3:
            p2d[p] = 7
        elif plen == 4:
            p2d[p] = 4
        elif plen == 7:
            p2d[p] = 8
    d2p = {v: k for k, v in p2d.items()}
    for p,plen in patterns:
        if p in p2d:
            #Pattern already known
            continue
        elif plen == 5:
            if len(p & d2p[1]) == 2:
                p2d[p] = 3
            elif len(p & d2p[4]) == 3:
                p2d[p] = 5
            else:
                p2d[p] = 2
        else:
            if len(p & d2p[4]) == 4:
                p2d[p] = 9
            elif len(p & d2p[7]) == 2:
                p2d[p] = 6
            else:
                p2d[p] = 0
    return p2d


fin = open("day8.inp")
total = 0
for line in fin:

    raw_pattern, raw_digits = map(str.split, line.split("|"))
    #patterns, digits = [], []
    #for p in raw_patterns:
    #    patterns.append((frozenset(p), len(p)))
    #for d in raw_digits:
    #    digits.append((frozenset(d), len(d)))
    #Above loops can be reduced to single lines like this

    patterns = tuple(map(lambda p:(frozenset(p), len(p)), raw_pattern))
    digits = tuple(map(lambda d:(frozenset(d), len(d)), raw_digits))
    p2d = deduce_mapping(patterns)
    total += p2d[digits[0][0]]*1000
    total += p2d[digits[1][0]]*100
    total += p2d[digits[2][0]]*10
    total += p2d[digits[3][0]]



#Part 2
print("Part 2: ", total)

