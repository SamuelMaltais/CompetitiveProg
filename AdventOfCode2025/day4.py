l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(list(line.strip()))

tot = 0

def check(grid,i,j):
    if not (0 <= i < len(grid) and 0<= j < len(grid[0])):
        return 0
    if grid[i][j] == "@":
        return 1
    return 0

changes = True
while changes:
    changes = False
    for i in range(len(l)):
        for j in range(len(l[0])):
            curr = 0
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di != 0 or dj != 0:
                        curr += check(l, i + di, j + dj)
            #print(i, j, curr)
            if curr < 4 and l[i][j] == '@':
                l[i][j] = '.'
                changes = True
                tot += 1
print(tot)