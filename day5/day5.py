import numpy as np
from itertools import repeat
def parseInput(fin):
    lines = fin.read().rstrip().split("\n")
    coord_matrix = []
    for l in lines:
        local = []
        local.append([int(x) for x in l.split()[0].split(",")])
        local.append([int(x) for x in l.split()[2].split(",")])
        coord_matrix.append(local)
    return coord_matrix

def max_min_coords(cmat):
    max_c = []
    min_c = []
    #X coords
    max_c.append(max(np.max(cmat[:,0]), np.max(cmat[:,2])))
    min_c.append(min(np.min(cmat[:,0]), np.min(cmat[:,2])))
    #Y coords
    max_c.append(max(np.max(cmat[:,1]), np.max(cmat[:,3])))
    min_c.append(min(np.min(cmat[:,1]), np.min(cmat[:,3])))

    return min_c, max_c
def hor_vert_connections(coords):
    coord_diff = np.zeros([coords.shape[0], 2])
    coord_diff[:,0] = np.abs(coords[:,0]-coords[:,2])
    coord_diff[:,1] = np.abs(coords[:,1]-coords[:,3])
    return coords[np.count_nonzero(coord_diff, axis=1) != 2, :]
    
def map_diag(coords, path):
    for i in range(coords.shape[0]):
        x_coords = [coords[i][0], coords[i][2]]
        y_coords = [coords[i][1], coords[i][3]]
        c_x = abs(np.diff(x_coords))
        c_y = abs(np.diff(y_coords))
        print([c_x, c_y])
        if c_x == 0 :
            #Vertical line
            y_start = np.arange(min(y_coords), max(y_coords)+1)
            for y in y_start:
                path[coords[i][0], y] += 1
        else:#c_y != 0 and c_x == 0:
            #Horizontal line
            x_start = np.arange(min(x_coords), max(x_coords)+1)
            
            for x in x_start:
                path[x,coords[i][1]] += 1
        #!else:
        #!    print("Whch line", coords[i][:])
    return path





def autorange(a, b):
    if a > b:
        yield from range(a, b-1 ,-1)
    yield from range(a, b+1)
def diag(ax, ay,bx,by):
    if ax!=bx and ay!=by:
        yield from zip(autorange(ax, bx), autorange(ay,by))


#de = parseInput(open("test.inp"))
de = parseInput(open("day5.inp"))
coords = np.array(de)
coords = np.reshape(coords, [coords.shape[0], coords.shape[1]*coords.shape[2]])
min_c, max_c = max_min_coords(coords)
path = np.zeros([x+1 for x in max_c])
hor_vert_coords = hor_vert_connections(coords)
path = map_diag(hor_vert_coords, path)

#Part 1
print(path)
print("Part1: ", np.count_nonzero(path.T >= 2))

#Part 2
for i in range(coords.shape[0]):
    line = coords[i][:]
    for p in diag(*line):
        print(p)
        path[p] += 1
print(path)
print("Part2: ", np.count_nonzero(path.T >= 2))


















