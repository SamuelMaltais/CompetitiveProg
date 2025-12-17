import random

triangles = []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        triangles.append(list(map(int, line.strip().split(','))))


def IsItIn(point, edges):
    p1, p2 = point

    count_x = 0
    count_y = 0
    for i in range(len(edges) - 1):
        x1, y1 = edges[i]
        x2, y2 = edges[i + 1]

        if x1 == x2:
            if min(y1, y2) < p2 < max(y1,y2):
                toAdd = 1 if x1 > p1 else 0
                count_x += toAdd

        if y1 == y2:
            if min(x1, x2) <= p1 <= max(x1,x2):
                toAdd = 1 if y1 >= p1 else -1
                count_y += toAdd
    
    x1, y1 = edges[0]
    x2, y2 = edges[-1]
    if x1 == x2:
        if min(y1, y2) < p2 < max(y1,y2):
            toAdd = 1 if x1 > p1 else 0
            count_x += toAdd

    return abs(count_x) % 2 == 1

best = 0
for i in range(len(triangles)):
    for j in range(i + 1, len(triangles)):
        mid_x = (triangles[i][0] + triangles[j][0]) // 2
        mid_y = (triangles[i][1] + triangles[j][1]) // 2
        
        print(i, j)
        x, y = triangles[i]
        x2, y2 = triangles[j]
        t1 = (max(x, x2), max(y,y2))
        t2 = (min(x, x2), min(y,y2))
        t3 = (min(x, x2), min(y,y2))
        t4 = (max(x, x2), min(y,y2))
        res = (abs(x - x2) + 1) * (abs(y2 - y) + 1)
        if res < best:
            continue

        ok = IsItIn((mid_x, mid_y), triangles)
        ok = True
        # ok = ok and IsItIn(t2, triangles)
        # ok = ok and IsItIn(t1, triangles) 
        # ok = ok and IsItIn(t3, triangles) 
        # ok = ok and IsItIn(t4, triangles)
        for _ in range(10000):
            if not ok:
                break 
            randx = random.randint(min(x,x2), max(x,x2))
            randy = random.randint(min(y,y2), max(y,y2))

            ok = ok and IsItIn((randx, randy), triangles)

        
        if ok:
            best = max(best,(abs(x - x2) + 1) * (abs(y2 - y) + 1))

print(best)

# 8911184
# 33199990
# 1440557528
# 1544362560