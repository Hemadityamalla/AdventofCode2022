#Add import libs below
from collections import deque



SYNTAX_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
TRANS_TABLE = str.maketrans("([{<", ")]}>") #One-one mapping to each open and closed bracket
COMPL_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}

def check(s):
#Takes a string of parenthesis and checks for syntax error
#Based on dyck automata
    stack = deque()
    for c in s:
        if c in "([{<":
            stack.append(c.translate(TRANS_TABLE))
        elif stack.pop() != c:
            return SYNTAX_SCORE[c], 0
    score2 = 0
    while stack:
        score2 *= 5
        score2 += COMPL_SCORE[stack.pop()]

    return 0,score2

#No need to explicitly parse input

fin = open("day10.inp")
tot_syntax = 0
autocompl_scores = list()
for l in map(str.rstrip, fin):
    score1, score2 = check(l)
    tot_syntax += score1
    if score2 > 0:
        autocompl_scores.append(score2)



#Part 1
print("Part 1: ", tot_syntax)



#Part 2
autocompl_scores.sort()
mid_val = autocompl_scores[len(autocompl_scores) // 2]
print("Part 2: ", mid_val)

