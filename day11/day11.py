#Add import libs below
from operator import attrgetter
import re
import math



class Monkey:
    def __init__(self, items, op, test, passconds):
        self.items = items
        self.op = op
        self.test = test
        self.passconds = passconds
        self.itemshandled = 0

    def getItemsHandled(self):
        return self.itemshandled


def parseInput(fin):
    monkeylist = []
    t = fin.read().rstrip("\n").split("\n")
    it = 0
    while t[it:it+6]:
        #Parsing the lines for each monkey
        monke = t[it:it+6]
        items = [int(x.strip()) for x in monke[1].split(":")[-1].split(",")]
        #pat1 = re.compile(r"(old|\d+) (\*|\+) (old|\d+)")
        #match = re.findall(pat1, monke[2].split("new = ")[-1])
        op = monke[2].split("new = ")[-1] #This is a string expression that we will 'eval()'
        test = int(monke[3].split(" ")[-1])
        iftrue,iffalse =int(monke[4].split(" ")[-1]), int(monke[5].split(" ")[-1])
        M = Monkey(items, op, test, [iftrue,iffalse])
        monkeylist.append(M)

        it+=7
    return monkeylist


def inspectItems(mon):
    while mon.items:
        old = mon.items.pop(0)
        mon.itemshandled+=1
        worrylevel = int(eval(mon.op)/3)
        if worrylevel%mon.test == 0:
            mainMonkeyList[mon.passconds[0]].items.append(worrylevel)
        else:
            mainMonkeyList[mon.passconds[1]].items.append(worrylevel)
def inspectItemspart2(mon):
    while mon.items:
        old = mon.items.pop(0)
        mon.itemshandled+=1
        #worrylevel = int(eval(mon.op)/3)
        modul = math.lcm(*map(attrgetter("test"), mainMonkeyList))
        worrylevel = eval(mon.op)%modul
        if worrylevel%mon.test == 0:
            mainMonkeyList[mon.passconds[0]].items.append(worrylevel)
        else:
            mainMonkeyList[mon.passconds[1]].items.append(worrylevel)

#mainMonkeyList = parseInput(open("test.inp"))
mainMonkeyList = parseInput(open("day11.inp"))


nrounds = 10000
for i in range(nrounds):
    print(i)
    #Here we perform the inpection action for all the items of a monkey
    for monkey in mainMonkeyList:
        inspectItemspart2(monkey)
itemsHandled = sorted([x.getItemsHandled() for x in mainMonkeyList])
#Part 1
print("Part 1: ", itemsHandled[-1]*itemsHandled[-2])



#Part 2
print("Part 2: ", )

