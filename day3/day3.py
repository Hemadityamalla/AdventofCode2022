import numpy as np
def parseInput(fin):
    d = fin.read().rstrip().split("\n")
    bin_nums = np.array([np.array([int(i) for i in x], dtype=np.int32) for x in d])
    
    return bin_nums
def convertToDec(binstr):
    decimal = 0
    for i in binstr:
        decimal = 2*decimal + int(i)
    return decimal


def mostcommonbit(arr):
    numones = np.sum(arr)
    if numones > (arr.size-numones):
        return 1
    else:
        return int(0)
def leastcommonbit(arr):
    numones = np.sum(arr)
    if numones > (arr.size-numones):
        return int(0)
    else:
        return int(1)

def part1(bin_nums):
    gamma_bits = []
    eps_bits = []
    for i in range(bin_nums.shape[1]):
        gamma_bits.append(str(mostcommonbit(bin_nums[:,i])))
        eps_bits.append(str(leastcommonbit(bin_nums[:,i])))
    return [convertToDec(gamma_bits), convertToDec(eps_bits)]

def o2filterBins(arr):
    if arr.size > 1:
        o2filterBins(arr(mostcommonbitidx(arr)))
    else:
        return arr

def co2filterBins(arr):
    if arr.size > 1:
        co2filterBins(arr(leastcommonbitidx(arr)))
    else:
        return arr

def mostcommonbitidx(bin_arr, it):
    arr = bin_arr[:, it]
    numones = np.sum(arr)
    print("numones:", numones, arr.size)
    if numones >= (arr.size-numones):
        print("arr", arr)
        idx = np.nonzero(arr == 0)[0]
        bin_arr = np.delete(bin_arr, idx, axis=0)
        print("newstuff1:",idx, bin_arr)
        return bin_arr
    else:
        idx = np.nonzero(arr == 1)[0]
        bin_arr = np.delete(bin_arr, idx, axis=0)
        print("new stuff0:",idx, bin_arr)
        return bin_arr
def leastcommonbitidx(bin_arr, it):
    arr = bin_arr[:, it]
    numones = np.sum(arr)
    print("numones:", numones, arr.size)
    if numones >= (arr.size-numones):
        print("arr", arr)
        idx = np.nonzero(arr)[0]
        bin_arr = np.delete(bin_arr, idx, axis=0)
        print("newstuff1:",idx, bin_arr)
        return bin_arr
    else:
        idx = np.nonzero(arr == 0)[0]
        bin_arr = np.delete(bin_arr, idx, axis=0)
        print("new stuff0:",idx, bin_arr)
        return bin_arr

def o2part2(bin_nums):
    bit_idx = 0
    while bin_nums[:,:].shape[0] > 1 and bit_idx < bin_nums.shape[1]:
        print(bin_nums[:,:])
        bin_nums = mostcommonbitidx(bin_nums,bit_idx)
        bit_idx += 1
    return bin_nums[0]
def co2part2(bin_nums):
    bit_idx = 0
    while bin_nums[:,:].shape[0] > 1 and bit_idx < bin_nums.shape[1]:
        print(bin_nums[:,:])
        bin_nums = leastcommonbitidx(bin_nums,bit_idx)
        bit_idx += 1
    return bin_nums[0]


def part2(bin_nums):
    oxy = []
    carb = []

    return [convertToDec(oxy), convertToDec(carb)]



#readings = parseInput(open("test.inp"))
readings = parseInput(open("day3.inp"))

#Part 1
gamma_rate, eps_rate = part1(readings)
print("Part 1:", gamma_rate*eps_rate, " rates: ", gamma_rate, eps_rate)
#
##Part 2
#print("Part2o2", o2part2(readings))
#print("Part2co2", co2part2(readings))
print("Part2full", convertToDec(o2part2(readings))*convertToDec(co2part2(readings)))
#oxy, carb = part1(readings)
#print("Part 2:", oxy*carb, " rates: ", oxy, carb)



















