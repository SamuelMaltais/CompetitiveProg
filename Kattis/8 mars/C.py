import sys

sys.setrecursionlimit(999999999)

n = int(input())



grid = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(False)
    grid.append(row)

def check_(grid, i, j, di, dj):
    if not(0 <= i < len(grid) and 0 <= j < len(grid)):
        return True
    if grid[i][j]:
        return False
    return check_(grid, i + di, j + dj, di, dj)

ok = True
for _ in range(n):
    queen = input().split()
    grid[int(queen[0])][int(queen[1])] = True


ok = True
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if not( dj == 0 and di == 0):
                        ok = ok and check_(grid, i + di, j + dj, di, dj)
                        if not ok:
                            break

if ok:
    print("CORRECT")
else:
    print("INCORRECT")