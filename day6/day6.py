#Add import libs below
from collections import defaultdict

def parseInput(fin):
    return list(map(int, fin.read().split(",")))



#fish = parseInput(open("test.inp"))
fish = parseInput(open("day6.inp"))


#Evolve fish for each day, with a new list each day
ndays = 80
for _ in range(ndays):
    newfish = list()
    for timer in fish:
        timer -= 1 #Progress by a day
        if timer < 0:
            #Reproduction
            newfish.append(8)
            newfish.append(6)
        else:
            newfish.append(timer)
    fish = newfish



#Part 1
print("Part 1: ", len(fish))

ndays = 256
#This is a large number of days and we dont have the memory space to simulate using a list. So we "bin" fish together based on their reproduction times
def evolve(fish, days):
    for _ in range(days):
        newfish = defaultdict(int)

        for t,n in fish.items():
            t -= 1
            if t<0:
                newfish[6] += n
                newfish[8] += n
            else:
                newfish[t] += n
        fish = newfish
    return fish, sum(fish.values())

#Creating the "binning "
fish_bin = defaultdict(int)
for i in fish:
    fish_bin[i] += 1

#Part 2
_ , p2 = evolve(fish_bin, 256 - 80)
print("Part 2: ", p2)

