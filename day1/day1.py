import numpy as np
def parseInput(fin):
    depths = fin.read().rstrip().split("\n")
    depths = [int(x) for x in depths]
    return depths




#de = parseInput(open("test.inp"))
de = parseInput(open("day1.inp"))

depths = np.array(de)

#Part 1
print("Part 1:", np.sum(np.diff(depths) > 0))

#Part 2
n = int(depths.shape[0]/3)
sum_depth = np.array([np.sum(depths[i:i+3]) for i in range(depths.size-2)])
print("Part 3:", np.sum(np.diff(sum_depth) > 0))



















