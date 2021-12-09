import numpy as np
class bingo_table:
    def __init__(self, table, idx):
        self.table = table
        self.idx = idx
        self.marker = np.ones([5,5])
        self.bingo = 0
    def checkBingo(self):
        if self.bingo == 0:
            row_sum = np.sum(self.marker, axis=0)
            col_sum = np.sum(self.marker, axis=1)
            if np.count_nonzero(row_sum == 0):
                rownum = np.nonzero(row_sum == 0)
                print("BINGO! on table", self.idx, " on row ", rownum[0])
                self.bingo = 1
                return [1, self.idx, rownum[0], -1]
            elif np.count_nonzero(col_sum == 0):
                colnum = np.nonzero(col_sum == 0)
                print("BINGO! on table", self.idx, " on col ", colnum[0])
                self.bingo = 1
                return [1, self.idx, -1, colnum[0]]
            else:
                print("No BINGO anywhere yet!", self.idx)
                return [0, self.idx, -1, -1]
        else: 
            print("Already bingo")
            return [0, self.idx, -1,-1]


def parseInput(fin):
    data = fin.read().rstrip().split("\n")
    randnums = [int(x) for x in data[0].split(",")]
    bingo_tables = []
    new_table = []
    for i in range(1,len(data)):
        if data[i] == "":
            bingo_tables.append(new_table)
            #print("table", i, " start")
            new_table = []
            continue
        else:
            #print(data[i])
            new_table.append([int(x) for x in data[i].split()])
    bingo_tables.append(new_table)
    return randnums, np.array(bingo_tables[1:])

def part1(t, row, col):
        return np.sum(t.table[t.marker == 1])


def init_tableClass(tables): 
    tab_list = []
    for cnt, tab in enumerate(tables):
        tab_list.append(bingo_table(tab, cnt))
    return tab_list

def processTable(tab_class, number):
    for tab in tab_class:
        id_row,id_col = np.nonzero(tab.table == number)
        tab.marker[id_row, id_col] = 0
    return tab_class


#rnums, tables = parseInput(open("test.inp"))
rnums, tables = parseInput(open("day4.inp"))
t_class = init_tableClass(tables)
outerbreak = 0
p1 = 0
if p1 == 1:
    for nums in rnums:
        t_class = processTable(t_class, nums)
        for tab in t_class:
            innerbreak, idx, row, col = tab.checkBingo()
            if innerbreak:
                outerbreak = 1
                break
        if outerbreak:
            finalanswer = part1(t_class[idx], row, col)
            print("Bingo at number ", nums, "part1: ", nums*finalanswer)
            break
else:
    
    bingo_counter = 0
    for nums in rnums:
        print(nums)
        t_class = processTable(t_class, nums)
        for tab in t_class:
            if bingo_counter < len(t_class):
                innerbreak,idx, row,col = tab.checkBingo()
                if innerbreak:
                    bingo_counter +=1
                    print("BINGOCOUNTER ", bingo_counter)
            else:
                finalanswer = part1(t_class[idx], row, col)
                print("last table to bingo:", idx, "part2: ", nums*finalanswer)
                outerbreak = 1
                break
        if outerbreak:
            break

        

#de = parseInput(open("day1.inp"))


#Part 1

#Part 2



















