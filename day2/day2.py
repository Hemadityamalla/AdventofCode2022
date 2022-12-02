#Add import libs below

def parseInput(fin):
    return fin.read().rstrip().split("\n")


#Rock: A,X
#Paper: B,Y
#Scissors: C,Z

lose = ["B X", "C Y", "A Z"]
win = ["B Z", "A Y", "C X"]
draw = ["B Y", "A X", "C Z"]

shapescore = {"X":1, "Y":2, "Z":3}




round_list = parseInput(open("test.inp"))
round_list = parseInput(open("day2.inp"))


score = 0
for r in round_list:
    if (r in win):
        score+=(6+shapescore[r[-1]])
        print(score)


    elif (r in lose):
        score+=(shapescore[r[-1]])
        print(score)
    else:
        score+=(3+shapescore[r[-1]])
        print(score)

#Part 1
print("Part 1: ", score)


#lose = ["B X", "C Y", "A Z"]
#win = ["B Z", "A Y", "C X"]
#draw = ["B Y", "A X", "C Z"]
#shapescore = {"X":1, "Y":2, "Z":3}

strat = {"X":0, "Y":3, "Z":6}
Astrat = {"X":"Z", "Y":"X", "Z":"Y"}
Bstrat = {"X":"X", "Y":"Y", "Z":"Z"}
Cstrat = {"X":"Y", "Y":"Z", "Z":"X"}
score = 0
for r in round_list:
    if r[0] == "A":
        score+=(strat[r[-1]]+shapescore[Astrat[r[-1]]])
    elif r[0] == "B":
        score+=(strat[r[-1]]+shapescore[Bstrat[r[-1]]])
    else: 
        score+=(strat[r[-1]]+shapescore[Cstrat[r[-1]]])


#Part 2
print("Part 2: ", score)

