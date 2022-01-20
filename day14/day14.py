#Add import libs below
from collections import defaultdict
from collections import Counter

class Node:
    def __init__(self, v, nxt=None):
        self.value = v
        self.next = nxt

def react(poly, rules, n, last):
    for _ in range(n):
        newpoly = defaultdict(int)
        for pair in poly:
            products = rules.get(pair)
            if products:
                n = poly[pair]
                newpoly[products[0]] += n
                newpoly[products[1]] += n
            else:
                newpoly[pair] = poly[pair]
        poly = newpoly
        counts = defaultdict(int, {last:1})
        for (a,_), n in poly.items():
            counts[a] += n
    return poly, max(counts.values()) - min(counts.values())


#fin = open("test.inp")
fin = open("day14.inp")
template = fin.readline().rstrip()
bleh = fin.readline().rstrip()
rules = {}
for line in map(str.rstrip, fin):
    (a,b), c = line.split(" -> ")
    rules[a, b] = ((a,c), (c,b))

poly = defaultdict(int)
for pair in zip(template, template[1:]):
    poly[pair] += 1


#Part 1
poly, ans1 = react(poly, rules, 10, template[-1])
print("Part 1: ", ans1)



#Part 2
poly, ans2 = react(poly, rules, 30, template[-1])
print("Part 2: ", ans2)

