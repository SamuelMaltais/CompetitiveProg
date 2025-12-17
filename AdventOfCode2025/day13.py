import numpy as np
from copy import deepcopy
import math

l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

presents = []
curr = []
challenges = []

for line in l:
    if line == "":
        if curr != []:
            presents.append(curr)
        curr = []
    elif ":" in line and "x" in line:
        challenges.append((tuple(map(int,line.split(":")[0].split('x'))), tuple(map(int,line.split(":")[1].split()))))
    elif ":" in line:
        pass
    else:
        curr.append(list(line))


def rotateShape(shape):
    r = np.array(shape)
    return np.rot90(r).tolist()

def flipShape(shape):
    r = np.array(shape)
    return np.flip(r).tolist()

def tryAdd(shape, grid, i, j):
    if len(shape) + i > len(grid):
        return False
    if len(shape[0]) + j > len(grid[0]):
        return False
    for di in range(len(shape)):
        for dj in range(len(shape)):
            if grid[i + di][j + dj] == "#" and shape[di][dj] == "#":
                return False
            grid[i + di][j + dj] = shape[di][dj]
    return True

found = False
def testAll(i, shapes, grid):
    
    global found
    if found:
        return

    if i >= len(shapes):
        found = True
        return
    
    currShape = shapes[i]
    for _ in range(2):
        for _ in range(4):
            for gi in range(len(grid)):
                for gj in range(len(grid[0])):
                    grid_cp = deepcopy(grid)
                    if tryAdd(currShape, grid_cp, gi, gj):
                        testAll(i + 1, shapes, grid_cp)
                        return
            currShape = rotateShape(currShape)
        currShape = flipShape(currShape)

tot = 0
for chal in challenges:
    (x, y), p = chal
    grid = [["." for _ in range(y)] for _ in range(x)]
    
    shapes = []
    aire = 0


    for i in range(len(p)):
        for _ in range(p[i]):
            shapes.append(presents[i])

    c1 = x // 3
    c2 = y // 3
    if c1 * c2  >= len(shapes):
        tot += 1

    s = min(x, y)




# 2 -> 4 4
# 4 -> 5 5
# 

print(tot)

# print(challenges)
# print(presents)
