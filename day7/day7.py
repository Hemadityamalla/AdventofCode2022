#Add import libs below
from collections import deque, defaultdict

def parseInput(fin):
    fs = defaultdict(list)
    lines = fin.read().rstrip().split("\n")
    #Start of the file system scan- $ cd /
    fs["/"]
    cwd = "/"
    lineiter = 1
    while True:
        if lineiter > (len(lines)-1):
            break
        #print(len(lines), lineiter, cwd)
        typ,cmd = lines[lineiter].split()[:2]

        if typ == "$" and cmd == "cd":
            #Doing the change directory function
            if lines[lineiter].split()[-1] == "..":
                cwd = " ".join([x for x in cwd.split()[:-1]])
                #cwd.pop()
                lineiter+=1
            else:
                cwd = cwd+f" {lines[lineiter].split()[-1]}/"
                #cwd.append(f"{lines[lineiter].split()[-1]}/")
                lineiter+=1
        if typ == "$" and cmd == "ls":
            #Doing the list function
            lineiter+=1
            while not lines[lineiter].startswith("$"):
                a1, a2 = lines[lineiter].split()
                if a1 == "dir":
                    #di = cwd.append(f"{a2}/")
                    di = cwd+f" {a2}/"
                    fs[cwd].append(di)
                    fs[di]
                else:
                    fs[cwd].append(int(a1))
                lineiter+=1
                #print("Insidelist ", fs)
                if lineiter >= len(lines):
                    break
    return fs



def directory_size(fs, path):

    local_sizes = 0
    for li in fs[path]:
        if type(li) == int:
            local_sizes += li
        else:
            local_sizes += directory_size(fs, li)
    sizes[path] = local_sizes
    return local_sizes




#filesys = parseInput(open("test.inp"))
filesys = parseInput(open("day7.inp"))

sizes = defaultdict(int)
used = directory_size(filesys,"/")
free = 70_000_000 - used
need = 30_000_000 - free
#Part 1
print("Part 1: ",sum(filter(lambda x: x<100_000, sizes.values())))

suitable_dirs = list(filter(lambda x: x>need, sizes.values()))
suitable_dirs.sort()

#Part 2
print("Part 2: ",suitable_dirs[0])

