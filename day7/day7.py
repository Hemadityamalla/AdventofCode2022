#Add import libs below

def parseInput(fin):
    return list(map(int, fin.readline().split(",")))



#parsed = parseInput(open("test.inp"))
parsed = parseInput(open("day7.inp"))

#The median of out list is the minimizer (check the internet for the mathematical proof)

#Sort the list of numbers
parsed.sort()

#Finding the median
median = parsed[len(parsed) // 2]
min_fuel = sum(abs(x - median) for x in parsed)



#Part 1
print("Part 1: ", min_fuel)
def sum_distances(nums, x):
    tot = 0
    for n in nums:
        delta = abs(n-x)
        tot += (delta *(delta+1))//2
    return tot

mean = sum(parsed) // len(parsed)
p2 = min(sum_distances(parsed, mean), sum_distances(parsed, mean+1))

#Part 2
print("Part 2: ", p2)

