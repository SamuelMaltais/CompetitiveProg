triangles = []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        triangles.append(list(map(int, line.strip().split(','))))

tot = 0
best = 0

max_x = 0
max_y = 0
for t in triangles:
    max_x = max(t[0], max_x)
    max_y = max(t[1], max_y)

candidats = set()

def fill(p1, p2, grid):
    global candidats

    if p1[0] == p2[0]:
        gros = max(p1[1], p2[1])
        petit = min(p1[1], p2[1])

        for i in range(petit, gros + 1):
            grid[p1[0]][i] = "X"
    else:
        gros = max(p1[0], p2[0])
        petit = min(p1[0], p2[0])
        for i in range(petit, gros + 1):
            grid[i][p1[1]] = "X"
            
print('Here')

def dirCheck(p, dir, grid):
    x, y = p
    dx, dy = dir
    
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return False
    
    if grid[x][y] == "X":
        return True
    
    x += dx
    y += dy

    return dirCheck((x,y), (dx,dy), grid)

def isIn(point, grid):
    ok = True
    ok = ok and dirCheck(point, (0,1), grid)
    ok = ok and dirCheck(point, (0,-1), grid)
    ok = ok and dirCheck(point, (1,0), grid)
    ok = ok and dirCheck(point, (-1,0), grid)
    return ok


max_x += 2
max_y += 2
print("start")
grid = [['.' for _ in range(max_y)] for _ in range(max_x)]
print("done")

fill(triangles[0], triangles[-1], grid)
for i in range(len(triangles) - 1):
    print("Fill", i)
    fill(triangles[i], triangles[i + 1], grid)



candidats = []
for i in range(len(triangles)):
    for j in range(i + 1, len(triangles)):
        x, y = triangles[i]
        x2, y2 = triangles[j]
        candidats.append(((x, y), (x2,y2)))

poss = []
for i in range(len(candidats)):
    x1, y1 = candidats[i][0]
    x2, y2 = candidats[i][1]
    
    ok = True
    print(i, len(candidats))
    for p1 in range(min(x1, x2), max(x1, x2) + 1):
        for p2 in range(min(y1, y2), max(y1, y2) + 1):
            if not ok:
                continue
            ok = ok and isIn((p1,p2), grid)
    if ok:
        best = max(best, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

        for p1 in range(min(x1, x2), max(x1, x2) + 1):
            for p2 in range(min(y1, y2), max(y1, y2) + 1):
                grid[p1][p2] = "X"

print(best)
